#!/usr/bin/python
import os,sys,time,socket,commands,cgitb,cgi,Cookie
#for database connectivity
import mysql.connector as mariadb
#for debugging
cgitb.enable()
#headers
print "Content-type:text/html\r\n\r\n"
#to fetch whole data from html page
data=cgi.FieldStorage()
#d_name for drive name
d_name=data.getvalue('dname')
#d_size for drive size value
d_size_value=data.getvalue('dsize')
#d_size for drive size
d_size=data.getvalue('size')

#database connectivity
mariadb_connection=mariadb.connect(user="root",password="123",database="cloud")
cursor=mariadb_connection.cursor()

#retrieving cookies
try:
	C= Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	usr=C["user"].value
	#to check cookie with database
	a=cursor.execute("SELECT * FROM object WHERE uname='{}' and drive='{}'".format(usr,d_name))
	#maintain a list of output of above query
	user_check = cursor.fetchone()
	if user_check is None:
		print '<script>alert("Session Expired!!please login again and if problem persist then enable cookies in your browser.")</script>'
		print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/index.html' />"
	else:
		#to check username and corresponding drive name existence
		cursor.execute("SELECT * FROM object WHERE uname='{}' and drive='{}'".format(usr,d_name))
		#maintain a list of output of above query
		user_drive_check = cursor.fetchone()
		if user_drive_check is None :
			print '<script>alert("Drive name does not exist.Please enter a valid drive name")</script>'
			print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/objectextend.html' />"
		else:
			if d_size_value!=None and d_name!=None:
				#extending storage
				ext_c,ext_o=commands.getstatusoutput('sudo lvextend --size +'+d_size_value+d_size+' /dev/myvg/'+d_name)
				if ext_c==0:
					#formatting extended part
					format_c,format_o=commands.getstatusoutput('sudo resize2fs /dev/myvg/'+d_name)
					print '<script>alert("Extension Done!!.")</script>'
				else:
					print '<script>alert("Please enter correct drive name and drive size as integer value.")</script>'
					print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/objectextend.html' />"
			else:
				print '<script>alert("Please enter correct drive name and drive size as integer value.")</script>'
				print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/objectextend.html' />"
except (Cookie.CookieError, KeyError):
	print '<script>alert("Session expired!! please login again and if problem persists then enable cookies in your browser.")</script>'
	print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/index.html' />"
