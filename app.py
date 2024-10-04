from flask import Flask,render_template, request ,flash , redirect,url_for ,session
from user import UserOperation
from encryption import Encryption
from validation import empty
from validation import checkdigit
from validation import checkalpha
from provider import ProviderOperation
from datetime import datetime 
import razorpay
from voice_search import voiceSearch

app = Flask(__name__)   # this is the flask object
app.secret_key="oij34jojh4"

client = razorpay.Client(auth=("rzp_test_ncA8cq0QRQXDlq","oAa0hlEpbvYHrg3Of8G139kE"))

userObj =UserOperation() #object of user module
eObj = Encryption() #object encription
providerObj=ProviderOperation() 

@app.route('/')
def index ():
     return render_template('index.html')
    #  return "Good night"


@app.route('/signup',methods=['POST','GET'])    
def signup():
     if request.method == 'GET':
          return render_template('user_signup.html')
     else:
          firstName=request.form['firstName'] 
          lastName=request.form['lastName']
          email=request.form['email']
          mobile=request.form['mobile']
          state=request.form['state']
          city=request.form['city']
          password=request.form['password']
          #------------validation-------
          datalist =[firstName,lastName,email,mobile,password]
          if(empty(datalist)):
               flash('Field cannot be empty !!')
               return redirect(url_for("signup"))
          if(checkdigit(mobile)) :
               flash("mobile must  be number")
               return redirect(url_for('signup'))
          if(checkalpha(firstName) or checkalpha(lastName)):
               flash("Number must be alphabet")
               return redirect(url_for('signup'))
               


          password=eObj.convert(password) # encription

          userObj.user_signup(firstName,lastName,email,mobile,state,city,password)
          flash('Register sucessful. login Now!!')
          return redirect(url_for('user_login'))

@app.route('/user_login', methods=['POST','GET'])
def  user_login():
     if request.method == 'GET':
        return render_template('user_login.html')
     else:
          email=request.form['email']
          password=request.form['password']
          # validation
          datalist =[email,password]
          if(empty(datalist)):
               flash('Field cannot be empty !!')
               return redirect(url_for("user_login"))
          password=eObj.convert(password) #encription

          status =userObj.user_login(email,password)
          if(status==0):
               flash("invalid email and password")
               return redirect(url_for('user_login'))
          else:
               return redirect(url_for('user_dashboard'))
    #  return 'about page'

@app.route('/user_logout')
def user_logout():
     session.clear()
     flash('successfully logout !!')
     return redirect(url_for('user_login'))

@app.route('/user_delete' ,methods =['POST','GET'])
def user_delete():
      if 'userEmail' in session:
          if request.method == 'GET':
               userObj.user_delete()
               session.clear()
               flash('Account delete sucessfully! see you soon ')
               return redirect(url_for('signup'))
      else:
          flash('to access this page login first')  
          return redirect(url_for('user_login'))



@app.route('/user_dashboard', methods=['POST','GET'])
def user_dashboard():
     if 'userEmail' in session:
          if request.method == 'GET':
               return render_template('user_dashboard.html')
     else:
          flash('to access this page login first')  
          return redirect(url_for('user_login'))
     
     
@app.route('/user_profile',methods=['POST','GET'])
def user_profile():
     if 'userEmail' in session:
          if request.method=='GET':
               record=userObj.user_profile()
               return render_template('user_profile.html',record=record)     
          else:
               firstName =request.form['firstName']
               lastName =request.form['lastName']
               mobile =request.form['mobile']
          # ---validation
               datalist =[firstName,lastName,mobile]
               if(empty(datalist)):
                    flash('Field cannot be empty !!')
                    return redirect(url_for("user_profile"))
          
               if(empty(mobile)):
                    flash('mobile cannot be empty !!')
                    return redirect(url_for("user_profile"))
          
               if(checkalpha(firstName) or checkalpha(lastName)):
                    flash('mobile cannot be empty !!')
                    return redirect(url_for("user_profile"))
#   -------------and validation
               userObj.user_login_update(firstName,lastName,mobile) 
               flash('profile update successfully')
               return redirect(url_for('user_profile'))
     else:
          flash('to access this page login first')  
          return redirect(url_for('user_login'))
     
