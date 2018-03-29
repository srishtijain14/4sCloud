#!/usr/bin/python

import os,sys,time,socket,commands,cgitb,cgi
#for debugging
cgitb.enable()
print "Content-type:text/html\r\n\r\n"
#to fetch data from html page
data=cgi.FieldStorage()
#to retrieve selection of button
button=data.getvalue('button')

if button=="saas":
	print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/saas.html' />"
elif button=="staas":
	print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/staas.html' />"
elif button=="iaas":
	print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/iaas.html' />"
elif button=="paas":
	print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/paas.html' />"
