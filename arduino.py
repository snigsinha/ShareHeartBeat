import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

def myHeartBeat():
    #while True:
    read_serial=ser.readline()
    myBeat = int(read_serial)
    return myBeat
#myHeartBeat()