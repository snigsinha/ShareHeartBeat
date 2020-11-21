import socket
from arduino import myHeartBeat
from beat import playHeartBeat

HOST = '138.16.161.123'
PORT = 65432

def connect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        th = []
     
        while True:
            myBeat = str(myHeartBeat())
            s.sendall(myBeat.encode())
       #     print('my beat :' + myBeat)
            
            data = s.recv(1024)
            if not data:
                continue
            otherBeat = data.decode()
         #   print('other beat: ' + otherBeat)
            if otherBeat != '':
                otherBeat = int(otherBeat)
                if otherBeat > 0:
                    playHeartBeat(otherBeat)
        
        #data = s.recv(1024)
    
        #print('Received', repr(data))

connect()
