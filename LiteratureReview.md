# Literature Review

The following is a collection of past research project that were conducted on stream splitting moving target defense. There are a number of different sources from unique authors that offer a lot of background knowledge in the area of stream splitting. The applications of stream splitting specifically for moving target defense are not quite as thoroughly researched, which provides an interesting opportunity.

1. ***A Measurement-based Study of MultiPath TCP Performance over Wireless Networks*** Chen, Y., Lim, Y., Gibbens, R. J., Nahum, E. M., Khalili, R., & Towsley, D. (2013). Retrieved February 10, 2019, from http://conferences.sigcomm.org/imc/2013/papers/imc231-chenA.pdf

This paper focused primarily on the effects of stream splitting between WiFi and LTE on mobile devices. The researchers implemented MPTCP in order to perform the stream splitting in various different scenarios. They found that MPTCP is robust in acheiving performance at least close to the best single-path performance, across a wide range of network environments. For large transfers, performance was better than the best single path, except in cases with poor cellular networks. What this means is that if they were attempting to download a large file, MPTCP provided significantly better performance than just using one link at a time. That being said, they did discover a major concern with MPTCP where different data links had very different latency. For example, a cell phone stream splitting between WiFi and 3G did not experience significant performance increases due to the fact that the reassembly process was hindered by waiting around for the packets that were tranfered via 3G.

In our case we will not be utilizing cellular networks, so we should not experience this issue due to the fact that WiFi vs Ethernet latency is much less significant than that of 3G. 


2. ***Enhancement of Packet Reordering in a Mobile Stream Control Transmission Protocol for a Heterogeneous Wireless Network Vertical Handover***
Hamza, B. J., Chee Kyun Ng, Noordin, N. K., Rasid, M. F. A., Ismail, A., & Tahir, Y. H. (2010). Enhancement of packet reordering in a mobile stream control transmission protocol for a heterogeneous wireless network vertical handover. Journal of High Speed Networks, 17(3), 163–173. https://doi-org.leo.lib.unomaha.edu/10.3233/JHS-2010-0338

This paper dates back to several years ago and describes a means of normalizing communications between mobile networks and wireless local area networks. While the technology mentioned in the paper is no longer new (for instance, the integration of 3G networks is not as fresh a research area), the researchers did encounter a similar problem to ours. As a transceiver moved between cellular towers and data was transferred between different types of communication networks, the data would have to be sent in chunks across distinct pathways.

Therefore they proposed a structure to perform buffering and only send data when a connection was available. This also handled error correction in ascertaining that all chunks were received. We might be able to use a similar concept to their proposed structure in handling incoming packets at the receiving end of split streams.


3. ***Stream-based aggregation of unreliable heterogeneous network links***
 M. Zielinski, “Stream-based aggregation of unreliable heterogeneous ´
network links,” arXiv preprint arXiv:1509.08222, 2015,Retrieved February 13, 2019, from https://arxiv.org/pdf/1509.08222.pdf
  
  
This paper talks about the uses of using MTCP while maximizing bandwidth and minimizing latency.It goes into detail about using a modified earliest delivery path first scheduling protocol. The use of an earliest delivery path protocol not only allows for the use of MTCP, but also allows better bandwidth to be achieved.this can be achieved in theory if not data streams go down.If a data stream does go down this packet scheduling protocol has a hard time making up that error.

After that it goes into a problem for MTCP called TCP over TCP meltdown.This occurs when TCP congestion control from two layer interfere badly.The work around they provided was to terminate TCP connections from the sender and receiver and send raw TCP stream.In addition to sending raw TCP stream there needs to be an addition reorder buffer and addition flow control needs to be add to make sure that the timeout of the packets is not a problem.This paper allows use not only to look into to a packet scheduler but also gives us to a problem we would have ran into if we hadn't used one.


4. ***MultiPath TCP: From Theory to Practice***
Z. Afzal and S. Lindskog, Multipath TCP IDS Evasion and Mitigation.
Cham: Springer International Publishing, 2015, pp. 265–282,Retrieved February 13, 2019, from https://link.springer.com/content/pdf/10.1007%2F978-3-642-20757-0_35.pdf

This paper gives a nice general overview of MTCP.The main purpose in our eyes is the implementation of MTCP that they go over. In this paper they go over a kernel implementation of MTCP, as of right now we have no intentions of going that far deep but instead would rather implement this in the application layer. In the paper's implementation they use a Multi-path control block to allow the start and stop of new and old TCP streams.They also use this control block to gather data from slave blocks that run on the tcp data streams and evaluate when they should be stopped.The big advantage for this is it allows for an easy way to monitor bandwidth through the streams and if a data stream goes down the control block can easily make a new one.

5. ***Fast and Flexible Application-Level Networking on Exokernel Systems.*** Ganger, G. R., Engler, D. R., & Pinckney, T. (2002). Retrieved February 12, 2019, from https://web.stanford.edu/~engler/exo-tocs.pdf

Since our group plans on developing software at the application level instead of the kernel level, it seemed fitting to research potential platforms and projects that have delved into this area before. This paper dates back to 2002 and focuses on the requirements and performance improvements for networking at the application level. The researchers found that specialized applications can be up to eight times faster than socket-based versions. The key challenges in implementing application-level networking are securely multiplexing multiple applications onto a single networking interface, and doing so while efficiently supporting useful network services. Due to the fact that this paper is 84 pages long, I have not made it through the entire thing but initially it is easy to see that we can learn a lot from their efforts. Essentially this gives us a head start in understanding our development path for the stream splitting software.

6. ***Performance Analysis of Data Transfer Protocols over Space Communications***
T. De Cola and M. Marchese, "Performance analysis of data transfer protocols over space communications," in IEEE Transactions on Aerospace and Electronic Systems, vol. 41, no. 4, pp. 1200-1223, Oct. 2005.
doi: 10.1109/TAES.2005.1561883

This paper discusses difficulties in transmitting information between ground stations and satellites in orbit. While we're focusing on cabled and local wireless signals, certain insights from the research can also help our project as plans had to be made for dealing with packet delay or loss. Additionally, a branch of the proposed approaches for coordinating packet transfer was to integrate the assurance properties of TCP into the application layer, which is part of our project's direction. A number of references are noted for both the application layer integration and using an interface as a specialized connection-splitting gateway, which could prove fruitful for further research.


#### Keyword Definitions
* **MultiPath TCP (MPTCP)** -  An effort towards enabling the simultaneous use of several IP-addresses/interfaces by a modification of 
TCP that presents a regular TCP interface to applications, while in fact spreading data across several subflows.

* **Application-level networking** - An effort towards enabling individual applicions to interact more directly with network interfaces and improve customizability of application specific network communications.

