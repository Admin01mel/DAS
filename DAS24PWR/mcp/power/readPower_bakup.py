import serial
import time
import struct
import array
import json
import mqtt as mqtt
import sys
sys.path.insert(0, '/home/pi/mcp')
import db as db
import math
import requests
import binascii

kode="000"
ser = None
client =None
par=None
jsonRes={"kode":"","type":0,"F":0,"VRN":0,"VSN":0,"VTN":0,"VAVG":0,"VRS":0,"VST":0,"VRT":0,"IR":0,"IS":0,"IT":0,"IN":0,"PFR":0,"PFS":0,"PFT":0,"PFAVG":0}
dataRequest=[]
idModbus=[0]
type=[0]
countModbus=[0,0]
req=[[0x01, 0x03, 0x40, 0x00, 0x00, 0x40],
     [0x01, 0x03, 0x40, 0x00, 0x00, 0x40],
     [0x01, 0x03, 0x40, 0x00, 0x00, 0x40]] #crc belum ada 
req2=[  [0x02, 0x03, 0x0B, 0xB7, 0x00, 0x40],
        [0x02, 0x03, 0x0C, 0x05, 0x00, 0x08],
        [0x02, 0x03, 0x0C, 0x25, 0x00, 0x2]]
dataSensor=[""]*20
reg =[0]*20
jumlah=3
for i in range(20):
    reg[i]=jumlah
    jumlah+=4
mqtt=mqtt.MQTT(0)


class config():
    def __init__(self,index):
        self.index = index
    def initConfig(self):
        global client 
        global ser
        global par
        dt= db.readDb.readDataTabel(1,"daspower_config")
        global req
        global dataRequest
        global idModbus
        global kode
        ###############config MQTT##################
       
        if(client!=None):
            print("rekonnect mqtt")
            client.disconnect()
        mqttUser =  dt[0]["user_mqtt"]
        mqttPass= dt[0]["pass_mqtt"]
        broker = dt[0]["server_mqtt"]
        port =dt[0]["port_mqtt"]
        client=mqtt.connect_mqtt(mqttUser,mqttPass,broker,port)
        client.loop_start()

        #################config Serial ###########
        if(ser!=None):
            ser.close()
        baud= dt[0]["baud_serial"]
        kode=dt[0]["kode_mesin"]
        jsonRes["kode"]=kode
        parity = int(dt[0]["parity_serial"])
        if(parity==0):
            par=serial.PARITY_NONE
        elif(parity==1):
            par=serial.PARITY_EVEN
        elif(parity==2):
            par=serial.PARITY_ODD
       #// ser=serial.Serial('/dev/ttyS0', baudrate = baud, timeout = 1,parity=par,)
        ser=serial.Serial('/dev/ttyAMA0', baudrate = baud,parity=par,  bytesize=8, timeout=1)
        #ser=serial.Serial('/dev/ttyS0', baud,serial.SEVENBITS, serial.PARITY_NONE,serial.STOPBITS_ONE)
        
        db.updDb.updData(1,"daspower_config","flag",0,"flag",1)

        ################Config Modbus ##################
               
        idModbus[0]=int(dt[0]["id_modbus"])
        type[0]=int(dt[0]["type"])
        print(idModbus)
       #jika jumlah data banyak
        # jml=0
        # for x,y in enumerate(dt):
        #     idModbus.append(int(y["id_modbus"]))
        #     type.append(int(y["type"]))
        Helper(0).resetJsonres()


class Modbus():
    def __init__(self,index):
        self.index = index
    def modbusCrc(self,msg:str) -> int:
        crc = 0xFFFF
        for n in range(len(msg)):
            crc ^= msg[n]
            for i in range(8):
                if crc & 1:
                    crc >>= 1
                    crc ^= 0xA001
                else:
                    crc >>= 1
        return crc
    def writeModbus(self,req):
        reqStr=""
        for i in range(len(req)):
            reqStr+="%02x" % req[i]
        msg = bytes.fromhex(reqStr)
        crc = self.modbusCrc(msg)
        ba = crc.to_bytes(2, byteorder='little')
        req.append(ba[0])
        req.append(ba[1])
        values = bytearray(req)
        ser.write(values)

