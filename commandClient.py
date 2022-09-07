import socket
import msvcrt

#THIS FILE IS FOR SENDING COMMANDS TO ARDUINO


#start the Keyboard thread



UDP_IP = "127.0.0.1"
UDP_PORT = 8080

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

#This line works if pi is on
#print (socket.gethostbyname("raspberrypi"))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((UDP_IP, UDP_PORT))
#sock.settimeout(1.0)
sock.setblocking(0)




while True:
        if msvcrt.kbhit():
                sock.send(msvcrt.getch())
                
        try:
                MSG = sock.recv(4096);
                print(MSG.decode())
        except:
                continue
        
