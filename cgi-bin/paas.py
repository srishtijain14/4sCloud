#!/usr/bin/python

import os,sys,time,socket,commands,cgitb,cgi

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

data=cgi.FieldStorage()
submit=data.getvalue('submit')

if submit=='Python':
	commands.getstatusoutput('sudo docker start a9f26a624d36')
	commands.getstatusoutput('sudo docker exec -it a9f26a624d36 bash')
	commands.getstatusoutput('sudo systemctl restart shellinaboxd')
	print '<a style="font-size:30px;color:green;" href="https://192.168.122.223:4201"> Enter <i><b>pycode</i></b> as username as well as password to login</a>'
elif submit=='Ruby':
	commands.getstatusoutput('sudo docker start a9f26a624d36')
	commands.getstatusoutput('sudo docker exec -it a9f26a624d36 bash')
	commands.getstatusoutput('sudo systemctl restart shellinaboxd')
	print '<a style="font-size:30px;color:green;" href="https://192.168.122.223:4201"> Enter <i><b>ruby</i></b> as username as well as password to login</a>'
elif submit=='Perl':
	commands.getstatusoutput('sudo docker start a9f26a624d36')
	commands.getstatusoutput('sudo docker exec -it a9f26a624d36 bash')
	commands.getstatusoutput('sudo systemctl restart shellinaboxd')
	print '<a style="font-size:30px;color:green;" href="https://192.168.122.223:4201"> Enter <i><b>perl</i></b> as username as well as password to login</a>'
elif submit=='C':
	commands.getstatusoutput('sudo docker start a9f26a624d36')
	commands.getstatusoutput('sudo docker exec -it a9f26a624d36 bash')
	commands.getstatusoutput('sudo systemctl restart shellinaboxd')
	print '<a style="font-size:30px;color:green;" href="https://192.168.122.223:4201"> Enter <i><b>c</i></b> as username as well as password to login</a>'
elif submit=='C++':
	commands.getstatusoutput('sudo docker start a9f26a624d36')
	commands.getstatusoutput('sudo docker exec -it a9f26a624d36 bash')
	commands.getstatusoutput('sudo systemctl restart shellinaboxd')
	print '<a style="font-size:30px;color:green;" href="https://192.168.122.223:4201"> Enter <i><b>ccode</i></b> as username as well as password to login</a>'
elif submit=='Java':
	commands.getstatusoutput('sudo docker start a9f26a624d36')
	commands.getstatusoutput('sudo docker exec -it a9f26a624d36 bash')
	commands.getstatusoutput('sudo systemctl restart shellinaboxd')
	print '<a style="font-size:30px;color:green;" href="https://192.168.122.223:4201"> Enter <i><b>java</i></b> as username as well as password to login</a>'

