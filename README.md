# Stream Splitting Moving Target Defense
### Team Members
* Greg Baltzer
* Luke Zwenger
* Marvin Roe
* Alex Stara

## Executive Summary
Sending communications along a single channel poses certain risks to the data streams being sent. Data which runs via a single route is vulnerable to a variety of threats against confidentiality, integrity, and availability. These include the actions of human threat agents who may jeopardize any of these principles via intercepting, modifying, replaying, or outright discarding messages of importance. Also of concern is the potential threat by natural occurrences which may interrupt or delay services which remain on one communication channel at a time.

This project seeks to address these concerns by creating a point-to-point stream splitting mechanism for channeling data to protect it while in motion. This will take advantage of using multiple communication routes in parallel. As such, any potential attackers will either observe at most a meaningless fraction of the data being sent or be discouraged from attacking by the prospect of compromising multiple lines of communication. This will also provide hardening against infrastructure collapse as the system will be already prepared to swap to different data channels. Beyond the security and redundancy benefits, this project will also seek to increase bandwidth through the simultaneous use of multiple data links. A plethora of industries would reap the benefits of such software including national security, maritime telecommunication, healthcare, and more.

The goal of this project is to develop and prototype an interface which may be deployed across organization locations. More specifically our goals are to provide an interface that will: 
 * Dynamically add and remove communication channels
 * Split streams between multiple data links
 * Ensure data encryption
 * Provide increased bandwidth
 * Test for communication quality


