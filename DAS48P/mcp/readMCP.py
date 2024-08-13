#!/usr/bin/python
'''
Exemple 'How to use the library MCP23017_I2C' - Rui Pedro Silva; Portugal; 03/2015
Connect a switch to GPB7 and led to GPA0. This program will make the LED turn on when you turn the switch.
'''
from MCP23017_I2C import *
import time
PORT = 48
i2cADDR=[0x20,0x21,0x22]
GP=['A','B']
log =[1]*48
GPIO_CHIP_DATA=[0]*len(i2cADDR)
for i in range(len(i2cADDR)):
	GPIO_CHIP_DATA[i]=GPIO_CHIP(i2cADDR[i],1)
for i in range(len(i2cADDR)):
	for j in GP:
		for k in range(8):
			GPIO_CHIP_DATA[i].setup( k, 'IN', j)
class Sensor :
	def __init__(self,index):
		self.index = index
	def readMcp(self):
		try:
			while 1:
				prdata=""
				prdata2=""
				count =0
				port=1
				for i in range(len(i2cADDR)):
					for j in GP:
						for k in range(8):
							switch = GPIO_CHIP_DATA[i].input(k, j)
							if(switch==1 or switch==0):
								prdata2+="PORT"+str(port)+":"+ str(switch)	
							prdata+=str(self.changeVal(switch))+"*"
							if(switch !=log[count]):
								print ("Port:"+str(port)+":"+str(switch))
								log[count]=switch
							time.sleep(0.001)
							count+=1
							port+=1				
						time.sleep(0.01)

				#print(log)
				#print()
				self.saveFile(prdata)
		except KeyboardInterrupt:
			print ('End exemple.py!')
	def saveFile(self,data):
		f = open('/home/pi/datapin.txt','w')
		
		f.write(data)
		f.close()
	def changeVal(self,data):
		if (data==0):
			return False
		elif(data==1):
			return True
Sensor(0).readMcp()