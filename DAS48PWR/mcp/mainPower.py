import RPi.GPIO as GPIO
from time import sleep
import os
import sys
import time
import requests
import busio
import digitalio
import threading 
import requests
from datetime import datetime
import db as db
from MCP23017_I2C import *
import os
import serial
import json
import binascii
import powerHelper as pwr
import struct
import mqtt as mqtt
#from multiprocessing import Process, Queue
countRead=0
dataPin=""
DASPORT = 48
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
boot=0
#mqtt cuy
ser = None
client =None
client2 =None
mqttUser=""
mqttPass=""
broker=""
port=""
mqtt=mqtt.MQTT(0)
reconnectMqtt=0
###################inisialisasi relay###############
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
####################inisialisasi i2c###############
i2cADDR=[0x20,0x21,0x22]
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
    #print(telLow)  


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
        global millis
        global ser
        global boot
        dataChannel=db.readDb.readChannel(1)
        LCD(0).inisialisasiLCD(dataChannel)
        while True:
            time.sleep(0.1)
            self.systemConfig()

            for i,item in enumerate(dataNotif):
                #update kondisi & flag kondisi
                try:
                    db.updDb.updMesin(0,item["cond"],item["flagCond"],item["port"])
                    time.sleep(0.1)
                    #print(item["port"]-1)
                    if (item["cond"]==0 and telLow[(item["port"]-1)]==1):
                        print("ins LOW")
                        db.InsDb.insNotif_list(0,item["port"],item["cond"],item["flagCond"],item["date"])
                    elif (item["cond"]==1 and  telHigh[(item["port"]-1)]==1):
                        db.InsDb.insNotif_list(0,item["port"],item["cond"],item["flagCond"],item["date"])
                        print("ins high")
                    dataLcd="N"+str((item["port"]))    
                    ser.write(bytes(dataLcd, 'ASCII'))
                    print(dataLcd)
                    time.sleep(0.1)
                    dataNotif.pop(i)
                except NameError:
                    os.popen("pm2 restart all")
                    #print(NameError)
                    sleep(1)
                
            
    def systemConfig(self):
        time.sleep(0.1)
        global dataChannel
        global mute
        global flagJmlAlrm
        global dataNotif
        global ser
        global countRead
        global mqttUser
        global mqttPass
        global broker
        global port
        global reconnectMqtt
        global client
        cfg=db.readDb.reaConfig(1)
        chnConfig=cfg[0]['cfg'] #var deteksi perubahan channel&config 
        rstChn =cfg[0]['reset']
        mute = cfg[0]['mute']
        wifi = cfg[0]['wifi']
        net = cfg[0]['net']
        reboot= cfg[0]['reboot']
        cfgPwr=cfg[0]['power_config']
        ser.flushOutput()
        ser.write(bytes("O", 'ASCII'))
        dt=ser.read(13)
        serRes=""  
        lenDt=len(dt)
        if(lenDt==13):
            if(dt[0]==77):
                for i in range(len(dt)):
                    serRes+=str(dt[i]) 
                try:
                    resArr= serRes.split('77') 
                    if((resArr[1]).find('50')>-1):
                        #ser.write(bytes("A", 'ASCII'))
                        db.updDb.updM_mesin(1,"mute",1)
                        print("mute")
                    if((resArr[2][0:4]).find('50')>-1):
                        ser.write(bytes("B", 'ASCII'))
                        db.updDb.rstMesin(1)
                    if((resArr[3][0:4]).find('50')>-1):
                        print("refresh wifi")
                        ipadr = LCD(0).readIp()
                        netw= ipadr.split(",")
                        ser.write(bytes("W "+netw[0], 'ASCII'))
                        time.sleep(0.2)
                    if((resArr[4][0:4]).find('50')>-1):
                        print("refresh Lan")
                        ipadr = LCD(0).readIp()
                        netw= ipadr.split(",")
                        ser.write(bytes("I "+netw[1], 'ASCII'))
                        time.sleep(0.2)
                except:
                            print(dt)
                            print("Serial Read Err")
        
        #fungsi read PowerMeter
        idM= pwr.idModbus[pwr.countModbus[1]]
        Type=int(pwr.type[pwr.countModbus[1]])
        #print("Type",Type)
        countRead=countRead+1
        if(countRead>2):
            #print(pwr.req[0])
            if(Type ==0):
               # pwr.req[0][0]=int(idM)
                pwr.req[pwr.countModbus[0]][0]=int(idM)
                ser.flushOutput()
                time.sleep(0.1)
                pwr.Modbus(0).writeModbus(pwr.req[pwr.countModbus[0]],ser)
                jmlArray=len(pwr.req[pwr.countModbus[0]])
                if(jmlArray>6):
                    for i in range(jmlArray-6):
                        try:
                            pwr.req[pwr.countModbus[0]].pop()
                        except:
                            print("jml error")
                # pwr.req[0].pop()
                # pwr.req[0].pop()
            elif(Type ==1):
                pwr.req2[pwr.countModbus[0]][0]=int(idM)
                ser.flushOutput()
                time.sleep(0.1)
                pwr.Modbus(0).writeModbus(pwr.req2[pwr.countModbus[0]],ser)
                jmlArray=len(pwr.req2[pwr.countModbus[0]])
                if(jmlArray>6):
                    for i in range(jmlArray-6):
                        try:
                            pwr.req2[pwr.countModbus[0]].pop()
                        except:
                            print("jml error")
            elif(Type ==2):
                pwr.req3[pwr.countModbus[0]][0]=int(idM)
                ser.flushOutput()
                time.sleep(0.1)
                pwr.Modbus(0).writeModbus(pwr.req3[pwr.countModbus[0]],ser)
                jmlArray=len(pwr.req3[pwr.countModbus[0]])
                if(jmlArray>6):
                    for i in range(jmlArray-6):
                        try:
                            pwr.req3[pwr.countModbus[0]].pop()
                        except:
                            print("jml error")
                #pwr.req2[0].pop()
                #pwr.req2[0].pop()
            dt=ser.read(300)
            #print("output Serial",dt)
            if(len(dt)>5):
                serRespond=[0]*200 #buffer data respon meter
                for i in range(len(dt)):
                    serRespond[i]=(dt[i])
                    #print(serRespond[1])
                    if(serRespond[1]==3 or serRespond[1]==4):
                        fReg= 3
                        for i in range(len(pwr.reg)):
                            fhex=""
                            for j in range(4):
                                dthex=(serRespond[pwr.reg[i]+j])
                                fhex+="%02x" % dthex
                            dataFloat=struct.unpack('!f', bytes.fromhex(fhex))[0]
                            pwr.dataSensor[i]=round(dataFloat,4)

                    pwr.Helper(0).toJson(pwr.dataSensor,Type,idM,serRespond[2])
            pwr.countModbus[0]+=1
            if(pwr.countModbus[0]==len(pwr.req)):
                pwr.countModbus[0]=0  
                pwr.countModbus[1]+=1
                pwr.jsonRes["IDMODBUS"]=idM
                try:
                    keys_jsonRes = list(pwr.jsonRes.keys())
                    for i in range(len(keys_jsonRes)):
                        #mqtt.send(client,str(pwr.jsonRes),pwr.jsonRes["kode"],idM) 
                        alias=str(pwr.jsonRes["kode"])+str(idM)+keys_jsonRes[i]
                        val= pwr.jsonRes[keys_jsonRes[i]]
                        res={"alias": alias, "val": val, "dataType": "float"}
                        topic=f"DASPOWER/"+str(pwr.jsonRes["kode"])+f"/MODBUS/{idM}/{keys_jsonRes[i]}"  
                        mqtt.send(client,str(res),topic)  
                        mqtt.send(client2,str(res),topic)  
                        
                        print(res)
                        time.sleep(0.01)
                   
                    # for i in range(len(flagKondisi)):
                    #     val=None
                    #     if (flagKondisi[i]==1):
                    #         val="True"
                    #     elif(flagKondisi[i]==0):
                    #         val="False"
                    #     alias=str(pwr.jsonRes["kode"])+str(idM)+"CHN"+str(i+1)
                    #     res={"alias": alias, "val": val, "dataType": "boolean"}
                    #     topic=f"DASPOWER/"+str(pwr.jsonRes["kode"])+f"/MODBUS/{idM}/CHN{str(i+1)}"  
                    #     mqtt.send(client,str(res),topic)  
                    #     time.sleep(0.01)    
                    
                    topic=f"DASPOWER/"+pwr.jsonRes["kode"]+f"/{idM}"
                    try:    
                        mqtt.send(client,str(pwr.jsonRes),topic)
                    except:
                        print("failed to send mqtt server")
                    try:    
                        mqtt.send(client2,str(pwr.jsonRes),topic)
                    except:
                        print("failed to send mqtt server")
                   
                    
                    #reconnectMqtt=0
                    #db.updDb.updDaspwrMon(0,jsonRes,idM)
                except NameError:
                    print("MQTT ERROR Reconnct MQT")
                    # if(reconnectMqtt>2):
                    #     reconnectMqtt=0
                    #     try:
                    #         client=mqtt.connect_mqtt(mqttUser,mqttPass,broker,port)
                    #         client.loop_start()
                    #     except:
                    #         print("reconnect")
                    # reconnectMqtt=reconnectMqtt+1
                    
                   

                # try:
                #     mqtt.send(client2,str(pwr.jsonRes),pwr.jsonRes["kode"],idM)
                # except NameError:
                #     print(NameError)
                #print(str(pwr.jsonRes))
                pwr.Helper(0).resetJsonres()
            if(pwr.countModbus[1]==len(pwr.idModbus)):
                pwr.countModbus[1]=0
            time.sleep(0.1)
            ser.flushOutput()
            countRead=0
       
        #config System
        if(cfgPwr==1):
            print("config bosku")
            db.updDb.updData(1,"daspower_config","flag",0,"flag",1)
            config(0).initConfig()

        if(chnConfig==1): #apabila Config dari db bernilai 1 
            inisialisasiChannel(1)
            print("Reset Config")
            dataChannel=db.readDb.readChannel(1)
            LCD(0).inisialisasiLCD(dataChannel)
            db.updDb.updM_mesin(1,"cfg",0) #mereset config
        if(rstChn==1): #apabila reset dari db bernilai 1 
            dataLcd="R01" 
            ser.write(bytes(dataLcd, 'ASCII'))
            for x,y in enumerate(flagKondisi):
                flagKondisi[x]=0
                kondisiOld[x]=0
                flagJmlAlrm=0
                dataNotif=[]
            print("channel reset")
            
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
        #print(flagKondisi)
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