## Proposed Project Timeline
 ![alt text](https://github.com/xoBalt/Capstone-Stream-Splitting-MTD/blob/master/Gnatt%20Chart.PNG)

## Project-oriented Risk List

|Risk name (value)  | Impact     | Likelihood | Description |
|-------------------|------------|------------|-------------|
|Loss of a team member. (20)|6|2|The members job or family prevents them from completing the course. That members responsibilities will be divided amongst the remaining members.|
|Loss of communication with our Sponsor. (10)|4|1|The sponsor is assigned other obligations that take them away from this project. The team will continue with the information already supplied by the sponsor and will clearly outline any assumptions made by the team for the project.|
|Team members having other scheduling engagements. (8)|1|6| This Risk might happen a few times during the research. The team has numerous ways of communicating. This Risk might happen, but it will have no impact on the project.|
|Not having the correct technical skillset. (24)|5|6|If a team member or the team has no prior experience with the research. There will be a few times this might happen, but as a team we will gather the needed information and accomplish our tasks.|
|Programing failure (25)|8|4|The project can not proceed because of a programing failure. This project will be written using Python and most members have a good knowledge base of Python. There might be a point where the team will need to reach out and find better ways to write aspects of the code.|
Loss of research (45)|10|2|A team member accidentally deletes a file. The team is working with a few different tools that keep saved work from being destroyed. Each team member will need to keep this practice consistent throughout the project, to ensure a minimal loss of data.|
|Failure to deliver a final project (50)|10|1|The team fails at any research. The team is excited and capable of accomplishing the tasks ahead. Each team member will need to be active throughout the project. We as a team believe that we can deliver a sound scholarly project.|





## Application Requirements

### User Stories
1. As a **network engineer**, I want all of my data links to be used concurrently to maximize bandwidth.

* Acceptance criteria: The stream splitting daemon should intelligently divide streams across links utilizing their bandwidth efficiently.

2. As a **network engineer**, I want to be able to dynamically add and remove data links.

* Acceptance criteria: The stream splitting daemon should dynacially add and remove links based on availability.

3. As a **network engineer**, I want my connection to stay up with minimal interruption, even if one of my links drops.

* Acceptance criteria: If a link loses bandwidth or goes down, the stream splitting daemon should respond automatically by limiting or stopping traffic through that link.


4. As a **network engineer**, I want my split information stream to transmit and reassemble data at a consistent rate comparable with standard network protocols.

* Acceptance criteria: The transmission speed and integrity of data falls within 10% of control tests with TCP.


5. As a **security engineer**, I want all of my data to be encrypted while in motion.

* Acceptance criteria: The data will be encrypted prior to splitting and transporting.


6. As a **security engineer**, I want my data to be randomly split between links to increase obfuscation.

* Acceptance criteria: Data will be split randomly between links. 

#### [Activity Diagram](https://www.lucidchart.com/invitations/accept/ec184381-74cb-44d4-9053-03b1bd58b8c0)

##  Project Methodology

Through our research thus far, we have discovered a number of techniques that may be used to achieve our project objectives. In deciding which path to take, one of our main considerations was the 
experience levels and expertise areas of the group. Seeing as none of us have experience in kernel level software development, we have decided that modifying MPTCP to our project objectives is not 
a direction that we feel comfortable with. Instead we plan on developing a user level application and creating a proof of concept most likely using Python. In order to achieve our goals
it may be advantageous to utilize an operating system that is specifically designed for application-level networking. We are currently considering the use of an operating system 
created by the MIT Parallel and Distributed Operating Systems Group called Exokernel. This operating system would allow our user level program to more directly interact with the networking 
interfaces and therefore increase performance. If we plan to use Exokernel, the application development will most likely have to be done in C but we are still researching this.

Measuring success in terms of our project goals will be one of the more complex tasks we complete. When testing the performance capabilities of the stream splitting software we plan to utilize ethernet and WiFi concurrently. Due to the fact that we will be utilizing wireless communication, one major concern is interference. All tests will be conducted in an
environment where the signal to noise ratio (SNR) is 23 dB or more so that signal interference could be consiered negligible. We will also be conducting tests during non-peak hours to ensure that network congestion on the WAN is a non factor. Measurements will be made not only in terms of aggregate bandwidth available, but also in latency and error frequency.

Throughout the project we will be utilizing Git in order to manage the code base more effectively. We will also be collaborating with Trello and organizing all of our tasks and task assignment through that platform. Our first sprint plan can be found on that Trello board. 
Below, there are a number of architectural diagrams that follow the C4 model and describe the general structure of the proof of concept software. These diagrams will be slightly fluid for the first couple weeks as the project 
progresses and we narrow down a more specific path for development.

### Architectural  Diagrams

#### [Level 1](https://www.lucidchart.com/invitations/accept/85a4fb6b-4c7b-486a-9fc6-2013971c1806)


#### [Level 2](https://www.lucidchart.com/invitations/accept/d02d1069-4ae7-4904-a2be-35bbf2d8029a)


#### [Level 3](https://www.lucidchart.com/invitations/accept/176e994b-ccd0-4253-b446-5c1b041db682)



## Resource Requirements
|Resource  | Dr. Hale needed?     | Investigating Team Member | Description |
|-------------------|------------|------------|-------------|
|Python|No|All|Using Python is a programming language to complete the project.|
|Criss Library|No|All|Accessing the Databases and Digital Commons at the Criss Library.|
|Raspberry Pi| No| Greg| Utilizing a Raspberry Pi in order to simulate a client connection more effectively.|
|Supporting Research|No|Greg|Existing research and software that performs a similar job and can be utilized for our purposes.|

## Group Trello Board
https://trello.com/b/S4UXJ3fy/stream-splitting-mtd

# Progress Report (3/28/2019)
## Overview
The majority of the past few weeks has been focused on research and planning for the stream splitting application.
Our research has helped both with understanding the scope of our project and in understanding how the Python libraries handle different aspects of the process.
The group has had a number meetings to keep honing our scope of the project so that we will be able to deliver a more complete deliverable to our sponsor.
Besides research, we have also implemented portions of functionality that we plan to implement in the final product. This includes ```MultiPathServer.py``` and ```MultiPathClient.py``` which will create threads for each network interface
on the machine and listen for incoming connections. The client can then send data to all of those interfaces simultaneously and it will be reassembled and sorted when received. 

## Outcomes
At this point we can automatically enumerate all network interfaces on the host machine and initialize a thread for each interface that will listen for incoming connections.
For demonstration purposes, the client accepts a message as input and splits that string into individual words. It then sends each word in its own isolated packet via a random selection
of destination addresses. Once the individual packets reach the destination, they're reassembled and sorted based on the order they were initially arranged.

* Successful data disassembly and reassembly.
* Error correction in the form of sorting the data back into it s intended sequence.
* Multithreaded socket connections for simultaneous data reception.
* Automatic enumeration and initialization of network interfaces.

## Hinderances
There have been a number of hindrances during our first sprint that were very low likelihood and unfortunately high cost. The primary cost originated from the loss of a team member.
There were also a couple of team members who experienced flooding in their homes which meant significantly decreased productivity for those members.
## Ongoing Risks
|Risk name (value)  | Impact     | Likelihood | Description |
|-------------------|------------|------------|-------------|
|Loss of a team member. (20)|10|2|The members job or family prevents them from completing the course. That members responsibilities will be divided amongst the remaining members. Since we have already lost one member, this risk's impact has increased.|
|Loss of communication with our Sponsor. (10)|4|1|The sponsor is assigned other obligations that take them away from this project. The team will continue with the information already supplied by the sponsor and will clearly outline any assumptions made by the team for the project. Thus far the sponsor has been very responsive and communication has not been an issue.|
|Team members having other scheduling engagements. (8)|1|4| Now that the team is in the routine of our schedule this semester, the probability of scheduling conflicts has decreased.|
|Not having the correct technical skillset. (24)|5|4|Thus far we have not had any issues in this area and through our research we have been able to decrease the likelihood of this risk. |
|Programming failure (25)|8|2|We have already established that much of the intended functionality of the application is feasible with Python, therefore the likelihood of this risk has decreased.|
|Loss of research (45)|10|1|The group is currently utilizing git to keep track of version history and we each have local backups of all our work up to this point. The likelihood of this risk has been decreased|
|Failure to deliver a final project (50)|10|1|The team fails at any research. The team is excited and capable of accomplishing the tasks ahead. Each team member will need to be active throughout the project. We as a team believe that we can deliver a sound scholarly project.|
|Natural Disaster|15|2|Tornado season is rapidly approaching and mother nature has already proved to be a risk in this project so it only seems appropriate to include this in our risk assessment.|







