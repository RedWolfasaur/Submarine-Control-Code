import socket, select
import serial, time

#ser1 = serial.Serial('COM3', 9600)

#THIS FILE IS FOR RECIEVING TEXT (TO CONTROL ARDUINO)

UDP_IP = "127.0.0.1"
UDP_PORT = 8080
MESSAGE = b"TEST"

connected_sockets = []

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind((UDP_IP, UDP_PORT))
server_sock.listen()

connected_sockets.append(server_sock)
buffer_size = 4096
"""
(socketForClient, clientIP) = sock.accept()
        MESSAGE = input("MSG: ").encode('utf-8')
        socketForClient.send(MESSAGE)]
        print("sent")
"""
time.sleep(5)
print("Ready")

while True:
        read_sockets, write_sockets, error_sockets = select.select(connected_sockets, [], [])
        
        for sock in read_sockets:

                if sock == server_sock:
                        print("Client accepted")
                        sockfd, client_address = server_sock.accept()
                        connected_sockets.append(sockfd)
                        sockfd.send("Ready for data.".encode("utf-8"))
                        

                else:
                        try:
                                print (' Buffer size is %s' % buffer_size)
                                data = sock.recv(buffer_size)
                                txt = data.decode();
                                """
                                if (ser1.inWaiting() > 0):
                                        print("data")
                                        print(ser1.read().decode())
                                        ser1.flushInput()

                                if txt.startswith("ECHO"):
                                        print("SENDING:")
                                        print(txt)
                                        sock.send(data)
                                        print("SENT")

                                if txt == ("w"):
                                        print("SENDING TO ARDUINO:")
                                        print(txt)
                                        ser1.write(txt.encode("UTF-8"))
                                        print("SENT")

                                if txt == ("s"):
                                        print("SENDING TO ARDUINO:")
                                        print(txt)
                                        ser1.write(txt.encode("UTF-8"))
                                        print("SENT")
                                """

                                if txt == ('p'):
                                        server_sock.shutdown()

                                elif txt:
                                        print(txt)
                            
                        except:
                                sock.close()
                                connected_sockets.remove(sock)
                                continue
