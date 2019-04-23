import socket
import threading
import pickle
import packet
import ThreadedSession
import ifaddr
import time

sessioncount = 0
sessions = []
array = []
sem_lock = threading.Lock()

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
        sessions.append(ThreadedSession(adapter.ips[-1].ip,portNo))
        #Create a new thread for each NIC
        threading.Thread(target = sessions[sessioncount].listen,args = ()).start()
        sessioncount+=1
    #This loop prints the contents of the data that has been recieved every 5 seconds then clears it.
    while True:
        time.sleep(5)
        print("...")
        array.sort(key= sortbysequence)
        for datum in array:
            print(datum.data)
        array.clear()