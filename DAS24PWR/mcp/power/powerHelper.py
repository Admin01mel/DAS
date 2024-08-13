import db

class config():
    def __init__(self,index):
        self.index = index
    def readLCDCond(self,ser):
        serRes=""
        ser.write(bytes("O", 'ASCII'))
        while ser.in_waiting:  # Or: while ser.inWaiting():
            serRes+=str(ser.readline())