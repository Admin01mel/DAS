import random
import time
from paho.mqtt import client as mqtt_client
import json
import db

#broker = "203.194.112.238"
#port = 1883
topic = "python/mqtt"
# generate client ID with pub prefix randomly
client_id = 'python-mqtt-'+str(random.randint(0, 1000))
username = 'das'
password = 'mgi2022'


dt= db.readDb.readDataTabel(1,"daspower_config")
kode_mesin=dt[0]["kode_mesin"]

class MQTT():
    def __init__(self,index):
        self.index = index
    def connect_mqtt(self,name,passw,broker,port):
        #client=1
        #userdata=2

        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                #client.subscribe("DASPOWER/"+kode_mesin+"/MODBUS/MUTE/#")
                #client.subscribe("DASPOWER/"+kode_mesin+"/MODBUS/RESET/#")
                print("Connected to MQTT Broker!")
            else:
                print("Failed to connect, return code %d\n", rc)
        #name=""
        #passw=""
        #print (name)
        global kode_mesin
        client = mqtt_client.Client(client_id,clean_session=False)
        client.username_pw_set(name, passw)
        client.on_connect = on_connect
        client.connect(broker, port)
        client.subscribe("DASPOWER/"+kode_mesin+"/MODBUS/MUTE/#")
        client.subscribe("DASPOWER/"+kode_mesin+"/MODBUS/RESET/#")
        print("Subscribe","DASPOWER/"+kode_mesin+"/MODBUS/MUTE/#")
        return client
    
    
    def publish(self,client):
        msg_count = 0
        while True:
            
            msg = "messages: "+str(msg_count)
            result = client.publish(topic, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print("Send "+msg+" to topic "+topic)
            else:
                print("Failed to send message to topic "+topic)
                break
            msg_count += 1
    def send(self,client,message,tpc):
        try:
            msg=message
            topic=tpc
            dt=str(msg).replace("'", "\"")
            #print(dt)
            result = client.publish(topic, dt)
            status = result[0]
            if status == 0:
                print("Send "+msg+" to topic "+topic)
            else:
                print("Failed to send message to topic "+topic)
        except  Exception as e:
            print(e)
            print("Mqtt Failed to send")
    #def sendData(self,message):
       # send(message)

    def run(self):
        client = self.connect_mqtt()
        client.loop_start()
        self.send(client,"mqtt Connect")


# if __name__ == '__main__':
    
#    mqtt=MQTT(0)
#    client=mqtt.connect_mqtt()
#    client.loop_start()
#    mqtt.send(client,"HAHAH")

    #MQTT(0).run()