@app.route('/user_password_change',methods=['POST','GET'])
def user_password_change():
     if 'userEmail' in session:
          if request.method=='GET':
               return render_template('user_password_change.html')
          else:
               oldpassword= request.form['oldpassword']
               newpassword= request.form['newpassword']
               # Validation
               dataList=[oldpassword,newpassword]
               if(empty(dataList)):
                    flash('fleld cannot be empty')
                    return redirect(url_for('user_password_change'))
               if(newpassword == oldpassword): #check both are same
                    flash("old password and new password canno't be change")
                    return redirect(url_for("user_password_change"))

               oldpassword=eObj.convert(oldpassword) # encription
               newpassword=eObj.convert(newpassword) # encription
               status=userObj.checkpassword(oldpassword)
               if(status):
                    userObj.user_password_change(newpassword)
                    session.clear()
                    flash('password change sucessfully .. login now')
                    return redirect(url_for('user_login'))
               else:
                    flash('your old password invalid.. tr again!')
                    return redirect(url_for('user_password_change'))
     else:
          flash('to access this page login first')  
          return redirect(url_for('user_login'))   


@app.route('/user_service' ,methods =['POST','GET'])
def user_service():
      if 'userEmail' in session:
               if request.method == 'GET':
                    sList=userObj.user_service()
                    return render_template('user_service.html',sList=sList)
               else:
                    skill=request.form['skill']
                    record1=userObj.user_service_search(skill)
                    sList=userObj.user_service() 
                    return render_template('user_service.html',sList=sList,record1=record1) 
      else :
           flash('to access this page login first')
           return redirect(url_for('user_login'))
      
      


@app.route('/user_service_city' ,methods =['POST','GET'])
def user_service_city():
      if 'userEmail' in session:
               if request.method == 'GET':
                    sList=userObj.user_service_city()
                    return render_template('user_service_city.html',sList=sList)
               else:
                    skill=request.form['skill']
                    city=request.form['city']
                    record=userObj.user_service_city_search(skill,city)
                    sList=userObj.user_service() 
                    return render_template('user_service_city.html',sList=sList,record=record)
      else :
           flash('to access this page login first')
           return redirect(url_for('user_login'))




@app.route("/user_service_view", methods=["POST", "GET"])
def user_service_view():
    if 'userEmail' in session:
        if request.method == 'GET':
             providerEmail= (request.args.get("providerEmail"))
             record=userObj.user_service_view(providerEmail)
             getStar= userObj.user_getStar(providerEmail)
             return render_template("user_service_view.html", record=record, getStar=getStar)
    else:
        flash("To access this page please login now!")
        return redirect(url_for("user_login"))
    
@app.route("/user_service_book", methods=["POST", "GET"])
def user_service_book():
    if 'userEmail' in session:
        if request.method == 'POST':
             providerEmail= request.args.get("providerEmail")
             charges= int(request.args.get("charges"))
             bookingDate= request.form["bookDate"]

             data ={"amount": charges*100, "currency":"INR","receipt":"xyz"}
             payment =client.order.create(data=data)
             pdata=[charges*100,payment['id'],providerEmail,bookingDate]
             return render_template("payment.html", pdata=pdata)
    else:
        flash("To access this page please login now!")
        return redirect(url_for("user_login"))
    


  
@app.route('/success', methods=["POST"])
def success():
    if('userEmail' in session):
        if(request.method=='POST'):
            providerEmail=request.args.get('providerEmail')
            bookingDate=request.args.get('bookingDate')
            charges=request.args.get('charges')
            pid=request.form.get("razorpay_payment_id")
            ordid=request.form.get("razorpay_order_id")
            sign=request.form.get("razorpay_signature")
            params={
            'razorpay_order_id': ordid,
            'razorpay_payment_id': pid,
            'razorpay_signature': sign
            }
            final=client.utility.verify_payment_signature(params)
            if final == True:
                
                userObj.booking(providerEmail,pid,bookingDate,charges)
                flash("Payment Done Successfully!! payment ID is "+str(pid))
                return redirect(url_for('user_service'))
            else:
                flash("Something Went Wrong Please Try Again")
                return redirect(url_for('user_camp_explore'))
    else:
        flash("please login to access this page..")
        return redirect(url_for('user_login'))  

