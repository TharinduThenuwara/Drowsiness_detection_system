import time
import paho.mqtt.client as paho

broker = 'test.mosquitto.org'
port = 1883
username = 'iot_user'
password = 'iot@1234'
client_id = 'python-mqtt'

topic = "sleep1"
temp_topic = topic 


def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))


# configure mqtt client
client = paho.Client(client_id)
client.username_pw_set(username, password)
client.on_message = on_message

print("connecting to broker ", broker)
client.connect(broker)

client.loop_start()     # start loop to process received messages
                        # client.loop_forever()
print("subscribing ")
client.subscribe(temp_topic)  # subscribe



while(1):
    print("publishing ")
   
    client.publish(temp_topic, 1)  # publish
    time.sleep(2)
client.disconnect()  # disconnect
