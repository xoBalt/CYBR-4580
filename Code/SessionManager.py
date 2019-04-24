import pickle
import ThreadedSession
import threading
import packet

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
        self.connection_count = 0

    def initialize_threads(self, adapters):
        # This loop will print out the adapter that is being used and create a new thread to listen for incomming
        # connections on each NIC. It will also add each session to a list of sessions.
        for adapter in adapters:
            print("Starting session on " + adapter.nice_name)
            # start listening on NICs
            self.sessions.append(ThreadedSession.ThreadedSession(adapter.ips[0].ip, self.local_port, self.sem_lock, self))
            threading.Thread(target=self.sessions[self.connection_count].listen, args=()).start()
            self.connection_count += 1
            # Create a new thread for each NIC

    def kill_threads(self):
        for connection in self.sessions:
            connection.sock.close()
        self.connection_count = 0
        print("All threads dead.")

    #sends list of available ip addresses
    def handshake_send(self, socket):
        print("Sent local addresses.")
        socket.send(pickle.dumps(self.local_addr))

    #returns a list of ip addresses
    def handshake_recv(self):
        print("Handshake recieved.")

        address = []
        try:
            for data in self.data_array:
                addresses = data
        except AttributeError:
            print("Got that error")

        self.dest_addr = addresses
        self.data_array.clear()
        return addresses