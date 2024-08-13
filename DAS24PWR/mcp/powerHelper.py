import db
import math
kode="000"
ser = None
client =None
client2 =None
par=None
jsonRes={"kode":"","type":0,"F":0,"VRN":0,"VSN":0,"VTN":0,"VAVG":0,"VRS":0,"VST":0,"VRT":0,"IR":0,"IS":0,"IT":0,"IN":0,"PFR":0,"PFS":0,"PFT":0,"PFAVG":0,"KW":0,"KVA":0,"KVAR":0,"IAVG":0}
dataRequest=[]
idModbus=[0]
type=[0]
countModbus=[0,0]
req=[[0x01, 0x03, 0x40, 0x00, 0x00, 0x50],
     [0x01, 0x03, 0x40, 0x22, 0x00, 0x30],
     [0x01, 0x03, 0x40, 0x00, 0x00, 0x50]] #crc belum ada 
req2=[  [0x02, 0x03, 0x0B, 0xB7, 0x00, 0x40],
        [0x02, 0x03, 0x0C, 0x05, 0x00, 0x08],
        [0x02, 0x03, 0x0C, 0x25, 0x00, 0x2]]
req3=[  [0x01, 0x04, 0x00, 0x01, 0x00, 0x28],
        [0x01, 0x04, 0x00, 0x29, 0x00, 0x14],
        [0x01, 0x04, 0x00, 0x01, 0x00, 0x28]
        ]
dataSensor=[""]*40
reg =[0]*20
jumlah=3
for i in range(20):
    reg[i]=jumlah
    jumlah+=4

class Modbus():
    def __init__(self,index):
        self.index = index
    def configModbus(self):
        global idModbus
        dt= db.readDb.readDataTabel(1,"daspower_config")
        idModbus[0]=int(dt[0]["id_modbus"])
        type[0]=int(dt[0]["type"])

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
    def writeModbus(self,req,ser):
        reqStr=""
        for i in range(len(req)):
            reqStr+="%02x" % req[i]
        msg = bytes.fromhex(reqStr)
        crc = self.modbusCrc(msg)
        ba = crc.to_bytes(2, byteorder='little')
        req.append(ba[0])
        req.append(ba[1])
        values = bytearray(req)
        print(values.hex())
        ser.write(values)
       # return values
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
        jsonRes["IAVG"] = 0


    def toJson(self,data,type,idm,res):
        global jsonRes
        global kode
        jsonRes["kode"]=kode
        jsonRes["type"]=type
        jsonRes["IDMODBUS"]=idm

        if(type==0): 
           
            if(res==160):
                dataParam=["F","VRN","VSN","VTN","VAVGN","VRS","VST","VRT","VAVG","IR","IS","IT","IN"]
                
                for i in range(len(dataParam)):
                    jsonRes[dataParam[i]]=data[i]
                jsonRes["IAVG"] = data[12]
                #,"PFR","PFS","PFT","PFAVG"
            if(res==96):
                #print(data)
                jsonRes["KW"] = data[0]
                jsonRes["KVA"] = data[8]
                jsonRes["KVAR"] = data[4]
                jsonRes["PFR"] = data[9]
                jsonRes["PFS"] = data[10]
                jsonRes["PFT"] = data[11]
                jsonRes["PFAVG"] = data[12]
             
                #print(res)
                #print(data)
                
                # jsonRes["IAVG"] = data[12]
                # jsonRes["PFR"] = data[14]
                # jsonRes["PFS"] = data[15]
                # jsonRes["PFT"] = data[16]
                # jsonRes["PFAVG"] = data[17]
                
        if(type==1):
            if(res==128):
                jsonRes["IR"] = data[0]
                jsonRes["IS"] = data[1]
                jsonRes["IT"] = data[2]
                jsonRes["IN"] = data[3]
                jsonRes["IAVG"] = data[5]
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
                kvaR=jsonRes["VRN"]* jsonRes["IR"]
                kvaS=jsonRes["VSN"]* jsonRes["IS"]
                kvaT=jsonRes["VTN"]* jsonRes["IT"]
                jsonRes["KVA"] = (kvaR+kvaS+kvaT)/1000
                kwR=kvaR*jsonRes["PFR"] 
                kwS=kvaS*jsonRes["PFS"] 
                kwT=kvaT*jsonRes["PFT"] 
                jsonRes["KW"] = (kwR+kwS+kwT)/1000
                KVARR=math.sqrt((math.pow(kvaR,2))-(math.pow(kwR,2)) )
                KVARS=math.sqrt((math.pow(kvaS,2))-(math.pow(kwS,2))) 
                KVART=math.sqrt((math.pow(kvaT,2))-(math.pow(kwT,2))) 
                jsonRes["KVAR"] =(KVARR+KVARS+KVART)/1000
                jsonRes["F"]=data[0]
        if(type==2): 
            if(res==80):
                jsonRes["VRN"] = data[0]
                jsonRes["VSN"] = data[1]
                jsonRes["VTN"] = data[2]
                jsonRes["VAVGN"] = data[3]

                jsonRes["VRS"] = data[4]
                jsonRes["VST"] = data[5]
                jsonRes["VRT"] = data[6]
                jsonRes["VAVG"] = data[7]
                
                jsonRes["IR"] = data[8]
                jsonRes["IS"] = data[9]
                jsonRes["IT"] = data[10]
                jsonRes["IN"] = 0
                jsonRes["IAVG"] = data[11]
                
            if(res==40):
                jsonRes["KW"] = data[1]
                jsonRes["KVA"] = data[2]
                jsonRes["KVAR"] = data[3]
                jsonRes["PFR"] = data[4]
                jsonRes["PFS"] = data[5]
                jsonRes["PFT"] = data[6]
                jsonRes["PFAVG"] =data[7]
                jsonRes["F"]=data[8]
               
                
            
                        