class MainClass():
    def __init__(self,index):
        self.index = index   
    def inisialisasiLCD(self,dataChannel):
        #ChannelData= dbRead.readChannel()
        ip = self.readIp()
        print(ip)
        ser.write(bytes(ip, 'ASCII'))
        time.sleep(0.2)
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
            ser.write(bytes(dt2, 'ASCII'))          
            time.sleep(0.2)
            #ser.write(bytes("T"+strjml+channel, 'ASCII'))
            #print(dt2)
            time.sleep(0.2)
            jml+=1
    def readNotifLCD(self):
        dataNotif=db.readDb.readNotifLCD(1)
        return dataNotif
    def readKondisiLCD(self):
        return db.readDb.readKondisiLCD(1)
    def resetFlagLCD(self,idNotif):
        dataNotif=db.updDb.updData(1,"notif_list","flag_notif_lcd",1,"port",idNotif)
        print(dataNotif)
    def readIp(self):
        url='http://localhost/das/backend/webapi/get_network.php?type=eth'
        url2='http://localhost/das/backend/webapi/get_network.php?type=wlan'
        res=requests.get(url)
        res2=requests.get(url2)
        row = json.loads(res.text)
        row2 = json.loads(res2.text)
        dtIp=row['IP']
        dtWf=row2['IP']
        return f"I WIFI:{dtWf}   IP: {dtIp}"
    def readLcdButton(self,x):
        #print(x)
        if(x==b'Z'):
            db.updDb.rstMesin(1)
            print("reset")
        if(x==b'['):
            db.updDb.updM_mesin(1,"mute",1)
            print("mute")
    def readLCDCond(self):
        serRes=""
        ser.write(bytes("O", 'ASCII'))
        while ser.in_waiting:  # Or: while ser.inWaiting():
            serRes+=str(ser.readline())
        print(serRes)
        if(serRes.find('M')>0):
            resArr= serRes.split('M')
            if((resArr[1]).find('5')>-1):
                #ser.write(bytes("A", 'ASCII'))
                db.updDb.updM_mesin(1,"mute",1)
                print("mute")
            if((resArr[2][0:4]).find('5')>-1):
                db.updDb.rstMesin(1)
                ser.write(bytes("B", 'ASCII'))
                #db.updDb.rstMesin(1)
                dataChannel=db.readDb.readChannel(1)
                self.inisialisasiLCD(dataChannel)
                print("reset")
        time.sleep(0.1)
    def mainLoop(self):
        global req
        global ser
        modbus= Modbus(0)
        dataChannel=db.readDb.readChannel(1)
        configLcd = dataChannel[0]["cfg"]
        self.inisialisasiLCD(dataChannel)
        if(int(configLcd)==1):
            self.inisialisasiLCD(dataChannel)
        #print(configLcd)
        waktu_sebelum=[0,0,0]
        waktu=[5000,100,10000]
        millis=lambda:int(round(time.time()*1000))
        global countModbus
        global jsonRes
        while True:
            waktu_sekarang=millis()
            if(waktu_sekarang-waktu_sebelum[0]>=waktu[0]):
                waktu_sebelum[0]=waktu_sekarang
                idM= idModbus[countModbus[1]]
                Type=int(type[countModbus[1]])
                if(Type ==0):
                    jmlArray=len(req[countModbus[0]])
                    if(jmlArray>6):
                        for i in range(jmlArray-6):
                            try:
                                req[countModbus[0]].pop()
                            except:
                                print("jml error")
                    req[countModbus[0]][0]=int(idModbus[countModbus[1]])
                    modbus.writeModbus(req[countModbus[0]])  
                elif(Type==1):
                    jmlArray=len(req2[countModbus[0]])
                    if(jmlArray>6):
                        for i in range(jmlArray-6):
                            try:
                                req2[countModbus[0]].pop()
                            except:
                                print("jml error")
                    req2[countModbus[0]][0]=int(idModbus[countModbus[1]])
                    modbus.writeModbus(req2[countModbus[0]])
                dt=ser.read(200)
                if(len(dt)>5):
                    serRespond=[0]*300 #buffer data respon meter
                    time.sleep(0.1)
                    for i in range(len(dt)):
                        serRespond[i]=(dt[i])
                    #print(serRespond[1])
                    if(serRespond[1]==3):
                        fReg= 3
                        for i in range(len(reg)):
                            fhex=""
                            for j in range(4):
                                dthex=(serRespond[reg[i]+j])
                                fhex+="%02x" % dthex
                            dataFloat=struct.unpack('!f', bytes.fromhex(fhex))[0]
                            dataSensor[i]=round(dataFloat,4)
                    Helper(0).toJson(dataSensor,Type,idM,serRespond[2])
                countModbus[0]+=1
                if(countModbus[0]==len(req)):
                    countModbus[0]=0  
                    countModbus[1]+=1
                    jsonRes["IDMODBUS"]=idM
                    
                    try:
                        mqtt.send(client,str(jsonRes),jsonRes["kode"],idM)
                        #db.updDb.updDaspwrMon(0,jsonRes,idM)
                        print("test")
                    except:
                        print("data not standart")
                    Helper(0).resetJsonres()
                if(countModbus[1]==len(idModbus)):
                    countModbus[1]=0
                
                
            #LCD wintec
            if(waktu_sekarang-waktu_sebelum[1]>=waktu[1]):
                waktu_sebelum[1]=waktu_sekarang
                dataNotif=self.readKondisiLCD()
                #dt=ser.read(5)
                #self.readLcdButton(dt)
                self.readLCDCond()
                if(len(dataNotif)>0):
                    for i in range(len(dataNotif)):
                        port=dataNotif[i]["port"]
                        dataLcd="N"+str(port)
                        ser.write(bytes(dataLcd, 'ASCII'))
                        dt=ser.read(3)
                        countSer=0
                        while(dt=='\x01'):
                            dt=ser.read()
                            if(countSer>20 and countSer<25):
                                print(port)
                                ser.write(bytearray(dataLcd,'ascii'))
                            if (countSer>25):
                                break
                            time.sleep(0.1)
                        time.sleep(0.1)

                        self.resetFlagLCD(port)
                        print("break"+ str(port))
                
                time.sleep(0.1)
    

                if(waktu_sekarang-waktu_sebelum[2]>=waktu[2]):
                    waktu_sebelum[2]=waktu_sekarang
                    print("baca LCD") 
                    dataChannel=db.readDb.readChannel(1)
                    configLcd = dataChannel[0]["cfg_lcd"]
                    configPwr=dataChannel[0]["power_cfg"]
                    reset =dataChannel[0]["reset_lcd"]
                    if(int(configLcd)==1):
                        self.inisialisasiLCD(dataChannel)
                        db.updDb.updM_mesin(1,"cfg_lcd",0) 
                    if(int(configPwr)==1):
                        cfg = config(0)
                        cfg.initConfig()
                    if(int(reset)==1):
                        print("reset channel")
                        ser.write(bytes('S', 'ASCII'))
                        ser.write(bytes('S', 'ASCII'))
                        db.updDb.updM_mesin(1,"reset_lcd",0) 

                      
