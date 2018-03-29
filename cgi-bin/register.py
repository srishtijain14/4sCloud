#!/usr/bin/python

import os,sys,time,socket,commands,cgitb,cgi,crypt
#package for database connectivity
import mysql.connector as mariadb
#for debugging
cgitb.enable()
print "Content-type:text/html\r\n\r\n"
#to fetch value from html page
data=cgi.FieldStorage()
#for First Name
fname=data.getvalue('fname')
#for last name
lname=data.getvalue('lname')
#for username
uname=data.getvalue('uname')
#for email
email=data.getvalue('email')
#for password
pwd=data.getvalue('pwd')
#encrypting password
#enc_pwd=crypt.crypt(pwd,"22")
#adding user at server
usr_c,usr_o=commands.getstatusoutput('sudo adduser '+uname)
#having pwd as password
pwd_c,pwd_o=commands.getstatusoutput('echo '+pwd+' | sudo passwd '+uname+' --stdin')
#having pwd as samba password
smb_c,smb_o=commands.getstatusoutput('(echo '+pwd+'; echo '+pwd+') | sudo smbpasswd -a '+uname)
if usr_c==0 and pwd_c==0 and smb_c==0:
	#try except for error handling
	try:
		#database connectivity
		mariadb_connection=mariadb.connect(user="root",password="123",database="cloud")
		cursor=mariadb_connection.cursor()
		#to insert value into database
		cursor.execute("INSERT INTO login(id,fname,lname,uname,email,pswd,smbpswd) VALUES(0,%s,%s,%s,%s,%s,%s)",(fname,lname,uname,email,pwd,pwd))
		#to save changes in database
		mariadb_connection.commit()
		mariadb_connection.close()
		print "<META name='viewport' HTTP-EQUIV='refresh' content='2 url=/index.html' />"
	except:
		#if error occurs then rollback
		print "error"
		mariadb_connection.rollback()
else:
	print '<script>alert("username already exits!") </script>'
