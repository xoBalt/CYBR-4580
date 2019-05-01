# Progress Report (5/2/2019)
## Overview
For milestone 3, the primary focus area was in code development and testing. Throughout this sprint we prioritized areas of the application
in which we believe have the most impact on the customer. Specifically we focused on, automating the connection process, 
ensuring data integrity, error detection/correction, and latency. 

As mentioned in our previous progress report, over the past few weeks we have been creating incremental pieces of code as 
a proof of concept before incorporating them into the final product. We have successfuly incorporated every proof of concept feature 
into our final product  ```MultiPathServer.py``` and ```MultiPathClient.py```. Fundamentally these two applications function in the same way
but for demonstration purposes we have included them as two seperate files. One which is intended to be the sender of data (```client```) and one which is intended to 
be the reciever (```server```). 
## Outcomes
At this point we can automatically enumerate all network interfaces on both host machines and initialize a thread for each interface that will listen for incoming connections and send data to outbound connections.
For demonstration purposes, the client accepts a message as input and splits that string into individual words. It then sends each word in its own isolated packet via a random selection
of both source and destination addresses associated with the host. Once the individual packets reach the destination, they're reassembled and sorted based on the order they were initially arranged. The following is a full list of 
the outcomes that have been achieved thus far:

* Successful data disassembly and reassembly.
* Random distribution of data segments between network interfaces.
* Error correction in the form of sorting the data back into its intended sequence.
* Multithreaded socket connections for simultaneous data reception.
* Automatic enumeration and initialization of network interfaces.
* OS independent operation.
* **Handshake between hosts to enumerate and connect all available interfaces on each machine.**
* **Error detection/correction to reduce probablity of broken messages.**
* **Automatic failover if an interface fails.**

## Hinderances
As we ventured into more advanced topics in Python, much of our prerequisite knowledge was put to the test. As was noted in milestone 1, the 
group's expereince in software development with Python was minimal so features such as the handshake took some extra time to get right. 
The necessary environment to test multi-interface network communications also presented logistical challenges. 