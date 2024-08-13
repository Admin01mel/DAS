import RPi.GPIO as GPIO
from time import sleep
import os
import sys
import time
import requests
import busio
import digitalio
import threading
import asyncio
from datetime import datetime
import db as db
from MCP23017_I2C import *
import os
#from multiprocessing import Process, Queue

dataPin=""
DASPORT = 24
jmlPin =0
delaySystem = 0
flagKondisi=[0]*DASPORT
flagJmlAlrm=0
pins = []
kondisi=[0]*DASPORT
kondisiOld=[0]*DASPORT
kondisiOldFlag=[0]*DASPORT
dataNotif=[]
telLow=[0]*DASPORT
telHigh=[0]*DASPORT
#dataTelegram=[]
dataChannel=[]
led1 = 4
led2=26
mute =0

###################inisialisasi relay###############
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
####################inisialisasi i2c###############
i2cADDR=[0x20,0x21]
GP=['A','B']
GPIO_CHIP_DATA=[0]*len(i2cADDR)
for i in range(len(i2cADDR)):
	GPIO_CHIP_DATA[i]=GPIO_CHIP(i2cADDR[i],1)
jmlPort=0
for i in range(len(i2cADDR)):
	for j in GP:
            if(jmlPort<DASPORT):
                    for k in range(8):
                        jmlPort+=1
                        GPIO_CHIP_DATA[i].setup( k, 'IN', j)
####################inisialisasi data channel#######
dataChannel=db.readDb.readChannel(1)
######################inisialisasi milis#############
waktu_sebelum=[0]*DASPORT
waktu=[0]* DASPORT
millis=lambda:int(round(time.time()*1000))

def inisialisasiChannel(x):
    global dataChannel
    global kondisiOld
    global flagKondisi
    global flagJmlAlrm
    global telLow
    global telHigh
    dataChannel=db.readDb.readChannel(1)
    global waktu
    jmlAlrm=0
    for i,dt in enumerate(dataChannel):
        waktu[i]=dt["delay"]*1000
        telLow[i]=dt["tel_low"]
        telHigh[i]=dt["tel_high"]
        kondisiOld[i]=dt["flag_kondisi"]
        jmlAlrm+=dt["flag_kondisi"]
        if(x==0):
            flagKondisi[i]=dt["flag_kondisi"]
            kondisiOld[i]=dt["flag_kondisi"]
    flagJmlAlrm=jmlAlrm
    print(telLow)  


class Sensor: 
    def __init__(self,index):
        self.index = index
  
    def readMcp(self):
        print('ok')
        global waktu
        global waktu_sebelum
     
        try:
            while 1:
                time.sleep(0.001)
                waktu_sekarang=millis()
                prdata=""
                prdata2=""
                count =0
                port=1
                jmlPort=0
                for i in range(len(i2cADDR)):
                    for j in GP:
                        if(jmlPort<DASPORT):
                            for k in range(8):
                                jmlPort+=1
                                switch = self.inverts(GPIO_CHIP_DATA[i].input(k, j))
                                if dataChannel[count]["invert"]==1:
                                    switch=self.inverts(switch)
                                if waktu[count]==0:
                                    if(switch==1 or switch==0):
                                        prdata2+="PORT"+str(port)+":"+ str(switch)	
                                        prdata+=str(self.changeVal(switch))+"*"
                                    if(switch !=None):
                                        if(switch !=kondisiOld[count]):
                                            print ("Port:"+str(port)+":"+str(switch))
                                            kondisiOld[count]=switch
                                            if(switch==1):
                                                flagKondisi[count]=1                                  
                                            dataNotif.append({"port":port,"cond":kondisiOld[count],"date": getDate(),"flagCond":flagKondisi[count]})
                                else:                                
                                    if(waktu_sekarang-waktu_sebelum[count]>=waktu[count]):
                                        if(switch !=kondisiOld[count]):
                                            kondisiOldFlag[count]=1
                                            kondisiOld[count]=switch
                                        if(kondisiOldFlag[count]==1 and kondisiOld[count]==switch):
                                            print ("Port:"+str(port)+":"+str(switch))
                                            if(switch==1):
                                                flagKondisi[count]=1                                
                                            dataNotif.append({"port":port,"cond":kondisiOld[count],"date": getDate(),"flagCond":flagKondisi[count]})
                                            kondisiOldFlag[count]=0
                                        elif(kondisiOldFlag[count]==1 and kondisiOld[count]!=switch):
                                            print("er")
                                            kondisiOld[count]=switch
                                            kondisiOldFlag[count]=0
                                                
                                        waktu_sebelum[count]=waktu_sekarang
                                time.sleep(0.001)
                                count+=1
                                port+=1				
                        #time.sleep(0.01)
                #self.saveFile(prdata)

        except KeyboardInterrupt:
            print ('End exemple.py!')
    def changeVal(self,data):
        if (data==0):
            return False
        elif(data==1):
            return True
 
    def inverts(self,data):
        if data==0:
            data=1
        else:
            data=0
        return data
