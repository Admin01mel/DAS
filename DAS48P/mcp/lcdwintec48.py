from urllib.request import DataHandler
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import serial
import time  
import requests
import json
#import RPi.GPIO as IO
import asyncio
import db as db
#import das24
#import mcp/readMCP
import threading
type = 24
pin=[0]*type


modbusServ = modbus_rtu.RtuServer(serial.Serial(port='/dev/ttyS0',baudrate= 115200,                 bytesize=8, parity='N', stopbits=1, xonxoff=0))
modbusServ.start()
slave_1 = modbusServ.add_slave(1,unsigned=False)
slave_1.add_block("stringVal", cst.HOLDING_REGISTERS, 0, 10000)
slave_1.add_block("coil",cst.READ_COILS,0,60)
slave_1.add_block("lamp",cst.READ_DISCRETE_INPUTS,0,100)
slave = modbusServ.get_slave(1)
flagmute =0
flagrelay = 0
flagcond =0
page =0
flagSumCnd=0
globaljml=0
flagglobaljml=0
config=[0,0,0] #mute,reset,cfg
dly =0
class webapi:
    def readConfig():
        global dly
        row = db.readDb.readM_mesin(2)
        dly=float(row[0]["system_delay"])

    def readlog(page):
        res = db.readDb.readLog(2,page)
        return res
    def readchn():
        res = db.readDb.readChannelLCD(2)
        return res
    def rstchn():
        res = db.updDb.rstMesinLCD(2)
        print("reset")
    #def readcond():
     #   print('hahha')
class service:
    def clearchn():
        data_name =()
        for x in range(1920):
            data_name=data_name+(0,)
        slave.set_values ("stringVal",40 ,data_name )
    def clearlogservice():
        data_name =()
        for x in range(2340):
            data_name=data_name+(0,)
        slave.set_values ("stringVal",4000 ,data_name )   
    def readlogservice(page):
        api=webapi
        dt=api.readlog(page)
        chnaddr=4000 #2000
        stsaddr=4320 #2160 
        dateaddr=4680 #
        locaddr=5000
        dly=0
        for x in dt:
            cnd_name=()
            sts_name=()
            date_name=()
            loc_name=()
            nama = list(x["nama_alat"])
            status = list(x["status"])
            date = list(x["tanggal"].strftime('%Y-%m-%d %H:%M:%s'))
            loc = list(x["nama_gi"])
          #  dly=(x["system_delay"])
            for y in nama:
                name2 = ord(y)
                cnd_name=cnd_name+(name2,)
            for z in status:
                status2 = ord(z)
                sts_name=sts_name+(status2,)
            for a in date:
                date2 = ord(a)
                date_name=date_name+(date2,)
            for b in loc:
                loc2 = ord(b)
                loc_name=loc_name+(loc2,)
           
            slave.set_values ("stringVal",chnaddr , cnd_name)
            slave.set_values ("stringVal",stsaddr , sts_name)
            slave.set_values ("stringVal",dateaddr , date_name)
            slave.set_values ("stringVal",locaddr , loc_name)
            chnaddr=chnaddr+40
            stsaddr=stsaddr+40
            dateaddr=dateaddr+40
            locaddr=locaddr+40
            #locaddr=locaddr+40
        #print(dly)
                
    # def readconf():
    #     f = open("/home/pi/conf.txt", "r")       
    #     data=int(f.read())
    #     return data
    def readrst():
        f = open("/home/pi/rst.txt", "r")       
        data=int(f.read())
        f.close()
        return data
    def writeconf(data):
        f = open("/home/pi/conf.txt", "w")
        f.write(str(data))
        f.close()
    def writemute(data):
        db.updDb.updM_mesin(2,'mute',data)
    def writerst(data):
        f = open("/home/pi/rst.txt", "w")
        f.write(str(data))
        f.close()
     
    def readcondservice():
        api=webapi
        dt=api.readchn()
        cnd=()
        jml=0
        sumCnd=0
        global config
        global flagSumCnd
        chnaddr=2000
        for x in dt:
            cnd_name=()
            cnd=cnd+(int(x["flag_kondisi"]),)
            jml=jml+(int(x["kondisi"]))
            sumCnd=sumCnd+(int(x["kondisi"]))
            config[0]=x['mute']
            config[1]=x['reset']
            config[2] = x["cfg"]
            if(int(x["flag_kondisi"])>0):
                #print("ok")
                name=list(x["high"])
                for y in name:
                    name2 = ord(y)
                    cnd_name=cnd_name+(name2,)
            else :
                #print("no")
                name=list(x["low"])
                for y in name:
                    name2 = ord(y)
                    cnd_name=cnd_name+(name2,)
            slave.set_values ("stringVal",chnaddr , cnd_name)
            #print(chnaddr)
            chnaddr=chnaddr+40
        #'slave.set_values ("stringVal",2000 , (80,213,2))'
                
        slave.set_values ("lamp",0 , cnd)
        global flagrelay
        global globaljml
        globaljml = jml
        #print(flagSumCnd)
        if(flagSumCnd!=sumCnd):
            slave.set_values("lamp",52,(0))
            flagSumCnd=sumCnd
        else:
            slave.set_values("lamp",52,(1))
        if sumCnd>0:
            #slave.set_values("lamp",52,(1))
            flagrelay=1
        else:
            #slave.set_values("lamp",52,(0))
            flagrelay=0
