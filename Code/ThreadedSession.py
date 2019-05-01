import pickle
import array
import socket
import hashlib
import SessionManager
import ifaddr
import threading

class ThreadedSession(object):
    def __init__(self, host, port, semaphore, session_manager): #Socket boilerplate.
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #self.sock.bind((self.host, self.port))
        self.sem_lock = semaphore
        self.manager = session_manager

    def listen(self):
        try:
            self.sock.bind((self.host, self.port))
            #print("Session running on: "+self.host)
            # Listen for incoming connections. Queue up to five waiting to be handled in threads.
            self.sock.listen(5)
            client, address = self.sock.accept()
            client.settimeout(60)
            self.listenToClient(client)
        except OSError:
            print("...")

    def connect(self, dest_address, dest_port):
        #print(dest_addregss+", "+str(dest_port))
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((dest_address, dest_port))
        print("Connected "+self.host+" and "+ str(dest_address))


    def listenToClient(self, client):
        size = 2048
        #print("Connection made on " + self.host)
        while True:
            data = client.recv(size) # Listen for data from client.
            if data:
                #locks access to the array to avoid different threads writing over each other
                self.sem_lock.acquire()
                self.manager.data_array.append(pickle.loads(data))
                self.sem_lock.release()
                #after modifying the array it is released

            else:
                client.close()
                return False

    def stop(self):
        self.sock.close()

    #we need to be able to send/receive data at the same time
    #figure out how to connect threads to new endpoints
    def connectToClient(self, client):
        client.send(data)