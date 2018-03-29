#!/usr/bin/python

import os,sys,time,socket,commands,cgitb,cgi,Cookie
#for database connectivity
import mysql.connector as mariadb
#for debugging
cgitb.enable()
print "Content-type:text/html\r\n\r\n"

#to fetch whole data from html page
data=cgi.FieldStorage()
#d_name for drive name
d_name=data.getvalue('dname')
#d_size for drive size value
d_size_value=data.getvalue('dsize')
#d_size for drive size
d_size=data.getvalue('size')
#retrieving cookies
#database connectivity
mariadb_connection=mariadb.connect(user="root",password="123",database="cloud")
cursor=mariadb_connection.cursor()
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
		#creating thin logical volume from vgpool
		lv_c,lv_o=commands.getstatusoutput('sudo lvcreate -V'+d_size_value+d_size+' --name '+d_name+' --thin myvg/pool1')
		if(lv_c==0):
			#installing scsi-target-utils
			ser_c,ser_o=commands.getstatusoutput('sudo rpm -q scsi-target-utils')
			if ser_c!=0:
				commands.getstatusoutput('sudo yum install scsi-target-utils -y')
			#entry   
			entry="<target iqn.2017-07.com.example:"+d_name+">\n\tbacking-store /dev/myvg/"+d_name+"\n</target>"
			#giving permission
			commands.getstatusoutput('sudo chmod 222 /etc/tgt/targets.conf')
			#appending this into conf file  
			f=open('/etc/tgt/targets.conf','a')
			f.write(entry)
			f.write("\n")
			f.close()
			#restart service
			serv_c,serv_o=commands.getstatusoutput('sudo systemctl reload tgtd')
			if serv_c==0:
				entry1='yum install iscsi-initiator-utils -y\nsystemctl restart iscsi iscsid\niscsiadm --mode discovery --type sendtargets --portal 192.168.122.223\niscsiadm --mode node --targetname iqn.2017-07.com.example:'+d_name+' --portal 192.168.122.223:3260 --login\n\n'
				commands.getstatusoutput('sudo touch /var/www/html/'+d_name+usr+'block.sh')
				commands.getstatusoutput('sudo chmod 777 /var/www/html/'+d_name+usr+'block.sh')
				f=open('/var/www/html/'+d_name+usr+'block.sh','w')
				f.write(entry1)
				f.close()
				commands.getstatusoutput('sudo tar -cvf /var/www/html/'+d_name+usr+'block.tar.gz /var/www/html/'+d_name+usr+'block.sh')
				commands.getstatusoutput('sudo chmod 555 /var/www/html/'+d_name+usr+'block.tar.gz')
				#to insert value into database
				cursor.execute("INSERT INTO block(id,uname,blockdrive) VALUES(0,%s,%s)",(usr,d_name))
				#to save changes in database
				mariadb_connection.commit()
				mariadb_connection.close()
				print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/"+d_name+usr+"block.tar.gz' />"
		else :
			print '<script>alert("Drive name already in use.Please enter a new drive name and drive size as integer value.")</script>'
			print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/block.html' />"
except (Cookie.CookieError, KeyError):
	print '<script>alert("Session expired!! please login again and if problem persists then enable cookies in your browser.")</script>'
	print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/index.html' />"
