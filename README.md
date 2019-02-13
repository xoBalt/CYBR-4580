# CYBR-4580
Repository for the capstone project. This is where we will compose our "proposal". This is all markdown so [here](https://www.markdownguide.org/cheat-sheet/) is a link to a helpful cheat sheet that you can use while writing your portion of the proposal. 

## Executive Summary
Here lies the executive summary

## Proposed Project Timeline
Here is a fancy gantt chart

## Project-oriented Risk List

|Risk name (value)  | Impact     | Likelihood | Description |
|-------------------|------------|------------|-------------|
|Loss of a team member. (20)|6|2|The members job or family prevents them from completing the course. That members responsibilities will be divided amongst the remaining members.|
|Loss of communication with our Sponsor. (10)|4|1|The sponsor is assigned other obligations that take them away from this project. The team will continue with the information already supplied by the sponsor and will clearly outline any assumptions made by the team for the project.|
|Team members having other scheduling engagements. (8)|1|6| This Risk might happen a few times during the research. The team has numerous ways of communicating. This Risk might happen, but it will have no impact on the project.|
|Not having the correct technical skillset. (24)|5|6|If a team member or the team has no prior experience with the research. There will be a few times this might happen, but as a team we will gather the needed information and accomplish our tasks.|
|Programing failure (25)|8|4|The project can not proceed because of a programing failure. This project will be written using Python and most members have a good knowledge base of Python. There might be a point where the team will need to reach out and find better ways to wright aspects of the code.|
Loss of research (45)|10|2|A team member accidentally deletes a file. The team is working with a few different tools that keep saved work from being destroyed. Each team member will need to keep this practice consistent throughout the project, to ensure a minimal loss of data.|
|Failure to deliver a final project (50)|10|1|The team fails at any research. The team is excited and capable of accomplishing the tasks ahead. Each team member will need to be active throughout the project. We as a team believe that we can deliver a sound scholarly project.|





## Application Requirements

### User Stories
1. As a **network engineer**, I want all of my data links to be used concurrently to maximize bandwidth.

* Acceptance criteria: The stream splitting daemon should intelligently divide streams across links utilizing their bandwidth efficiently.


2. As a **network engineer**, I want my connection to stay up with minimal interruption, even if one of my links drops.

* Acceptance criteria: If a link loses bandwidth or goes down, the stream splitting daemon should respond automatically by limiting or stopping traffic through that link.


3. As a **network engineer**, I want my split information stream to transmit and reassemble data at a consistent rate comparable with standard network protocols.

* Acceptance criteria: The transmission speed and integrity of data falls within 10% of control tests with TCP.


4. As a **security engineer**, I want all of my data to be encrypted while in motion.

* Acceptance criteria: The data will be encrypted prior to splitting and transporting.


5. As a **security engineer**, I want my data to be randomly split between links to increase obfuscation.

* Acceptance criteria: Data will be split randomly between links. 


### C4 Model Diagrams

#### Level 1
![alt text](https://github.com/xoBalt/Capstone-Stream-Splitting-MTD/blob/master/Level%201%20Diagram.png)

#### Level 2
![alt text](https://github.com/xoBalt/Capstone-Stream-Splitting-MTD/blob/master/Level%202%20diagram.png)



## Resource Requirements
|Resource  | Dr. Hale needed?     | Investigating Team Member | Description |
|-------------------|------------|------------|-------------|
|Python|No|All|Using Python is a programming language to complete the project.|
|Criss Library|No|All|Accessing the Databases and Digital Commons at the Criss Library.|
|Raspberry Pi| No| Greg| Utilizing a Raspberry Pi in order to simulate a client connection more effectively.|
|Supporting Research|No|Greg|Existing research and software that performs a similar job and can be utilized for our purposes.

