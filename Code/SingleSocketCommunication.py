import ifaddr, socket, pickle

class Packet:
    sequenceNumber = 0
    size = 0
    sequenceSize = 0
    data = 0

#grabs all the nics on the host
adapters = ifaddr.get_adapters()

HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)

# Create second socket on different NIC
s2 = socket  .socket(socket.AF_INET, socket.SOCK_STREAM)
s2.bind(('192.168.0.3', PORT))
s2.listen((1))
conn2, addr2 = s2.accept()
print('Socket 2 connected at', addr2)

data = conn.recv(4096)
data_variable = pickle.loads(data)
conn.close()
print (data_variable.sequenceNumber)
# Access the information by doing data_variable.process_id or data_variable.task_id etc..,
print ('Data received from client on socket 1')

# Recieve second chunk of data
data2 = conn2.recv(4096)
data_variable2 = pickle.loads(data2);
conn2.close()
print(data_variable2.sequenceNumber)
print ('Data received from client on socket 2')
