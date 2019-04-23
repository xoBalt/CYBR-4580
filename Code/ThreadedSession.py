class ThreadedSession(object):
    def __init__(self, host, port): #Socket boilerplate.
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        print("Session running on: "+self.host)
        # Listen for incoming connections. Queue up to five waiting to be handled in threads.
        self.sock.listen(5)
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

                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False