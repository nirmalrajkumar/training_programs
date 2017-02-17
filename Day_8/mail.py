import sys
import smtplib
import getpass 
host = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(host,port)
server.ehlo()
server.starttls()
server.ehlo()
v1 = sys.argv[1]
v2 = sys.argv[2]
v3 = sys.argv[3]
username = raw_input("gmail user name:")
password = getpass.getpass()
server.login(username,password)
to = v1
sub = v2
mes = v3
with open(mes,'r')as f:
	f1=f.read()
	message= "subjuct: %s\n\n%s"%(sub,f1)
	server.sendmail(username,to,message)




