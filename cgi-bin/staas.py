#!/usr/bin/python

import os,sys,time,socket,commands,cgitb,cgi
#for debugging
cgitb.enable()
print "Content-type:text/html\r\n\r\n"
#to fetch whole data from html page
data=cgi.FieldStorage()
#to get radio button selection
option=data.getvalue('option')
#to get block button selection
block=data.getvalue('block')
#to get further button selection
opt=data.getvalue('opt')

if block=='Click Here For Block Storage':
	print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/block.html' />"
elif option=='object':
	if opt=='Click here for new drive.':
		print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/objectnew.html' />"
	elif opt=='Click here to extend existing one.':
		print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/objectextend.html' />"
