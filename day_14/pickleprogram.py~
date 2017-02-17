import pickle
import sys
import os
import re
sys1=sys.argv[1]
sys2=sys.argv[2]
username="asm"  
password="asm123"
i=1
list1=[]
 
if((username==sys1)&(password==sys2)):
	
	while True:
		data=raw_input("mysql>")
		data2=raw_input()
		str1=data+data2
		if str1:
			reg1=re.search(r'(create database.*)',str1,re.I|re.M)
			if reg1:
				dbname=str(reg1.group())
				#print dbname
				l2=dbname.split()
				#print l2	
				#databasename=str(l2[2])
				databasename=str(l2)
				databasename=databasename.strip(';')
				print "table name is",databasename
				newpath = r'/home/Documents/python_training/day_13' 
				if not os.path.exists(newpath):
    					os.makedirs(newpath)
					print "folder created"
				
			reg2=re.search(r'(create table.*)',str1,re.I|re.M)
			if reg2:
				f=open("/home/Documents/python_training/day_13/table.txt",'w')
				print "table created"
			reg3=re.search(r'(insert the values.*)',str1,re.I|re.M)
			if reg3:
				f=open("/home/Documents/python_training/day_13/table.txt",'w')
				inp=input("enter the number of elements you want to insert")
				for i in range(inp):
					data=raw_input("enter the data")
					list1.append(data)
					print list1
				pickle.dump(list1,f)
				f.close()
			reg4=re.match('select',str1,re.I|re.M)
			if reg4:
				f=open("/home/Documents/python_training/day_13/table.txt",'r')
				list1 = pickle.load(f)
				print list1
				f.close()
else:
	print "authorization failed"
			


		
