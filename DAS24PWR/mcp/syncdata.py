import time  
import requests
import json
import db as db
import os
import RPi.GPIO as GPIO
link =19
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(link, GPIO.OUT)
class webapi:
    def readlog(page):
        url='http://localhost/dasmonanouncer/backend/webapi/viewlog.php'
        obj = {'data':page}
        res=requests.post(url,data=obj,timeout=3)
        #print(res.json())
        return res.json()
    def readchn():
        res=db.readDb.readChannelSynk(1)
        #res =requests.get("http://localhost/dasmonanouncer/backend/webapi/viewcond.php")
        #print(res)
        return res
       # print(res)
    def readnet():
        res=requests.get("http://localhost/dasmonanouncer/backend/webapi/viewnetwork.php")
        data = json.loads(res.text, timeout=3)
        print(data[0]["ipserver"])
        return data[0]["ipserver"]
    def server(dt):
        net = dt[0]["ipserver"]
        #print(dt[0])
        data=json.dumps(dt)
        try:
            url = 'http://'+net+'/dasmon/apialat/updcond24.php'
            #print(url)
            myobj = {'data': data}
            resp=requests.post(url, data = myobj,timeout=3)
            url2 =f"http://{net}/getTimeServer"
            resp2=requests.post(url2, timeout=3)
            if resp.status_code == 200 or resp2.status_code == 200:
                print ('success!')
                GPIO.output(link, GPIO.HIGH)  
            else:
                print ('fail!')
                GPIO.output(link, GPIO.LOW)  
        except:
            print("request error")
            GPIO.output(link, GPIO.LOW) 
        #print(url)
        #print(dt)
        #print(res.text)
def syncTime():
    api = webapi
    chn = api.readchn()
    ipserver = chn[0]["ipserver"]
    url="http://"+ipserver+"/dasmon/apialat/getdate.php"
    try:
        req=requests.get(url, timeout=3)
        res=req.text.replace("<html>","")
        res2=res.replace("</html>","")
        res3=res2.replace("/","-")
        res4=res3.split("*")
        res5=res4[1].split(" ")
        res6= res5[0].split("-")
        dates=f'{res6[2]}-{res6[1]}-{res6[0]} {res5[1].replace(".",":")}'
        command=f"sudo date -s \"{dates}\""
        print(command)
        os.popen(command)
    except :
        print("error")
    
    #print(command)
   # res4= res3[1].replace("/","-")
  



syncTime()
api = webapi
while True:
    try:
        data = api.readchn()
        serv = api.server(data)
    except:
        print ("datanotfound")
    time.sleep(90)
    
