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
        #Woah is this a thread of threads?
        self.listenToClient(client,address)

    def listenToClient(self, client, address):
        size = 4096
        response = "All good!"

        while True:
            try:
                data = client.recv(size) # Listen for data from client.
                if data:
                    sem_lock.acquire()
                    array.append(pickle.loads(data))
                    sem_lock.release()

                    print("...")

                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

            client.send(response.encode())



if __name__ == "__main__":
    adapters = ifaddr.get_adapters()

    for adapter in adapters:
        if adapter.nice_name.find("Loopback") == -1:
            print( adapter.nice_name)
            for ip in adapter.ips:
                print("   %s/%s" % (ip.ip, ip.network_prefix))
        else:
            #remove the loopback interface
            adapters.remove(adapter)


    while True:
        portNo = input("Port? ")
        try:
            portNo = int(portNo) # Ensure port is valid.
            break
        except ValueError:
            pass

    for adapter in adapters:
        print(adapter.nice_name)
        sessions.append(ThreadedServer(adapter.ips[-1].ip,portNo))
        #Create a new thread for each NIC
        threading.Thread(target = sessions[sessioncount].listen,args = ()).start()
        sessioncount+=1

    while True:
        time.sleep(5)
        for datum in array:
            print(datum.data)

