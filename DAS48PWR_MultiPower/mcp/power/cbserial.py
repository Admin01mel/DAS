import serial
import time
import struct
import array
import json
ser = serial.Serial('/dev/ttyAMA0', baudrate = 19200, timeout = 1,parity=serial.PARITY_EVEN,)
req=[0x02,0x03, 0x0B, 0xB7, 0x00, 0x40] #crc belum ada 
dataSensor=[""]*20
reg =[0]*20
jumlah=3


for i in range(20):
    reg[i]=jumlah
    jumlah+=4
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
        #print(ba)
        req.append(ba[0])
        req.append(ba[1])
       
        values = bytearray(req)
        #print(values)
        #ser.write(values)
        res = ser.read(20)
        print(res)
        return res

class MainClass():
    def __init__(self,index):
        self.index = index   
    def mainLoop(self):
        global req
        modbus= Modbus(0)
        helper =Helper(0)
        dt =modbus.writeModbus(req)
        print(dt)
        #while True:
            #dt =modbus.writeModbus(req)
            # serRespond=[0]*300
            # time.sleep(0.1)
            # for i in range(len(dt)):
            #     serRespond[i]=(dt[i])
            # if(serRespond[2]==128):
            #     fReg= 3
            #     for i in range(len(reg)):
            #         fhex=""
            #         for j in range(4):
            #             dthex=(serRespond[reg[i]+j])
            #             fhex+="%02x" % dthex
            #         dataFloat=struct.unpack('!f', bytes.fromhex(fhex))[0]
            #         dataSensor[i]=dataFloat
            # json = helper.toJson(dataSensor,0)
            # print(json)
            # time.sleep(1)
class Helper():
    def __init__(self,index):
        self.index = index   
    def toJson(self,data,type):
        if(type==0):
            json={"kode":"065","type":0}
            dataParam=["F","VRN","VSN","VTN","VAVGN","VRS","VST","VRT","PAVG","IR","IS","IT","IN","PFR","PFS","PFT","PFAVG"]
            for i in range(len(dataParam)):
                json[dataParam[i]]=data[i]
            return json




MainClass(0).mainLoop()        
    #print(struct.unpack('!f', bytes.fromhex(dataSensor[0]))[0])
    #struct.unpack('!f', bytes.fromhex(fhex))[0]
    

    #test=hex(serRespond[3])[2:]+hex(serRespond[4])[2:]+hex(serRespond[5])[2:]+hex(serRespond[6])[2:]
    #print(fhex)
    #print(struct.unpack('!f', bytes.fromhex(fhex))[0])
    #print(struct.unpack('!f', bytes.fromhex(fhex))[0])


# while True:
#     ser.write(values)
#     time.sleep(0.1)
#     data = ser.read(200)
#     for i in range(len(data)):
#         serRespond[i]=(data[i])
#     print(serRespond)
# while True:
#     ser.write(values)
#     data=ser.readline()
#     for i in range(len(data)):
#         serRespond[i]=(data[i])
#     print(serRespond)
#     time.sleep(0.1)
    
