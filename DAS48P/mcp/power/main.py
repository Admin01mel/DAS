import serial
import struct

ser = serial.Serial(
    port='com8',
    baudrate=19200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)


def modbusCrc(msg:str) -> int:
    crc = 0xFFFF
    for n in range(len(msg)):
        crc ^= msg[n]
        for i in range(8):
            if crc & 1:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

msg = bytes.fromhex("010340000040")
crc = modbusCrc(msg)
print("0x%04X"%(crc))            
ba = crc.to_bytes(2, byteorder='little')
#print(type(crc))
#message_bytes=bytes.fromhex("01034000004051FA")
#cw = [0x05,0x03,0x40,0x00,0x00,0x40,0x51,0xFA]

#ser.write(serial.to_bytes(cw))
#count=''
#response = ser.read()
#print(response)
#dt="01034000004051FA".decode('hex')
#ser.write(dt)
#response = ser.read()
#print(response)