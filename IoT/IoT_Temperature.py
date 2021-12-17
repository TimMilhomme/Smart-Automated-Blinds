import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT
from mpu9250_jmdev.registers import *
from mpu9250_jmdev.mpu_9250 import MPU9250
import time as t
import json
import math

#Initialize IMU
mpu = MPU9250(
            address_ak=AK8963_ADDRESS, 
            address_mpu_master=MPU9050_ADDRESS_68, # In 0x68 Address
            address_mpu_slave=None, 
            bus=1,
            gfs=GFS_1000, 
            afs=AFS_8G, 
            mfs=AK8963_BIT_16, 
            mode=AK8963_MODE_C100HZ)
mpu.configure() # Apply the settings to the registers.


# Define ENDPOINT, CLIENT_ID, PATH_TO_CERT, PATH_TO_KEY, PATH_TO_ROOT, MESSAGE, TOPIC, and RANGE
ENDPOINT = "ac6s09xm1v6hb-ats.iot.eu-west-1.amazonaws.com"
CLIENT_ID = "Temperature"
PATH_TO_CERT = "/home/tim/SAB/IoT/certificate.pem.crt"
PATH_TO_KEY = "/home/tim/SAB/IoT/30bd399a6e6e42f93d80a9dcf1528173d017832506e73a20dd365e23ca78c322-private.pem.key"
PATH_TO_ROOT = "/home/tim/SAB/IoT/AmazonRootCA1.pem"
TOPIC = "Temperature/result"


myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_ROOT, PATH_TO_KEY, PATH_TO_CERT)

while True:
    
    myAWSIoTMQTTClient.connect()
    
    temperature = mpu.readTemperatureMaster()
    message = {'Temperature':temperature}
    myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'Temperature/result'")
    myAWSIoTMQTTClient.disconnect()
    t.sleep(1)
