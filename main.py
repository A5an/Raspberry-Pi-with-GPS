import serial
import time
import string
import pynmea2
import firebase_admin
import json
import time
from firebase_admin import db, credentials

cred = credentials.Certificate("/home/asan/credentials.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://sharsha-8e860-default-rtdb.firebaseio.com/"})

def geoloc():
        port="/dev/ttyAMA0"
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        out = pynmea2.NMEAStreamReader()
        data=ser.readline().decode('unicode_escape')

        if data[0:6] == "$GPRMC":
                msg=pynmea2.parse(data)
                lat=msg.latitude
                lng=msg.longitude
                loc = str(lat) + ', ' + str(lng)
                db.reference("/Location").set(loc)


running = True
while running:
        geoloc()
        time.sleep(3)