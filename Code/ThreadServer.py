import socket
import threading

class ThreadedServer(object):
    def __init__(self, host, port): #Socket boilerplate.
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5) # Listen for incoming connections. Queue up to five waiting to be handled in threads.
        while True: # Create accepted connection state and send it off as thread.
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 256
        while True:
            try:
                data = client.recv(size) # Listen for data from client.
                if data:
                    # Set the response to echo back the recieved data.
                    response = data.decode()
                    print("From client: {}".format(response))
                    client.send(response.encode())
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    while True:
        portNo = input("Port? ")
        try:
            portNo = int(portNo) # Ensure port is valid.
            break
        except ValueError:
            pass

    ThreadedServer('',portNo).listen()
