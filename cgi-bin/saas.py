#!/usr/bin/python

import os,sys,time,socket,commands,cgitb,cgi,Cookie
import mysql.connector as mariadb
#for debugging
cgitb.enable()
#headers
print "Content-type:text/html\r\n\r\n"
##to fetch whole data from html page
data=cgi.FieldStorage()
#to get software selection
service=data.getvalue('service')
#database connectivity
mariadb_connection=mariadb.connect(user="root",password="123",database="cloud")
cursor=mariadb_connection.cursor()
#retrieving cookies
try:
	C= Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	usr=C["user"].value
	#to check cookie with database
	cursor.execute("SELECT uname FROM login WHERE uname=%s",(usr,))
	#maintain a list of output of above query
	logincheck1 = cursor.fetchone()
	if logincheck1 is None :
		print '<script>alert("Session expired!! please login again and if problem persists then enable cookies in your browser.")</script>'
		print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/index.html' />"
	else:
		if service=='Firefox Web Browser':
			entry="#!/usr/bin/python\nimport os\nos.system('ssh -X "+usr+"@192.168.122.223 firefox')"		
			commands.getstatusoutput('sudo touch /var/www/html/firefox.sh')
			commands.getstatusoutput('sudo chmod 777 /var/www/html/firefox.sh')
			f=open('/var/www/html/firefox.sh','w')
			f.write(entry)
			f.close()
			commands.getstatusoutput('sudo tar -cvf /var/www/html/firefox.tar.gz /var/www/html/firefox.sh')
			commands.getstatusoutput('sudo chmod 555 /var/www/html/firefox.tar.gz')
			print "<META name='viewport' HTTP-EQUIV='refresh' width=device-width initial-scale=1.0 content='0 url=/firefox.tar.gz' />"
		elif service=='VLC Media Player':
			entry="#!/usr/bin/python\nimport os\nos.system('ssh -X "+usr+"@192.168.122.223 vlc')"		
			commands.getstatusoutput('sudo touch /var/www/html/vlc.sh')
			commands.getstatusoutput('sudo chmod 777 /var/www/html/vlc.sh')
			f=open('/var/www/html/vlc.sh','w')
			f.write(entry)
			f.close()
			commands.getstatusoutput('sudo tar -cvf /var/www/html/vlc.tar.gz /var/www/html/vlc.sh')
			commands.getstatusoutput('sudo chmod 555 /var/www/html/vlc.tar.gz')
			print "<META name='viewport' HTTP-EQUIV='refresh' width=device-width initial-scale=1.0 content='0 url=/vlc.tar.gz' />"
		elif service=='Calculator':
			entry="#!/usr/bin/python\nimport os\nos.system('ssh -X "+usr+"@192.168.122.223 gnome-calculator')"		
			commands.getstatusoutput('sudo touch /var/www/html/cal.sh')
			commands.getstatusoutput('sudo chmod 777 /var/www/html/cal.sh')
			f=open('/var/www/html/cal.sh','w')
			f.write(entry)
			f.close()
			commands.getstatusoutput('sudo tar -cvf /var/www/html/cal.tar.gz /var/www/html/cal.sh')
			commands.getstatusoutput('sudo chmod 555 /var/www/html/cal.tar.gz')
			print "<META name='viewport' HTTP-EQUIV='refresh' width=device-width initial-scale=1.0 content='0 url=/cal.tar.gz' />"
		elif service=='Gedit Text Editor':
			entry="#!/usr/bin/python\nimport os\nos.system('ssh -X "+usr+"@192.168.122.223 gedit')"		
			commands.getstatusoutput('sudo touch /var/www/html/gedit.sh')
			commands.getstatusoutput('sudo chmod 777 /var/www/html/gedit.sh')
			f=open('/var/www/html/gedit.sh','w')
			f.write(entry)
			f.close()
			commands.getstatusoutput('sudo tar -cvf /var/www/html/gedit.tar.gz /var/www/html/gedit.sh')
			commands.getstatusoutput('sudo chmod 555 /var/www/html/gedit.tar.gz')
			print "<META name='viewport' HTTP-EQUIV='refresh' width=device-width initial-scale=1.0 content='0 url=/gedit.tar.gz' />"
		elif service=='Openoffice':
			entry="#!/usr/bin/python\nimport os\nos.system('ssh -X "+usr+"@192.168.122.223 libreoffice4.3 ')"		
			commands.getstatusoutput('sudo touch /var/www/html/open.sh')
			commands.getstatusoutput('sudo chmod 777 /var/www/html/open.sh')
			f=open('/var/www/html/open.sh','w')
			f.write(entry)
			f.close()
			commands.getstatusoutput('sudo tar -cvf /var/www/html/open.tar.gz /var/www/html/open.sh')
			commands.getstatusoutput('sudo chmod 555 /var/www/html/open.tar.gz')
			print "<META name='viewport' HTTP-EQUIV='refresh' width=device-width initial-scale=1.0 content='0 url=/open.tar.gz' />"
		elif service=='Webcam':
			entry="#!/usr/bin/python\nimport os\nos.system('ssh -X "+usr+"@192.168.122.223 cheese')"		
			commands.getstatusoutput('sudo touch /var/www/html/cam.sh')
			commands.getstatusoutput('sudo chmod 777 /var/www/html/cam.sh')
			f=open('/var/www/html/cam.sh','w')
			f.write(entry)
			f.close()
			commands.getstatusoutput('sudo tar -cvf /var/www/html/cam.tar.gz /var/www/html/cam.sh')
			commands.getstatusoutput('sudo chmod 555 /var/www/html/cam.tar.gz')
			print "<META name='viewport' HTTP-EQUIV='refresh' width=device-width initial-scale=1.0 content='0 url=/cam.tar.gz' />"
		elif service=='Screenshot':
			entry="#!/usr/bin/python\nimport os\nos.system('ssh -X "+usr+"@192.168.122.223 gnome-screenshot -a')"		
			commands.getstatusoutput('sudo touch /var/www/html/screenshot.sh')
			commands.getstatusoutput('sudo chmod 777 /var/www/html/screenshot.sh')
			f=open('/var/www/html/screenshot.sh','w')
			f.write(entry)
			f.close()
			commands.getstatusoutput('sudo tar -cvf /var/www/html/screenshot.tar.gz /var/www/html/screenshot.sh')
			commands.getstatusoutput('sudo chmod 555 /var/www/html/screenshot.tar.gz')
			print "<META name='viewport' HTTP-EQUIV='refresh' width=device-width initial-scale=1.0 content='0 url=/screenshot.tar.gz' />"
except (Cookie.CookieError, KeyError):
	print '<script>alert("Some problem occured!! please login again")</script>'
	print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/index.html' />"