class config():
    def __init__(self,index):
        self.index = index
    def initConfig(self):
        print("initConfig")
        global client
        global client2 
        global boot
        global ser
        global par
        global mqttUser
        global mqttPass
        global broker
        global port
        dt= db.readDb.readDataTabel(1,"daspower_config")
        global dataRequest
        ###############config MQTT##################
        if(boot==0):
            time.sleep(10)
            boot=1
       # time.sleep(1)
        if(client!=None):
            print("rekonnect mqtt 1")
            client.disconnect()
        if(client2!=None):
            print("rekonnect mqtt 2")
            client2.disconnect()
        mqttUser =  dt[0]["user_mqtt"]
        mqttPass= dt[0]["pass_mqtt"]
        broker = dt[0]["server_mqtt"]
        port =dt[0]["port_mqtt"]
        try:
            print(mqttUser)
            print(mqttPass)
            client=mqtt.connect_mqtt(mqttUser,mqttPass,broker,port)
            client.loop_start()
            #client.loop_forever()
        except:
            print("mqtt disconnect")
        client2=mqtt.connect_mqtt("das","das12345","localhost",1883)
        client2.loop_start()

    #################config Serial ###########
        if(ser!=None):
            ser.close()
        baud= dt[0]["baud_serial"]
        pwr.kode=dt[0]["kode_mesin"]
        pwr.jsonRes["kode"]=pwr.kode
        parity = int(dt[0]["parity_serial"])
        if(parity==0):
            par=serial.PARITY_NONE
        elif(parity==1):
            par=serial.PARITY_EVEN
        elif(parity==2):
            par=serial.PARITY_ODD
        ser=serial.Serial('/dev/ttyAMA0', baudrate = baud,parity=par,  bytesize=8, timeout=0.6)
        #ser=serial.Serial('/dev/ttyS0', baud,serial.SEVENBITS, serial.PARITY_NONE,serial.STOPBITS_ONE)
        db.updDb.updData(1,"daspower_config","flag",0,"flag",1)

     ################Config Modbus ##################
               
        pwr.idModbus[0]=int(dt[0]["id_modbus"])

        pwr.type[0]=int(dt[0]["type"])
        print(pwr.idModbus)
       #jika jumlah data banyak
        # jml=0
        # for x,y in enumerate(dt):
        #     idModbus.append(int(y["id_modbus"]))
        #     type.append(int(y["type"]))
        pwr.Helper(0).resetJsonres()   



