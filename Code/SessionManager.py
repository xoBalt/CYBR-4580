import pickle
import ThreadedSession
import threading
import packet
import time
import socket
import ifaddr
import random

data_array = []
size = 2048


class SessionManager(object):
    def __init__(self, dest_addr, local_addr, local_port, dest_port, semaphore): #Socket boilerplate.
        self.dest_addr = dest_addr
        self.local_addr = local_addr
        self.local_port = local_port
        self.dest_port = dest_port
        self.sem_lock = semaphore
        self.data_array = data_array
        self.sessions = []
        self.threads = []
        self.connection_count = 0

    def initialize_threads(self, adapters):
        # This loop will print out the adapter that is being used and create a new thread to listen for incomming
        # connections on each NIC. It will also add each session to a list of sessions.
        for adapter in adapters:
            if(isinstance(adapter,ifaddr.Adapter)):
                print("Starting session on " + adapter.nice_name+" at "+adapter.ips[0].ip)
                # start listening on NICs
                try:
                    self.sessions.append(ThreadedSession.ThreadedSession(adapter.ips[0].ip, self.local_port, self.sem_lock, self))
                    t = threading.Thread(target=self.sessions[self.connection_count].listen, args=())
                    self.threads.append(t)
                    t.start()
                    self.connection_count += 1
                except OSError:
                    print("Invalid ip address for interface: " + str(adapters[self.connection_count]))
            else:
                adapters.remove(adapter)



    def kill_threads(self):
        #Close all the sockets in the threads
        for connections in self.sessions:
            connections.sock.close()
        #Wait for all the threads to finish up
        for thread in self.threads:
            thread.join()
        #clean up
        self.connection_count = 0
        self.threads.clear()
        self.sessions.clear()
        print("All threads dead.")

    def initialize_connections(self):
        address_i = 0
        #Shuffle destination addresses
        random.shuffle(self.dest_addr)
        for session in self.sessions:
            session.connect(self.dest_addr[address_i].ips[0].ip, self.dest_port)
            address_i += 1

        print("Connections made....")
    #sends list of available ip addresses
    def handshake_send(self, sock, dest_ip):
        handshake_packet = packet.packet(socket.AF_INET, dest_ip, 1, 2048,pickle.dumps(self.local_addr), None, None)
        sock.send(pickle.dumps(handshake_packet))
        print("Sent local addresses.")
        for address in self.local_addr:
            print("     "+str(address))
        #sock.send(pickle.dumps(self.local_addr))

    #returns a list of ip addresses
    def handshake_recv(self):
        print("Handshake recieved.")
        address = []
        try:
            for packet in self.data_array:
                addresses = pickle.loads(packet.data)
        except AttributeError:
            print("Got that error")

        print("Possible Destination Addresses: ")
        for address in addresses:
            print("    "+ str(address.ips[0].ip))
            self.dest_addr.append(address)
        self.data_array.clear()
        return addresses