import paho.mqtt.client as MQTTClient
import time

def OnConnect(client, userdata, flags, rc):
    if rc == 0:
        print("Client is connected")
        global Connected
        Connected = True
    else:
        print("Client is not connected")

def OnMessage(client, userdata, message):
    print("Message received "+ str(message.payload.decode("utf-8")))
    print("Topin "+str(message.topic))

Connected = False
MessageReceived = False
Broker_Adrress = "test.mosquitto.org"
Topic = "Test"
port = 1883
user= "DIUEIL"
password = "0000"
Client = MQTTClient.Client("MQTT")
Client.username_pw_set(user, password=password)
Client.on_connect = OnConnect
Client.connect(Broker_Adrress, port=port)
Client.loop_start()
Client.subscribe("Test")
while Connected != True:
    time.sleep(0.5)
while MessageReceived != True:
    time.sleep(0.5)

Client.loop_stop()