class SecondaryLoop:
    def __init__(self,index):
        self.index = index        
    def dataProcess(self):
        global dataNotif
        global dataChannel
        global led1
        global telLow
        global telHigh
        waktu_sebelum2=0
        global millis
        while True:
            time.sleep(0.1)
            self.systemConfig()

            for i,item in enumerate(dataNotif):
                #update kondisi & flag kondisi
                try:
                    db.updDb.updMesin(0,item["cond"],item["flagCond"],item["port"])
                    time.sleep(0.1)
                    print(item["port"]-1)
                    if (item["cond"]==0 and telLow[(item["port"]-1)]==1):
                        print("ins LOW")
                        db.InsDb.insNotif_list(0,item["port"],item["cond"],item["flagCond"],item["date"])
                    elif (item["cond"]==1 and  telHigh[(item["port"]-1)]==1):
                        db.InsDb.insNotif_list(0,item["port"],item["cond"],item["flagCond"],item["date"])
                        print("ins high")
                    time.sleep(0.1)
                    dataNotif.pop(i)
                except:
                    print("database error")
                    sleep(1)
                
            
    def systemConfig(self):
        time.sleep(0.1)
        global dataChannel
        global mute
        global flagJmlAlrm
        global dataNotif
        cfg=db.readDb.reaConfig(1)
        chnConfig=cfg[0]['cfg'] #var deteksi perubahan channel&config 
        rstChn =cfg[0]['reset']
        mute = cfg[0]['mute']
        wifi = cfg[0]['wifi']
        net = cfg[0]['net']
        reboot= cfg[0]['reboot']
     
        if(chnConfig==1): #apabila Config dari db bernilai 1 
            #dataChannel=db.readDb.readChannel(1) #reset pengaturan awal channel 
            inisialisasiChannel(1)
            #time.sleep(4)
            print("Reset Config")
            db.updDb.updM_mesin(1,"cfg",0) #mereset config
        if(rstChn==1): #apabila reset dari db bernilai 1 
            for x,y in enumerate(flagKondisi):
                flagKondisi[x]=0
                kondisiOld[x]=0
                flagJmlAlrm=0
                dataNotif=[]
            #print("channel reset")
            
        if(wifi =="1"):
            print ("wifi config")
            changeWifi()
            db.updDb.updData(1,"wifi","flag",0,"flag",1)
        if(net =="1"):
            print ("LAN config")
            changeNet()
            db.updDb.updData(1,"network","flag",0,"flag",1)
        if(reboot ==1):
            print("reboot")
            db.updDb.updData(1,"power","reboot",0,"reboot",1)
            time.sleep(2)
            os.popen("sudo reboot")
        jmlAlrm=0    
        for i,item in enumerate(flagKondisi):
            jmlAlrm+=item
        print(flagKondisi)
        if (jmlAlrm<1):
            GPIO.output(led1, GPIO.LOW)
            GPIO.output(led2, GPIO.LOW)
            #print("lowcond")
        else:
            if(jmlAlrm!=flagJmlAlrm):
                db.updDb.updM_mesin(1,"mute",0) #apabila ada notif baru menyalakan alarm
                #print ("nyalakan alarm")
                flagJmlAlrm=jmlAlrm
                #mute=0

            if(mute==1):
                GPIO.output(led1, GPIO.LOW)
                GPIO.output(led2, GPIO.LOW)
                #print("alarm OFF")
            else:
                GPIO.output(led1, GPIO.HIGH)  
                GPIO.output(led2, GPIO.HIGH)    
        if(rstChn==1):
            #time.sleep(3)
            db.updDb.updM_mesin(1,"reset",0) #mereset channel
        #print(led1)

            #print(cfg[0][22])