api = webapi
serv = service
def readchnname():
    api = webapi
    dtjson =  api.readchn()
    cond=()
    regaddr = 40
    for x in dtjson:
        alat = list(x["nama_alat"])
        chn2=()
        a = 0
        cond=cond+(int(x["flag_kondisi"]),)
        for y in alat:
            alat2=ord(y)
            if(a>15):
                chn2=chn2+(10,)
                a=0
            chn2=chn2+(alat2,)
            a=a+1
        slave.set_values ("stringVal",regaddr , chn2)
        regaddr=regaddr+40
    slave.set_values ("lamp",0 , cond)    

def runAsync(x):
    loop=asyncio.get_event_loop()
    loop.run_until_complete(x)
    loop.close() 
def getIp():
    url='http://localhost/das/backend/webapi/get_network.php?type=eth'
    url2='http://localhost/das/backend/webapi/get_network.php?type=wlan'
    res=requests.get(url)
    res2=requests.get(url2)
    row = json.loads(res.text)
    row2 = json.loads(res2.text)
    ip=()
    wf=()
    dtIp=row['IP']
    dtWf=row2['IP']
    if(dtIp==None):
        dtIp="0.0.0.0        "
    if(dtWf==None):
        dtWf="0.0.0.0        "
    for x in dtIp:
        ips=ord(x)
        ip=ip+(ips,)
    for x in dtWf:
        ips=ord(x)
        wf=wf+(ips,)
    print(wf)
    slave.set_values ("stringVal",8000 , ip)
    slave.set_values ("stringVal",8040 , wf)
webapi.readConfig()
serv.readlogservice(page)
slave.set_values ("stringVal",5400 , [(page+1)])
readchnname()
getIp()
def arrayPage(page):
    arrPage=[]
    row= str(page)
    for i in row:
        arrPage.append(ord(i))
    return arrPage


def writeLcd():
    millis=lambda:int(round(time.time()*1000))
    waktu_sebelum=[0,0]
    waktu=[100,1000,3000]
    global flagglobaljml
    global globaljml
    global conf
    global page
    while True:
        waktu_sekarang=millis()   
        if(waktu_sekarang-waktu_sebelum[1]>=waktu[1]):
            serv.readcondservice()
            waktu_sebelum[1]=waktu_sekarang
        
        arrayPage(str(page))
        values = slave.get_values("coil", 0, 10)
        rst = values[3]
        alm = values[1] #input mute dari LCD
        muteDb = config[0]
        slave.set_values("lamp",50,(muteDb))
        #print(rst)
    # rsthmi=serv.readrst()
        
        #conf=serv.readconf()
        if(int(config[2])>0): ## membaca perubahab konfig channel
            print('update')
            serv.clearchn()
            readchnname()
            #db.updDb.updM_mesin(2,"cfg",0)
            serv.clearlogservice()
            serv.readlogservice(0)
            slave.set_values ("stringVal",5400 , arrayPage(1))
            slave.set_values("coil",6,(0))
        # readchnname()
        if(globaljml!=flagglobaljml):
            serv.clearlogservice()
            serv.readlogservice(0)
            flagglobaljml=globaljml
            slave.set_values ("stringVal",5400 , arrayPage(1))
        #print(globaljml)
        nextpage=values[4] # tombol next page
        prevpage=values[5] # tombol prev page 
        firstpage=values[6]
        #slave.set_values ("stringVal",5400 , [(str(21))])  
        
        if(firstpage>0):
            page=page+1
            serv.clearlogservice()
            serv.readlogservice(0)
            slave.set_values("coil",6,(0))
            page =0
            slave.set_values ("stringVal",5400 , arrayPage(page+1))
            #slave.set_values ("stringVal",5400 , [(str(page+1))])
        if(nextpage >0):
            page=page+1
            serv.clearlogservice()
            serv.readlogservice(page)
            slave.set_values("coil",4,(0))
            print("tambah")
            slave.set_values ("stringVal",5400 , arrayPage(page+1))
        if(prevpage >0):
            if(page>0):
                page=page-1
                serv.clearlogservice()
                serv.readlogservice(page)
                slave.set_values("coil",5,(0))
                slave.set_values ("stringVal",5400 , arrayPage(page+1))
                #slave.set_values ("stringVal",5400 , [ord(str(page+1))])
        if(alm>0):
            print('Tombol mute ditekan')
            slave.set_values("coil", 1, (0))
            #print(muteDb)
            print(flagrelay)
            if(flagrelay>0):
                if(muteDb==0):
                    slave.set_values("lamp",50,(1))
                    serv.writemute(1)
                else:
                    slave.set_values("lamp",50,(0))
                    serv.writemute(0)
            else:
                slave.set_values("lamp",50,(1))
                serv.writemute(1)
        if(rst>0):
            global pin
            global flagcond
            global flagmute
            global type
            serv.clearchn()
            readchnname()
            api.rstchn()
            getIp()
            pin=[0]*type
            print("resetLCD")
            slave.set_values("coil",0,(0,0,0,0,0,0,0,0))
            slave.set_values("lamp",50,(0))
            flagcond=0
            flagmute=0        
        time.sleep(0.01)

thread1 = threading.Thread(target=writeLcd)
thread1.daemon=True
thread1.start()
