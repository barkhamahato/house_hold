# install - pip install mysql-connector-python
from flask import session

import mysql.connector as sql

class ProviderOperation:
    def connect(self):
        con= sql.connect(host='127.0.0.1',port='3306',user='root',password='root',database='b6_full_stack')
        return con 
    
   
#------------------provider_______------------------------------------------
    def provider_signup(self,firstName,lastName,email,mobile,address,skill,state,city,charges,exp,photo,password):
        con = self.connect()
        cursor = con.cursor()
        sq="insert into provider(firstName,lastName,email,mobile,address,skill,state,city,charges,exp,photo,password) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        record = [firstName,lastName,email,mobile,address,skill,state,city,charges,exp,photo,password]

        cursor.execute(sq,record)
        con.commit()
        con.close()

    def provider_login(self,email,password)    :
        con =self.connect()
        cursor= con.cursor()
        sq="select firstName from provider where email=%s and password=%s"
        record=[email,password]
        cursor.execute(sq,record)
        row=cursor.fetchall()
        con.close()
        if(row):
            session['providerEmail']=email
            session['firstName']=row[0][0]
            
            return 1
        else:
            return 0
     
    def provider_profile(self):
        con = self.connect()
        cursor = con.cursor()
        sq = "select firstName,lastName,email,mobile,Address,skill,charges,exp from provider where email=%s"
        record=[session['providerEmail']]
        cursor.execute(sq,record)
        row=cursor.fetchall()
        con.close()
        return row  
    
    def provider_login_update(self,firstName,lastName,mobile,skill,address,charges,exp) :
        con = self.connect()
        cursor = con.cursor()
        sq="update provider set firstName = %s , lastName=%s, mobile=%s ,address=%s ,skill= %s, charges=%s ,exp=%s where email= %s"

        record = [firstName,lastName,mobile,address,skill,charges,exp,session['providerEmail']]

        cursor.execute(sq,record)
        con.commit()
        con.close()
        return
    
    def checkpassword(self,oldpassword):
        con = self.connect()
        cursor = con.cursor()
        sq = "select * from provider where email=%s and password =%s"
        record=[session['providerEmail'],oldpassword]
        cursor.execute(sq,record)
        row=cursor.fetchall()
        con.close()
        if(row):
            return True
        else:
            return False
        
    def provider_password_change(self,newpassword)  :
        con = self.connect()
        cursor = con.cursor()
        sq = "update provider set password =%s where email=%s"
        record=[ newpassword ,session['providerEmail']]
        cursor.execute(sq,record)
        con.commit()
        con.close()
        return
    
    def provider_delete(self)  :
        con = self.connect()
        cursor = con.cursor()
        sq="delete from provider where email =%s"

        record = [session['providerEmail']]

        cursor.execute(sq,record)
        con.commit()
        con.close()
        return
    
    def pBooking_history(self):
        con = self.connect()
        cursor = con.cursor()
        sq = "select firstName,userEmail,city,mobile,bookingDate,amount from booking b,user u where b.providerEmail=%s and b.userEmail=u.email "
        record=[session['providerEmail']]
        cursor.execute(sq,record)
        row=cursor.fetchall()
        con.close()
        return row 

    def provider_review(self):
        con = self.connect()
        cursor = con.cursor()
        sq = "select u.firstName,star,comment from review r, user u  where u.email = r.userEmail and providerEmail=%s  "
        record=[session['providerEmail']]
        cursor.execute(sq,record)
        row=cursor.fetchall()
        con.close()
        return row 
    
   