@app.route('/user_booking_history', methods=['POST','GET'])
def user_booking_history():
     if 'userEmail' in session:
          if request.method == 'GET':
             record=userObj.user_booking_history()    
             return render_template('user_booking_history.html',record=record)
     else:
          flash('to access this page login first')  
          return redirect(url_for('user_login'))

#______________user voice search________________

@app.route('/user_voice_search', methods=['POST','GET'])
def user_voice_search():
     if 'userEmail' in session:
          if request.method == 'GET':
               skill =voiceSearch()
               record1=userObj.user_service_search(skill)
               sList=userObj.user_service() 
               if(record1):
                    return render_template('user_service',sList=sList,record1=record1)
               else:
                    flash('no skills matched')    
                    return render_template('user_service.html',sList=sList,record1=record1)
     else:
          flash('to access this page login first')  
          return redirect(url_for('user_login'))    


#______________________user review________________

@app.route('/user_review', methods=['POST','GET'])
def user_review():
     if 'userEmail' in session:
          if request.method == 'GET':
               providerEmail=request.args.get('providerEmail')
               record=userObj.user_review_show(providerEmail) #ov
               return render_template('user_review.html',providerEmail=providerEmail,record=record) #record ov
          else:
               providerEmail=request.args.get('providerEmail')
               star=request.form['star']
               comment=request.form['comment']
               userObj.user_review(providerEmail,star,comment)
               flash("review submitted sucessfully")
               return redirect(url_for('user_review'))
     else:
          flash('to access this page login first')  
          return redirect(url_for('user_login'))


     
      

#-----------------------------provider-user-------------------------------  
@app.route('/provider_signup',methods=['POST','GET'])    
def provider_signup():
     if request.method == 'GET':
          return render_template('provider_signup.html')
     else:
        
          firstName=request.form['firstName'] 
          lastName=request.form['lastName']
          email=request.form['email']
          mobile=request.form['mobile']
          state=request.form['state']
          city=request.form['city']
          address=request.form['address'] 
          skill=request.form['skill'] 
          charges=request.form['charges'] 
          exp=request.form['exp'] 
          photo=request.files['photo']
          password=request.form['password']
           
          #------------validation-------
          datalist =[firstName,lastName,email,mobile,address,skill,state,city,charges,exp,photo,password]
          if(empty(datalist)):
               flash('Field cannot be empty !!')
               return redirect(url_for("provider_signup"))
          if(checkdigit(mobile))  :
               flash("must  be number")
               return redirect(url_for('provider_signup'))
          if(checkalpha(firstName) or checkalpha(lastName)):
               flash("Number must be alphabet")
               return redirect(url_for('provider_signup'))
               
  
   #-----------------uplode photo-------
          p = photo.filename #retrive photo name with extention
          d = datetime.now() # current data time (import datatime)
          t = int(round(d.timestamp()))  #timestamp will conver time in plane digit ex 12/06/2002= 12062002
          path =str(t)+'.'+ p.split('.')[-1]
          photo.save("static/provider/"+path) #create provider folder insidide side 
   
   #-------------------------------------
          password=eObj.convert(password) # encription

          providerObj.provider_signup(firstName,lastName,email,mobile,address,skill,state,city,charges,exp,path,password)
          flash('Register sucessful. login Now!!')
          return redirect(url_for('provider_login'))
     
@app.route('/provider_login', methods=['POST','GET'])
def  provider_login():
     if request.method == 'GET':
        return render_template('provider_login.html')
     else:
          email=request.form['email']
          password=request.form['password']
          # validation
          datalist =[email,password]
          if(empty(datalist)):
               flash('Field cannot be empty !!')
               return redirect(url_for("provider_login"))
          password=eObj.convert(password) #encription

          status =providerObj.provider_login(email,password)
          if(status==0):
               flash("invalid email and password")
               return redirect(url_for('provider_login'))
          else:
               return redirect(url_for('provider_dashboard'))    

@app.route('/provider_dashboard', methods=['POST','GET'])
def provider_dashboard():
     if 'providerEmail' in session:
          if request.method == 'GET':
               return render_template('provider_dashboard.html')
     else:
          flash('to access this page login first')  
          return redirect(url_for('provider_login'))  
              
