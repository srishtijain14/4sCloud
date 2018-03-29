#!/usr/bin/python

import os,sys,time,socket,commands,cgitb,cgi,random
#for debugging
cgitb.enable()
print "Content-type:text/html\r\n\r\n"

#to fetch whole data from html page
data=cgi.FieldStorage()
#osname for operating system name
osname=data.getvalue('os')
#osramfor operating system ram
osram=data.getvalue('ram')
#oscore for operating system cpu core
oscore=data.getvalue('core')
#oshdd for operating system hard drive
oshdd=data.getvalue('hdd')
#ospwd for operating system password
ospwd=data.getvalue('pwd')
#function for port no
def port():
	#port no to launch novnc in browser
	usr_port=str(random.randint(5900,6500))
	#port no for os with vnc 
	vnc_port=str(random.randint(6800,7500))
	return (usr_port,vnc_port)
#calling function 
fun_o=port()
#retrieving values
for i in fun_o:
	usr_port=fun_o[0]
	vnc_port=fun_o[1]
#checking availability of port no.
usr_c,usr_o=commands.getstatusoutput('sudo netstat -tanp | grep '+usr_port)
vnc_c,vnc_o=commands.getstatusoutput('sudo netstat -tanp | grep '+vnc_port)
if osname=='redhat7':
	if(usr_c !=0 and vnc_c!=0): 
		#image is created
		img_c,img_o=commands.getstatusoutput('sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhel7.1-3-1.qcow2 /var/lib/libvirt/images/'+osname+'.qcow2')
		#os is launched
		os_c,os_o=commands.getstatusoutput('sudo virt-install  --name '+osname+' --ram '+osram+' --vcpu '+oscore+' --disk path=/var/lib/libvirt/images/'+osname+'.qcow2 --import --graphics vnc,listen=192.168.122.1,port='+vnc_port+',password='+ospwd+' --noautoconsole')
		#for novnc
		vnc_c,vnc_o=commands.getstatusoutput('sudo websockify -D --web=/usr/share/novnc '+usr_port+' 192.168.122.1:'+vnc_port)
		if vnc_c==0:
			entry='firefox 192.168.122.1:'+usr_port
			commands.getstatusoutput('sudo touch /var/www/html/iaas.sh')
			commands.getstatusoutput('sudo chmod 777 /var/www/html/iaas.sh')
			f=open('/var/www/html/iaas.sh','w')
			f.write(entry)
			f.close()
			commands.getstatusoutput('sudo tar -cvf /var/www/html/iaas.tar.gz /var/www/html/iaas.sh')
			commands.getstatusoutput('sudo chmod 555 /var/www/html/iaas.tar.gz')
			print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/iaas.tar.gz' />"
	else:
		usr_port=port()

elif osname=='ubuntu':
	if(usr_c !=0 and vnc_c!=0):
		#live os ubuntu
		os_c,os_o=commands.getstatusoutput('sudo virt-install  --cdrom /ubuntu.iso --ram '+osram+' --vcpu '+oscore+' --nodisk  --name '+osname+' --graphics vnc,listen=192.168.122.1,port='+vnc_port+',password='+ospwd+' --noautoconsole')
		#for novnc
		vnc_c,vnc_o=commands.getstatusoutput('sudo websockify -D --web=/usr/share/novnc '+usr_port+' 192.168.122.1:'+vnc_port)
		if vnc_c==0:
			entry='firefox 192.168.122.1:'+usr_port
			commands.getstatusoutput('sudo touch /var/www/html/iaas.sh')
			commands.getstatusoutput('sudo chmod 777 /var/www/html/iaas.sh')
			f=open('/var/www/html/iaas.sh','w')
			f.write(entry)
			f.close()
			commands.getstatusoutput('sudo tar -cvf /var/www/html/iaas.tar.gz /var/www/html/iaas.sh')
			commands.getstatusoutput('sudo chmod 555 /var/www/html/iaas.tar.gz')
			print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/iaas.tar.gz' />"
	else:
		usr_port=port()

elif osname=='kali':
	if(usr_c !=0 and vnc_c!=0):
		#live os kali
		os_c,os_o=commands.getstatusoutput('sudo virt-install  --cdrom /kali.iso --ram '+osram+' --vcpu '+oscore+' --nodisk  --name '+osname+' --graphics vnc,listen=192.168.122.1,port='+vnc_port+',password='+ospwd+' --noautoconsole')
		#for novnc
		vnc_c,vnc_o=commands.getstatusoutput('sudo websockify -D --web=/usr/share/novnc '+usr_port+' 192.168.122.1:'+vnc_port)
		if vnc_c==0:
			entry='firefox 192.168.122.1:'+usr_port
			commands.getstatusoutput('sudo touch /var/www/html/iaas.sh')
			commands.getstatusoutput('sudo chmod 777 /var/www/html/iaas.sh')
			f=open('/var/www/html/iaas.sh','w')
			f.write(entry)
			f.close()
			commands.getstatusoutput('sudo tar -cvf /var/www/html/iaas.tar.gz /var/www/html/iaas.sh')
			commands.getstatusoutput('sudo chmod 555 /var/www/html/iaas.tar.gz')
			print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/iaas.tar.gz' />"
	else:
		usr_port=port()
else:
	print "<META name='viewport' HTTP-EQUIV='refresh' content='0 url=/iaas.html' />"
