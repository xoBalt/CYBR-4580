import socket
import threading
import pickle
import packet
import ThreadedSession
import SessionManager
import ifaddr
import time
import random

sessions = []
sem_lock = threading.Lock()
valid_adapters = []

def validate_ip(s):
    #if we can connect to the ip address and it's not the loopback interface return true
    try:
        #check if it follows a valid pattern for ip
        a = str(s).split('.')
        if len(a) != 4:
            raise socket.error
        for x in a:
            if not x.isdigit():
                raise socket.error
            i = int(x)
            if i < 0 or i > 255:
                raise socket.error

        socket.inet_aton(str(s))
        if str(s).find('127.0.0.1') == 0:
            raise socket.error
    except socket.error:
        return False

    return True

if __name__ == "__main__":

    #this method allows us to sort by sequence number
    def sortbysequence(val):
        return val.sequence_number

    #get all network adapters
    adapters = ifaddr.get_adapters()

    valid = False
    #Print out all available network interfaces
    for adapter in adapters:
        valid = False
        #Don't use the default loopback interfaces
        index = 0
        for ip in adapter.ips:
            if validate_ip(ip.ip):
                valid = True
            else:
                del(adapter.ips[index])
            index+=1

        if valid:
            #add the valid interfaces
            valid_adapters.append(adapter)

    for adapter in valid_adapters:
        print(adapter.nice_name)
        print("   %s" % (adapter.ips[0].ip))

    while True:
        #Each NIC operates on the same port (this isn't necessary but just allows for faster testing)
        local_portNo = 1111
            #input("Listening Port? ")

        try:
            local_portNo = int(local_portNo) # Ensure port is valid.
            break
        except ValueError:
            pass

    while True:
        #Each NIC operates on the same port (this isn't necessary but just allows for faster testing)
        dest_portNo = 1234
            #input("Destination Port? ")
        try:
            dest_portNo = int(dest_portNo) # Ensure port is valid.
            break
        except ValueError:
            pass
    manager = SessionManager.SessionManager([],valid_adapters, local_portNo, dest_portNo, sem_lock)

    manager.initialize_threads(valid_adapters)
    #This loop prints the contents of the data that has been recieved every 5 seconds then clears it.
    while True:
        ip = input("Enter ip address to connect to or type \"listen\" to wait for incoming connections: ")

        #Wait for incoming connection
        if(str(ip) == "listen"):
            while True:
                complete = False
                time.sleep(2)
                print(".")
                for datum in manager.data_array:
                    if datum.data == "78342341":
                        manager.handshake_recv()
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        sock.connect((manager.dest_addr[0].ips[0].ip, dest_portNo))
                        handshake_packet = packet.packet(socket.AF_INET, ip, 1, 2048, "78342341", None, None)
                        sock.send(pickle.dumps(handshake_packet))
                        manager.handshake_send(sock)
                        print("Sent to: "+str(manager.dest_addr[0].ips[0].ip))
                        complete = True
                        break;
                    else:
                        manager.data_array.clear()
                if complete:
                    break;
            if complete:
                manager.data_array.clear()
                break;
        #Actively seek connection
        else:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((ip, dest_portNo))
                handshake_packet = packet.packet(socket.AF_INET, ip, 1, 2048, "78342341", None, None)
                sock.send(pickle.dumps(handshake_packet))
                manager.handshake_send(sock)
                while True:
                    complete = False
                    time.sleep(2)
                    print(".")
                    for datum in manager.data_array:
                        if datum.data == "78342341":
                            manager.handshake_recv()
                            complete = True
                    if complete:
                        break
            except socket.error:
                print("Failed to connect, please retry...")
                print(socket.error)
        break

    print("Handshake complete.")



    while True:
        time.sleep(5)
        if(manager.data_array):
            manager.data_array.sort(key= sortbysequence)
            for datum in manager.data_array:
                print(datum.data)

            manager.data_array.clear()