# @app.route('/provider_profile', methods=['POST','GET'])
# def provider_profile():
#      if 'email' in session:
#           if request.method == 'GET':
#                return render_template('provider_profile.html')
#      else:
#           flash('to access this page login first')  
#           return redirect(url_for('provider_login'))  

@app.route('/provider_profile',methods=['POST','GET'])
def provider_profile():
     if 'providerEmail' in session:
          if request.method=='GET':
               record=providerObj.provider_profile()
               return render_template('provider_profile.html',record=record)     
          else:
               firstName =request.form['firstName']
               lastName =request.form['lastName']
               mobile =request.form['mobile']
               address=request.form['address'] 
               skill=request.form['skill'] 
               charges=request.form['charges'] 
               exp=request.form['exp'] 
          # ---validation
               datalist =[firstName,lastName,mobile,address,skill,charges,exp]
               if(empty(datalist)):
                    flash('Field cannot be empty !!')
                    return redirect(url_for("provider_profile"))
          
               if(empty(mobile)):
                    flash('mobile cannot be empty !!')
                    return redirect(url_for("provider_profile"))
          
               if(checkalpha(firstName) or checkalpha(lastName)):
                    flash('must be alphabet !!')
                    return redirect(url_for("provider_profile"))
#   -------------and update
               providerObj.provider_login_update(firstName,lastName,mobile,address,skill,charges,exp) 
               flash('profile update successfully')
               return redirect(url_for('provider_profile'))
     else:
          flash('to access this page login first')  
          return redirect(url_for('provider_login'))

@app.route('/provider_logout')
def provider_logout():
     if 'providerEmail' in session:
          session.clear()
          flash('successfully logout !!')
          return redirect(url_for('provider_login'))
     else:
          flash('to access this page login first')  
          return redirect(url_for('provider_login'))
     




@app.route('/provider_password_change',methods=['POST','GET'])
def provider_password_change():
     if 'providerEmail' in session:
          if request.method=='GET':
               return render_template('provider_password_change.html')
          else:
               oldpassword= request.form['oldpassword']
               newpassword= request.form['newpassword']
               # Validation
               dataList=[oldpassword,newpassword]
               if(empty(dataList)):
                    flash('fleld cannot be empty')
                    return redirect(url_for('provider_password_change'))
               if(newpassword == oldpassword): #check both are same
                    flash("old password and new password canno't be same")
                    return redirect(url_for("provider_password_change"))

               oldpassword=eObj.convert(oldpassword) # encription
               newpassword=eObj.convert(newpassword) # encription
               status=providerObj.checkpassword(oldpassword)
               if(status):
                    providerObj.provider_password_change(newpassword)
                    session.clear()
                    flash('password change sucessfully .. login now')
                    return redirect(url_for('provider_login'))
               else:
                    flash('your old password invalid.. tr again!')
                    return redirect(url_for('provider_password_change'))
     else:
          flash('to access this page login first')  
          return redirect(url_for('provider_login'))     
     


@app.route('/provider_delete' ,methods =['POST','GET'])
def provier_delete():
      if 'providerEmail' in session:
          if request.method == 'GET':
               providerObj.provider_delete()
               session.clear()
               flash('Account delete sucessfully! see you soon ')
               return redirect(url_for('provider_signup'))
      else:
          flash('to access this page login first')  
          return redirect(url_for('provider_login'))
         
@app.route('/pBooking_history',methods=['POST','GET'])
def pBooking_history():
    if 'providerEmail' in session:    
        if request.method=='GET':
            record=providerObj.pBooking_history()
            return render_template('pBooking_history.html',record=record)
    else:
        flash("to access this page please login now!!")
        return redirect(url_for('provider_login'))
    
@app.route('/provider_review',methods=['POST','GET'])
def provider_review():
    if 'providerEmail' in session:    
        if request.method=='GET':
            record=providerObj.provider_review()
            return render_template('provider_review.html',record=record)
    else:
        flash("to access this page please login now!!")
        return redirect(url_for('provider_login'))  






#----------------------------------------------------------------------------

if __name__ == '__main__':
     #app.run(debug = True ) # 127.0.0.1.5000
     app.run(host='0.0.0.0',port='5001',debug= True) #activate server