class Helper():
    def __init__(self,index):
        self.index = index 
    def getPfVal(self,x):
        data=0
        if (x > 1) :
            data= 2 - x
        elif (x < -1) :
            data= -2 - x   
        elif ( abs(x) == 1):
            data= x
        else :
            data= x
        if math.isnan(data)==True:
            return 0
        else:
            return data
    def resetJsonres(self):
        #print("reset data")
        global jsonRes
        jsonRes["VRN"] = 0
        jsonRes["VSN"] = 0
        jsonRes["VTN"] = 0
        jsonRes["VAVG"] = 0
        jsonRes["VAVGN"] = 0
        jsonRes["VRS"] = 0
        jsonRes["VST"] = 0
        jsonRes["VRT"] = 0
        jsonRes["PFR"] = 0
        jsonRes["PFS"] = 0
        jsonRes["PFT"] = 0
        jsonRes["PFAVG"] =0
        jsonRes["F"]=0
        jsonRes["IDMODBUS"]=0


    def toJson(self,data,type,idm,res):
        global jsonRes
        global kode
        jsonRes["kode"]=kode
        jsonRes["type"]=type
        jsonRes["IDMODBUS"]=idm

        if(type==0): 
            dataParam=["F","VRN","VSN","VTN","VAVGN","VRS","VST","VRT","VAVG","IR","IS","IT","IN","PFR","PFS","PFT","PFAVG"]
            for i in range(len(dataParam)):
                jsonRes[dataParam[i]]=data[i]
        if(type==1):
            
            if(res==128):
                
                jsonRes["VRN"] = data[14]
                jsonRes["VSN"] = data[15]
                jsonRes["VTN"] = data[16]
                jsonRes["VAVG"] = data[13]
                jsonRes["VRS"] = data[10]
                jsonRes["VST"] = data[11]
                jsonRes["VRT"] = data[12]
                jsonRes["VAVGN"] = data[18]
            if(res==16):
                jsonRes["PFR"] = self.getPfVal(data[0])
                jsonRes["PFS"] = self.getPfVal(data[1])
                jsonRes["PFT"] = self.getPfVal(data[2])
                jsonRes["PFAVG"] =self.getPfVal(data[3])
            if(res==4):
                jsonRes["F"]=data[0]
               


if __name__ =="__main__":
    
    config(0).initConfig()
    MainClass(0).mainLoop() 
