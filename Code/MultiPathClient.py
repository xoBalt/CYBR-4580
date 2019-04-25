import socket
import packet
import pickle
import ThreadedSession
import time
import random

connections = []
i = 0
hostCount = int(input("Host count: "))
hostIPs = []

#Initialize all the sockets that will be used and create list of host ips.
while i < hostCount:
    hostIPs.append(input("Server ip/hostname: "))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections.append(sock)
    i+=1

#Grab server port from user
while True:
    port = input("Server port: ")
    try:
        port = int(port) #Ensure port is valid.
        break
    except ValueError:
        print("Port must be an integer value")
        pass

i = 0
#Connects sockets to all the host ips and stores them in a list.
while i < hostCount:
    print("Connecting socket to: "+hostIPs[i])
    connections[i].connect((hostIPs[i], port))
    i+=1


size = 2048

#Constant loop to send messages
while True:
    count = 0

    message = input("message: ")

    if message == "stop":
        break
    #Split sentence per word and put it in individual packet
    data = []
    sentence = []
    sentence = str.split(message, " ")

    #initialize array of packets
    for word in sentence:
        data.append(packet.packet(None,None,None,None,word,None,None))

    #send each packet
    for datum in data:
        #select random connection to send the data on
        randomConnection = random.randint(0,len(connections)-1)
        #Set packet information
        datum.sequence_number = count
        datum.size = len(data)
        datum.destination = connections[randomConnection].getsockname()
        print(datum.data)
        connections[randomConnection].send(pickle.dumps(datum))
        count+=1
        #time.sleep(0.1)
        print("Sent to: "+ str(datum.destination))

#close all the connections if the user types "stop"
for connection in connections:
    connection.close()