class LCD():
    def __init__(self,index):
        self.index = index 
    def inisialisasiLCD(self,dataChannel):
        #ChannelData= dbRead.readChannel()

        ip = self.readIp()
        try:
            netw= ip.split(",")
            ser.write(bytes("W "+netw[0], 'ASCII'))
            time.sleep(0.2)
            ser.write(bytes("I "+netw[1], 'ASCII'))
            time.sleep(0.2)
        except:
            print("net err")
        jml=1
        for i in range(len(dataChannel)):
            channel =dataChannel[i]["nama_alat"]
            strjml=str(jml)
            if jml<10:
                strjml="0"+str(jml)
            
            dataChn=("T"+strjml+channel).encode()
            dataSend =binascii.hexlify(dataChn).decode() 
            dt1=dataSend[:50]+"0A"+dataSend[50:]
            #print(binascii.unhexlify(dt1).decode() )
            dt2=(binascii.unhexlify(dt1).decode() )
            time.sleep(0.2)
            ser.flushOutput()
            ser.write(bytes(dt2, 'ASCII'))    
            jml+=1
        print("done")
    def readIp(self):
        url='http://localhost/das/backend/webapi/get_network.php?type=eth'
        url2='http://localhost/das/backend/webapi/get_network.php?type=wlan'
        res=requests.get(url)
        res2=requests.get(url2)
        row = json.loads(res.text)
        row2 = json.loads(res2.text)
        dtIp=row['IP']
        dtWf=row2['IP']
        return f"{dtWf},{dtIp}"

def changeNet():
    net = db.readDb.readDataTabel(1,"network")
    ip = net[0]["iplocal"]
    #print(net)
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
    #print(dhcp)
    program=""
    if dhcp==0:
        program = 'sudo cat /home/pi/mcp/config/ipstatic.cfg > /etc/dhcpcd.conf'
        #print("ip static")
    elif dhcp==1:
        program ='sudo cat /home/pi/mcp/config/ipdynamic.cfg > /etc/dhcpcd.conf'
    os.popen(program)
    time.sleep(2)
    program ='sudo ifconfig eth0 down'
    os.popen(program)
    time.sleep(15)
    program ='sudo ifconfig eth0 up'
    os.popen(program)
    #print("LAN RESTARTED")
        
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
    #print("wifi restarted")
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
    config(0).initConfig()
    #print(dataChannel)
    p =threading.Thread(target=Sensor(0).readMcp)
    p2 =threading.Thread(target=SecondaryLoop(0).dataProcess)
    p.start()
    p2.start()
    p.join()
    p2.join()


