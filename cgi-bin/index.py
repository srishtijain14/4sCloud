#!/usr/bin/python
import Cookie,os,sys,time,socket,commands,cgitb,cgi
#for database connectivity
import mysql.connector as mariadb
#for debugging
cgitb.enable()

#headers
print "Content-type:text/html"

#to fetch data from html page
data=cgi.FieldStorage()
#for username
u_name=data.getvalue('uname')
#for password
pswd=data.getvalue('pwd')

#database connectivity
mariadb_connection=mariadb.connect(user="root",password="123",database="cloud")
cursor=mariadb_connection.cursor()
#to check input with database
cursor.execute("SELECT uname,pswd FROM login WHERE uname=%s && pswd=%s",(u_name,pswd))
#maintain a list of output of above query
logincheck1 = cursor.fetchone()

if logincheck1 is None :
	print ""
	print '<script>alert("Invalid login!!")</script>'
	print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/index.html' />"
else:
	
	C = Cookie.SimpleCookie()
	C["user"] = u_name
	print C
	print ""
	print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/services.html' />"