def changeNet():
    net = db.readDb.readDataTabel(1,"network")
    ip = net[0]["iplocal"]
    print(net)
    gateway = net[0]["gateway"]
    netmask = net[0]["netmask"]
    dns = net[0]["dns"] 
    prefik = net[0]["prefik"]
    dhcp = net[0]["dhcp"]   
    dataSetting=f"\
hostname \n\
clientid \n\
persistent \n\
option rapid_commit \n\
option domain_name_servers, domain_name, domain_search, host_name \n\
option classless_static_routes \n\
option ntp_servers \n\
option interface_mtu \n\
require dhcp_server_identifier \n\
slaac private \n\
#ipbaru \n\
#set ip dari wizard \n\
interface eth0 \n\
static ip_address={ip}/{prefik}\n\
static ip6_address=fd51:42f8:caae:d92e::ff/64 \n\
static routers={gateway}\n\
static domain_name_servers={dns}"
    saveFile('ipstatic.cfg',dataSetting)
    print(dhcp)
    program=""
    if dhcp==0:
        program = 'sudo cat /home/pi/mcp/config/ipstatic.cfg > /etc/dhcpcd.conf'
        print("ip static")
    elif dhcp==1:
        program ='sudo cat /home/pi/mcp/config/ipdynamic.cfg > /etc/dhcpcd.conf'
    os.popen(program)
    time.sleep(2)
    program ='sudo ifconfig eth0 down'
    os.popen(program)
    time.sleep(15)
    program ='sudo ifconfig eth0 up'
    os.popen(program)
    print("LAN RESTARTED")
        
def changeWifi():
    wifi = db.readDb.readDataTabel(1,"wifi")
    ssid=wifi[0]["ssid"]
    password=wifi[0]["pass"]
    dataSetting='ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n\
update_config=1\n\
country=ID\n\
network={\n\
	ssid="'+ssid+'"\n\
	psk="'+password+'"\n\
	key_mgmt=WPA-PSK\n\
}'
    saveFile('wpa_supplicant.conf',dataSetting)
    os.popen("sudo cat /home/pi/mcp/config/wpa_supplicant.conf > /etc/wpa_supplicant/wpa_supplicant.conf")
    time.sleep(2)
    os.popen("sudo wpa_cli -i wlan0 reconfigure")
    time.sleep(2)
    os.popen("sudo ifconfig wlan0 down")
    time.sleep(5)
    os.popen("sudo ifconfig wlan0 up")
    print("wifi restarted")
def saveFile(loc,data):
    f = open(f'/home/pi/mcp/config/{loc}','w')
    f.write(data)
    f.close()

def changeBol(dt):
    y=0
    if(dt==True):
        y=0
    else:
        y=1
    return y
def getDate():
    now = datetime.now()
    now2=str(now).split(".")
    #print (strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    return now2[0]

def addNotif(x):
    global dataNotif
    dataNotif.append(x)
    #print(dataNotif)



if __name__ =="__main__":
    inisialisasiChannel(0)
    #print(dataChannel)
    p =threading.Thread(target=Sensor(0).readMcp)
    p2 =threading.Thread(target=SecondaryLoop(0).dataProcess)
    p.start()
    p2.start()
    p.join()
    p2.join()


