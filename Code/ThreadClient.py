import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostIP = input("Server ip/hostname: ")
while True:
    port = input("Server port: ")
    try:
        port = int(port) #Ensure port is valid.
        break
    except ValueError:
        print("Port must be an integer value")
        pass

sock.connect((hostIP, port)) #Takes one argument containing both parameters.
size = 256
while True:
    data = input("message: ")
    sock.send(data.encode())
    received = sock.recv(size)
    print("response: {}".format(received.decode()))
