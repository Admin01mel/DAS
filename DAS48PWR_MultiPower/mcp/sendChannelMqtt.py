import mqtt
import db
mqtt=mqtt.MQTT(1)
import requests
dt= db.readDb.readDataTabel(1,"daspower_config")
import threading
import time
mqttUser =  dt[0]["user_mqtt"]
mqttPass= dt[0]["pass_mqtt"]
broker = dt[0]["server_mqtt"]
port =dt[0]["port_mqtt"]
kode_mesin=dt[0]["kode_mesin"]
client=mqtt.connect_mqtt(mqttUser,mqttPass,broker,port)
client.loop_forever()

def channel_loop(client):
    #print("test")
    while True:
        res=db.readDb.readChannelPower(1)
        for i in range(len(res)):

            kode=res[i]["kode_mesin"]
            idM=str(res[i]["id_modbus"])
            alias=kode+idM+"CHN"+str(res[i]["port"])
            val =""
            if(int(res[i]["flag_kondisi"])==0):
                val="False"
            elif(int(res[i]["flag_kondisi"])==1):
                val="True"
            topic=f"DASPOWER/"+kode+f"/MODBUS/{idM}/CHN{str(i+1)}" 
            result={"alias": alias, "val": val, "dataType": "boolean"}
           
            mqtt.send(client,str(result),topic)  
        time.sleep(2)
channel_loop(client)