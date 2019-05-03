# Stream Splitting Moving Target Defense
### Team Members
* Greg Baltzer
* Luke Zwenger
* Marvin Roe
* Alex Stara

## Executive Summary
Sending communications along a single channel poses certain risks to the data streams being sent. Data which runs via a single route is vulnerable to a variety of threats against confidentiality, integrity, and availability. These include the actions of human threat agents who may jeopardize any of these principles via intercepting, modifying, replaying, or outright discarding messages of importance. Also of concern is the potential threat by natural occurrences which may interrupt or delay services which remain on one communication channel at a time.

This project seeks to address these concerns by creating a point-to-point stream splitting mechanism for channeling data to protect it while in motion. This will take advantage of using multiple communication routes in parallel. As such, any potential attackers will either observe at most a meaningless fraction of the data being sent or be discouraged from attacking by the prospect of compromising multiple lines of communication. This will also provide hardening against infrastructure collapse as the system will be already prepared to swap to different data channels. Beyond the security and redundancy benefits, this project will also seek to increase bandwidth through the simultaneous use of multiple data links. A plethora of industries would reap the benefits of such software including national security, maritime telecommunication, healthcare, and more.

## Project Goals
The goal of this project is to develop and prototype an interface which may be deployed across organization locations. More specifically our goals are to provide an interface that will: 
 * Dynamically add and remove communication channels
 * Split streams between multiple data links
 * Ensure data encryption
 * Provide increased bandwidth
 * Test for communication quality
 
To better describe the desired workflow of the application, we have created activity diagrams linked below.
##### [Activity Diagrams](https://www.lucidchart.com/invitations/accept/ec184381-74cb-44d4-9053-03b1bd58b8c0)

## Project Methodology

Through our research thus far, we have discovered a number of techniques that may be used to achieve our project objectives. In deciding which path to take, one of our main considerations was the 
experience levels and expertise areas of the group. Seeing as none of us have experience in kernel level software development, we have decided that modifying MPTCP to our project objectives is not 
a direction that we feel comfortable with. Instead we have developed a user level application and created a proof of concept using Python. In order to achieve our goals
it may be advantageous to utilize an operating system that is specifically designed for application-level networking. We had considered the use of an operating system 
created by the MIT Parallel and Distributed Operating Systems Group called Exokernel. This operating system would allow a user level program to more directly interact with the networking 
interfaces and therefore increase performance. After deliberation however, we have decided that it would be better for the application to be OS independent to increase portability. 

Measuring success in terms of our project goals was one of the more complex tasks we had to tackle. When testing the performance capabilities of the stream splitting software we utilized ethernet and WiFi concurrently. Due to the fact that we were utilizing wireless communication, one of our major concerns was interference. All tests were conducted in an
environment where the signal to noise ratio (SNR) was 23 dB or more so that signal interference could be consiered negligible. We also conducted tests during non-peak hours to ensure that network congestion on the WAN was a non factor.

Throughout the project we utilized Git in order to manage the code base more effectively. We also collaborated on Trello, organizing all of our tasks and task assignment through that platform. All of the completed tasks from throughout the project can be found there.
Below, there are a number of architectural diagrams that follow the C4 model and describe the general structure of the proof of concept software. These diagrams were slightly fluid for the first couple weeks as the project 
progressed but we narrowed them down as development went on.

### Group Trello Board
https://trello.com/b/S4UXJ3fy/stream-splitting-mtd

## Results / Findings
At this point we can automatically enumerate all network interfaces on the host machine and initialize a thread for each interface that will listen for incoming connections.
For demonstration purposes, the client accepts a message as input and splits that string into individual words. It then sends each word in its own isolated packet via a random selection
of destination addresses associated with the host. Once the individual packets reach the destination, they're reassembled and sorted based on the order they were initially arranged. The following is a full list of 
the outcomes that have been achieved thus far:

* Successful data disassembly and reassembly.
* Random distribution of data segments between network interfaces.
* Error correction in the form of sorting the data back into its intended sequence.
* Multithreaded socket connections for simultaneous data reception.
* Automatic enumeration and initialization of network interfaces.
* OS independent operation.
* Handshake between hosts to enumerate and connect all available interfaces on each machine.
* Error detection/correction to reduce probablity of broken messages.
* Code maintainability.

### Architectural  Diagrams

#### [Level 1](https://www.lucidchart.com/invitations/accept/85a4fb6b-4c7b-486a-9fc6-2013971c1806)

#### [Level 2](https://www.lucidchart.com/invitations/accept/d02d1069-4ae7-4904-a2be-35bbf2d8029a)

#### [Level 3](https://www.lucidchart.com/invitations/accept/176e994b-ccd0-4253-b446-5c1b041db682)

#### [Level 4](https://www.lucidchart.com/documents/edit/b4d7d994-e823-49d3-ad65-f07a17aea869#)



## Install Instructions 
### Requirements
* Python 3.6.3

### Installation Instructions
* Download Python [here](https://www.python.org/downloads/).


### Getting started
Below you will find a list of instructions associated with getting started on this project. This includes, cloning the repository, running the application, and using the application. 
#### Cloning this repository:
Specific instructions on how to do this on each operating system can be found [here](https://help.github.com/en/articles/cloning-a-repository).

#### Running the application:
##### Windows
* Open Command line:   Start menu -> Run  and type cmd
* Type:   ```C:\{path to your python interpreter}\python.exe C:\{path to your code}\MultiPathServer.py```
* Type:   ```C:\{path to your python interpreter}\python.exe C:\{path to your code}\MultiPathClient.py```
* Or if your system is configured correctly, you can drag and drop your scripts from Explorer onto the Command Line window and press enter.

##### Mac OS X
* Open Command line: Finder -> Go menu -> Applications -> Terminal
* Type: ```python ~/{path to your code}/MultiPathServer.py```
* Type: ```python ~/{path to your code}/MultiPathClient.py```

##### Linux
* Open a command prompt
* Type: ```python ~/{path to your code}/MultiPathServer.py```
* Type: ```python ~/{path to your code}/MultiPathClient.py```

#### Using the application
* Once the program is running the user will be prompted for an ip address with which to connect. The user may enter any of the destination's ip addresses and all the available interfaces will be connected. 
* For ease of use, the ports have been hard coded but that can be undone quite simply by uncommenting the following lines ```input("Listening Port? ")``` and ```input("Destination Port? ")```
* Be sure that the ```MultiPathServer``` is running and listening before you attempt to connect ```MultiPathClient```.
* Once the connections are made, you can send data from the client

#### Full project documentation can be found on our group github:
https://github.com/xoBalt/Capstone-Stream-Splitting-MTD