import db as db
import time
import threading
import os
os.environ['DISPLAY'] = ":0"
#print(os.environ['DISPLAY'])
from pynput import mouse
dataChannel=db.readDb.readChannel(1)
mouseCond=1
waktu_sebelum=[0,0]
waktu=[100,1000]
class server:
    
    def __init__(self,index):
        self.index = index
    def readSleepTime(self):
        dataDb= db.readDb.readDataTabel(1,"m_mesin")
        return dataDb[0]["display_time"]
    def sendServer(self):
        global mouseCond
        global mouseCondFlag
        global waktu
        global waktu_sebelum
        millis=lambda:int(round(time.time()*1000))
        while True:
            time.sleep(0.1)
            waktu_sekarang=millis()
            if(waktu_sekarang-waktu_sebelum[0]>=waktu[0]):
                dataNotifNew=db.readDb.readNotifNew(2)
                if(len(dataNotifNew)>0):
                    mouseCond=1
                for i,chnData in enumerate(dataNotifNew):
                    print(chnData["kondisi"])
                    kondisi =chnData["kondisi"]
                    if (kondisi==0 and chnData["tel_low"]==1):
                        db.requestData.sendNotif(chnData["kode_mesin"],chnData["nama_gi"],chnData["nama_alat"],chnData["nama_mesin"],chnData["port"],chnData["tanggal"],chnData["status"],chnData["flag_kondisi"],chnData["ipserver"])
                    if (kondisi==1 and chnData["tel_high"]==1):
                        db.requestData.sendNotif(chnData["kode_mesin"],chnData["nama_gi"],chnData["nama_alat"],chnData["nama_mesin"],chnData["port"],chnData["tanggal"],chnData["status"],chnData["flag_kondisi"],chnData["ipserver"])                
                    db.updDb.updData(2,"notif_list","flag_notif","1","id",chnData["id"])
                    time.sleep(0.1)
                waktu_sebelum[0]=waktu_sekarang
            if(waktu_sekarang-waktu_sebelum[1]>=waktu[1]):
                if(mouseCond==2):
                    print("display off")
                    os.popen("vcgencmd display_power 0")
                    
                    waktu[1]=100
                    mouseCond+=1
                if(mouseCond==3):
                    mouseCond=0
                if(mouseCond==1):
                    print("display on")
                    os.popen("vcgencmd display_power 1")
                    
                    #print(self.readSleepTime())
                    waktu[1]=self.readSleepTime()*1000
                    mouseCond+=1
                waktu_sebelum[1]=waktu_sekarang
                
                
               
                #print(mouseCond)
               
#server.sendServer(0)
class Mouse:
    def __init__(self,index):
        self.index = index
    def on_move(self,x, y):
        global mouseCond
        if(mouseCond==0):
            mouseCond=1
        
    def readMouse(self):
        with mouse.Listener(on_move=self.on_move) as listener :
            listener.join()
        #global waktu
        #waktu_sebelum=[0,0]
        #millis=lambda:int(round(time.time()*1000))
       
        # while True:
        #     waktu_sekarang=millis()
        #     if(waktu_sekarang-waktu_sebelum[0]>=waktu[0]):
        #         waktu_sebelum[0]=waktu_sekarang
        #     if(waktu_sekarang-waktu_sebelum[1]>=waktu[1]):
        #         waktu_sebelum[1]=waktu_sekarang


p1 = threading.Thread(target=server(0).sendServer)
p2 = threading.Thread(target=Mouse(0).readMouse)
p1.start()
p2.start()
p1.join()
p2.join
    