# install - pip install mysql-connector-python
from flask import session

import mysql.connector as sql

class UserOperation:
    def connect(self):
        con= sql.connect(host='127.0.0.1',port='3306',user='root',password='root',database='b6_full_stack')
        return con 
    
    def user_signup(self,firstName,lastName,email,mobile,state,city,password):
        con = self.connect()
        cursor = con.cursor()
        sq="insert into user(firstName,lastName,email,mobile,state,city,password) value(%s,%s,%s,%s,%s,%s,%s)"

        record = [firstName,lastName,email,mobile,state,city,password]

        cursor.execute(sq,record)
        con.commit()
        con.close()
    def user_login(self,email,password)    :
        con =self.connect()
        cursor= con.cursor()
        sq="select firstName from user where email=%s and password=%s"
        record=[email,password]
        cursor.execute(sq,record)
        row=cursor.fetchall()
        con.close()
        if(row):
            session['firstName']=row[0][0]
            session['userEmail']=email
            return 1
        else:
            return 0

    def user_profile(self):
        con = self.connect()
        cursor = con.cursor()
        sq = "select firstName,lastName,mobile,email,state,city from user where email=%s"
        record=[session['userEmail']]
        cursor.execute(sq,record)
        row=cursor.fetchall()
        con.close()
        return row

    def user_login_update(self,firstName,lastName,mobile) :
        con = self.connect()
        cursor = con.cursor()
        sq="update user set firstName = %s , lastName=%s, mobile=%s where email= %s"

        record = [firstName,lastName,mobile,session['userEmail']]

        cursor.execute(sq,record)
        con.commit()
        con.close()
        return

    def user_delete(self)  :
        con = self.connect()
        cursor = con.cursor()
        sq="delete from user where email =%s"

        record = [session['userEmail']]

        cursor.execute(sq,record)
        con.commit()
        con.close()
        return
    
    def checkpassword(self,oldpassword):
        con = self.connect()
        cursor = con.cursor()
        sq = "select * from user where email=%s and password =%s"
        record=[session['userEmail'],oldpassword]
        cursor.execute(sq,record)
        row=cursor.fetchall()
        con.close()
        if(row):
            return True
        else:
            return False
    def user_password_change(self,newpassword)  :
        con = self.connect()
        cursor = con.cursor()
        sq = "update user set password =%s where email=%s"
        record=[ newpassword ,session['userEmail']]
        cursor.execute(sq,record)
        con.commit()
        con.close()
        return
    
    
    def user_service(self)  :
        con = self.connect()
        cursor = con.cursor()
        sq = "select distinct(skill) from provider p, user u where p.city=u.city and u.email=%s"
        record=[session['userEmail']]
        cursor.execute(sq,record)
        row = cursor.fetchall()
        con.close()
        return row
    
    def user_service_search(self,skill)  :
        con = self.connect()
        cursor = con.cursor()
        sq = "select photo, p.firstName ,p.mobile,exp,charges,p.email from provider p,user u where p.city=u.city and skill=%s and u.email=%s"
        record=[skill,session['userEmail']]
        cursor.execute(sq,record)
        row = cursor.fetchall()
        con.close()
        return row
    
    def user_service_city(self)  :
        con = self.connect()
        cursor = con.cursor()
        sq = "select distinct(skill) from provider"
        cursor.execute(sq)
        row = cursor.fetchall()
        con.close()
        return row  
    
    def user_service_city_search(self,skill,city)  :
        con = self.connect()
        cursor = con.cursor()
        sq = "select photo, firstName,mobile,exp,charges,email from provider where skill=%s and city=%s"
        record=[skill,city]
        cursor.execute(sq,record)
        row = cursor.fetchall()
        con.close()
        return row

    def user_service_view(self, providerEmail):
        con = self.connect()
        cursor = con.cursor()
        sq = "select firstName,lastName, email, mobile,state,city,address,skill,exp,charges,photo from provider where email=%s"
        record=[providerEmail]
        cursor.execute(sq,record)
        row= cursor.fetchall()
        con.close()
        return row
    
    def booking(self,providerEmail,pid,bookingDate,charges):
        con = self.connect()
        cursor = con.cursor()
        sq = "insert into booking(userEmail,providerEmail,paymentID,bookingDate,amount) values(%s,%s,%s,%s,%s)"
        record=[session['userEmail'],providerEmail,pid, bookingDate,charges]
        cursor.execute(sq,record)
        con.commit()
        con.close()
        return
    
    def user_booking_history(self):
        con = self.connect()
        cursor = con.cursor()
        sq = "select skill ,firstName,mobile,bookingDate ,amount  from booking b,provider p where b.userEmail=%s and b.providerEmail=p.email"
        record=[session['userEmail']] 
        cursor.execute(sq,record)
        row = cursor.fetchall()
        con.close()
        return row
    
    def user_review(self,providerEmail, star, comment):
        con = self.connect()
        cursor = con.cursor()
        sq = "insert into review(userEmail,providerEmail,star,comment) values(%s,%s,%s,%s)"
        record=[session['userEmail'],providerEmail,star,comment] 
        cursor.execute(sq,record)
        con.commit()
        con.close()
        return  
    
    def user_review_show(self,providerEmail):
        con = self.connect()
        cursor = con.cursor()
        sq="select star,u.firstName,comment from review r,user u where u.email=r.userEmail and providerEmail=%s"
        record = [providerEmail]
        cursor.execute(sq,record)
        row=cursor.fetchall()
        con.close()
        return row 
    
    def user_getStar(self,providerEmail):
        con = self.connect()
        cursor = con.cursor()
        sq = "select floor(avg(star)) from review r,provider p where p.email=r.providerEmail and r.providerEmail=%s "
        record=[providerEmail]
        cursor.execute(sq,record)
        row = cursor.fetchall()
        con.close()
        return row[0][0]

 
   

#------------------provider_______------------------------------------------
    # def provider_signup(self,providerID,firstName,lastName,email,mobile,Address,skill,state,city,charges,experiance,password):
    #     con = self.connect()
    #     cursor = con.cursor()
    #     sq="insert into provider(providerID,firstName,lastName,email,mobile,Address,skill,state,city,charges,experiance,password) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    #     record = [providerID,firstName,lastName,email,mobile,Address,skill,state,city,charges,experiance,password]

    #     cursor.execute(sq,record)
    #     con.commit()
    #     con.close()

    # def provider_login(self,providerID,password)    :
    #     con =self.connect()
    #     cursor= con.cursor()
    #     sq="select firstName from provider where providerID=%s and password=%s"
    #     record=[providerID,password]
    #     cursor.execute(sq,record)
    #     row=cursor.fetchall()
    #     con.close()
    #     if(row):
    #         session['firstName']=row[0][1]
    #         session['providerID']=providerID
    #         return 1
    #     else:
    #         return 0
     