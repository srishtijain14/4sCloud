#!/usr/bin/python
import Cookie,os,sys,time,socket,commands,cgitb,cgi
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
#d_size_value for drive size value
d_size_value=data.getvalue('dsize')
#d_size for drive size
d_size=data.getvalue('size')

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
		if d_size_value!=None and d_name!=None:
			#creating thin logical volume from vgpool
			lv_c,lv_o=commands.getstatusoutput('sudo lvcreate -V'+d_size_value+d_size+' --name '+d_name+' --thin myvg/pool1')
			if(lv_c==0):
				#formatting 
				commands.getstatusoutput('sudo mkfs.ext4 /dev/myvg/'+d_name)
				#creating mount point
				commands.getstatusoutput('sudo mkdir /mnt/'+d_name)
				#local mount
				commands.getstatusoutput('sudo mount /dev/myvg/'+d_name+' /mnt/'+d_name)
				#giving permission to directory
				commands.getstatusoutput('sudo chmod 777 /mnt/'+d_name)
				#installing nfs-utils
				smb_c,smb_o=commands.getstatusoutput('sudo rpm -q samba')
				if smb_c!=0:
					commands.getstatusoutput('sudo yum install samba* -y')
				#entry in smb.conf file
				entry='\n['+d_name+']\npath=/mnt/'+d_name+'\nwritable=yes\nhosts allow=192.168.\nvalid users='+usr+'\ncreate mask=777\ndirectory mask=777'
				#giving conf file write permission
				commands.getstatusoutput('sudo chmod 777 /etc/samba/smb.conf')
				#appending this to end of /etc/samba/smb.conf file
				f=open('/etc/samba/smb.conf','a')
				f.write(entry)
				f.write('\n\n')
				f.close()
				#starting samba service and service persistant
				ser_c,ser_o=commands.getstatusoutput('sudo systemctl reload smb')
				test_c,test_o=commands.getstatusoutput('sudo testparm')
				if ser_c==0 and test_c==0:
					entry1='yum install samba* cifs* -y\nsystemctl start smb\nmkdir /mnt/'+d_name+'\nchmod 777 /mnt/'+d_name+'\nmount -vo username='+usr+' //192.168.122.223/'+d_name+' /mnt/'+d_name+'\n\n'		
					commands.getstatusoutput('sudo touch /var/www/html/'+d_name+usr+'obj.sh')
					commands.getstatusoutput('sudo chmod 777 /var/www/html/'+d_name+usr+'obj.sh')
					f=open('/var/www/html/'+d_name+usr+'obj.sh','w')
					f.write(entry1)
					f.close()
					commands.getstatusoutput('sudo tar -cvf /var/www/html/'+d_name+usr+'obj.tar.gz /var/www/html/'+d_name+usr+'obj.sh')
					commands.getstatusoutput('sudo chmod 555 /var/www/html/'+d_name+usr+'obj.tar.gz')
					#to insert value into database
					cursor.execute("INSERT INTO object(id,uname,drive) VALUES(0,%s,%s)",(usr,d_name))
					#to save changes in database
					mariadb_connection.commit()
					mariadb_connection.close()
					print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/"+d_name+usr+"obj.tar.gz' />"
			else :
				print '<script>alert("Drive name already in use.Please enter a new drive name and drive size as integer value.")</script>'
				print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/objectnew.html' />"
		else:
			print '<script>alert("Please enter a new drive name and drive size as integer value.")</script>'
			print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/objectnew.html' />"
except (Cookie.CookieError, KeyError):
	print '<script>alert("Session expired!! please login again and if problem persists then enable cookies in your browser.")</script>'
	print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/index.html' />"

