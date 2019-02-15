# Literature Review

The following is a collection of past research project that were conducted on stream splitting moving target defense. There are a number of different
sources from unique authors that offer a lot of background knowledge in the area of stream splitting. The applications of stream splitting
specifically for moving target defense are not quite as thouroughly researched which provides an interesting opportunity.

1. "***A Measurement-based Study of MultiPath TCP
Performance over Wireless Networks***"

I will put my summary of this paper here.


#### Keyword Definitions

* **MultiPath TCP (MPTCP)** -  An effort towards enabling the simultaneous use of several IP-addresses/interfaces by a modification of 
TCP that presents a regular TCP interface to applications, while in fact spreading data across several subflows.


2. "***Enhancement of Packet Reordering in a Mobile Stream Control Transmission Protocol for a Heterogeneous Wireless Network Vertical Handover***
Hamza, B. J., Chee Kyun Ng, Noordin, N. K., Rasid, M. F. A., Ismail, A., & Tahir, Y. H. (2010). Enhancement of packet reordering in a mobile stream control transmission protocol for a heterogeneous wireless network vertical handover. Journal of High Speed Networks, 17(3), 163–173. https://doi-org.leo.lib.unomaha.edu/10.3233/JHS-2010-0338

This paper dates back to several years ago and describes a means of normalizing communications between mobile networks and wireless local area networks. While the technology mentioned in the paper is no longer new (for instance, the integration of 3G networks is not as fresh a research area), the researchers did encounter a similar problem to ours. As a transceiver moved between cellular towers and data was transferred between different types of communication networks, the data would have to be sent in chunks across distinct pathways.

Therefore they proposed a structure to perform buffering and only send data when a connection was available. This also handled error correction in ascertaining that all chunks were received. We might be able to use a similar concept to their proposed structure in handling incoming packets at the receiving end of split streams.


3. "***Stream-based aggregation of unreliable heterogeneous network links***"

https://arxiv.org/pdf/1509.08222.pdf
Working on paragraphs right now



4. "***MultiPath TCP: From Theory to Practice***"

https://link.springer.com/content/pdf/10.1007%2F978-3-642-20757-0_35.pdf
Working on paragraphs right now

#### Keyword Definitions

* ** Stream Control Transmission Protocol (SCTP)** -  was designed with multihoming in mind and supports fail-over
