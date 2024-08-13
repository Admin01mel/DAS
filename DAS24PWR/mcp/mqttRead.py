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
client.subscribe("DASPOWER/"+kode_mesin+"/MODBUS/MUTE/#")
client.subscribe("DASPOWER/"+kode_mesin+"/MODBUS/RESET/#")


def on_message(client, userdata, msg):
    print(msg)
    type= msg.topic.split("/")
    if(type[3]=="MUTE"):
        if(int(msg.payload)==1):
            response=requests.get('http://127.0.0.1/das/backend/webapi/readmute.php?w=1')
            print(response)
            if response.status_code == 200:
                # Print the response content
                print(response.text)
            else:
                print("Failed to fetch data. Status code:", response.status_code)

            
    elif(type[3]=="RESET"):
        if(int(msg.payload)==1):
            response=requests.get('http://127.0.0.1/das/backend/webapi/resetflag.php')
            print(response)
            if response.status_code == 200:
                # Print the response content
                print(response.text)
            else:
                print("Failed to fetch data. Status code:", response.status_code)
            print("reset cuy")
    print(msg.topic+" "+str(msg.payload))
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected MQTT disconnection. Will auto-reconnect")


def mqtt_loop(client):
    client.on_message = on_message
    #client.on_disconnect = on_disconnect
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
      
        mute=res[0]["mute"]
        kodes=res[i]["kode_mesin"]
        #print(mute)
        topic=f"DASPOWER/{kode}/MODBUS/MUTECondition" 
        result=mute
        mqtt.send(client,str(result),topic) 
        time.sleep(2)

p1 = threading.Thread(target=mqtt_loop, args=(client,))
p2 =threading.Thread(target=channel_loop, args=(client,))
p1.start()
p2.start()
p1.join()
p2.join()