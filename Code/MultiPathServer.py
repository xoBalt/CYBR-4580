import socket
import threading
import pickle
import packet
import ifaddr
import time

sessioncount = 0
sessions = []
array = []
sem_lock = threading.Lock()

class ThreadedServer(object):
    def __init__(self, host, port): #Socket boilerplate.
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        print("Session running on: "+self.host)

        self.sock.listen(5) # Listen for incoming connections. Queue up to five waiting to be handled in threads.
        client, address = self.sock.accept()
        client.settimeout(60)
        self.listenToClient(client,address)

    def listenToClient(self, client, address):
        size = 2048

        while True:
            try:
                data = client.recv(size) # Listen for data from client.
                if data:
                    #locks access to the array to avoid different threads writing over each other
                    sem_lock.acquire()
                    array.append(pickle.loads(data))
                    sem_lock.release()
                    #after modifying the array it is released

                    print("...")

                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":

    #this method allows us to sort by sequence number
    def sortbysequence(val):
        return val.sequence_number

    #get all network adapters
    adapters = ifaddr.get_adapters()

    #Print out all available network interfaces
    for adapter in adapters:
        #Don't use the default loopback interfaces
        if adapter.nice_name.find("Loopback") == -1:
            print( adapter.nice_name)
            for ip in adapter.ips:
                print("   %s/%s" % (ip.ip, ip.network_prefix))
        else:
            #remove the loopback interface
            adapters.remove(adapter)


    while True:
        #Each NIC operates on the same port (this isn't necessary but just allows for faster testing)
        portNo = input("Port? ")
        try:
            portNo = int(portNo) # Ensure port is valid.
            break
        except ValueError:
            pass

    #This loop will print out the adapter that is being used and create a new thread to listen for incomming
    #connections on each NIC. It will also add each session to a list of sessions.
    for adapter in adapters:
        print(adapter.nice_name)
        sessions.append(ThreadedServer(adapter.ips[-1].ip,portNo))
        #Create a new thread for each NIC
        threading.Thread(target = sessions[sessioncount].listen,args = ()).start()
        sessioncount+=1
    #This loop prints the contents of the data that has been recieved every 5 seconds then clears it.
    while True:
        time.sleep(5)
        array.sort(key= sortbysequence)
        for datum in array:
            print(datum.data)
        array.clear()

