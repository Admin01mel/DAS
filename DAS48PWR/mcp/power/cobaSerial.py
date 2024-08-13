import serial
import time
 

ser = serial.Serial('/dev/ttyAMA0', baudrate = 19200, timeout = 1,parity=serial.PARITY_EVEN,)
jml=0
ser.write(bytes("I IP=192.168.0.10 WIFI 192.168.0.1", 'ASCII'))

time.sleep(2)
dt=ser.read(1)
print(dt)
jml+=1
