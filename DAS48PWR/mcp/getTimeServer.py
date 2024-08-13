import requests
import db
import json
import os
def readchn():
    res=db.readDb.readChannelSynk(1)
    return res
chn = readchn()
ipserver = chn[0]["ipserver"]
print(ipserver)
url =f"http://{ipserver}/getTimeServer"
req=requests.post(url, timeout=3)
jsons =json.loads(str(req.text))
datetime=jsons["time"].replace("T", " ")
command=f"sudo date -s \"{datetime[:-5]}\""
print(command)
os.popen(command)

