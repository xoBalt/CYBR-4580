import socket, pickle

class Packet:
    sequenceNumber = 0
    size = 0
    sequenceSize = 0
    data = 0


HOST = 'localhost'
PORT = 50007
# Create a socket connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Create second socket
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect(('192.168.0.3',PORT))

# Create an instance of ProcessData() to send to server.
datum = Packet()
# Pickle the object and send it to the server
data_string = pickle.dumps(datum)
s.send(data_string)

#load the new data into the object and send
datum.sequenceNumber = 1
data_string = pickle.dumps(datum)
s2.send(data_string)

s.close()
s2.close()
print ('Data Sent to Server')