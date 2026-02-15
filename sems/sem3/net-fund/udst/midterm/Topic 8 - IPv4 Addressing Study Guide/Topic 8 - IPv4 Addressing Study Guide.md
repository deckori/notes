## Topic 8 - IPv4 Addressing Study Guide Study Guide

1.  How many bits are in an IPv4 address, and how are they grouped? (S3)

-   Each address contains 32 bits, divided into four octets.

2.  IPv4 addresses have two parts; what are they, and what process is used identify them? (S8,9)

-   Network portion and a host portion.
-   A subnet mask is used to determine the network and host portions in a process called ANDing.

3.  What is the prefix length? (S10)

-   The number of bits set to 1 in the subnet mask
-   It is written in "slash notation"

4.  What operation is used to identify the network address? (S11)

-   To identify the network address, the host IPv4 address is logically ANDed, bit by bit, with the subnet mask.

5.  How can you tell if an IPv4 address is a host, network or broadcast address? (S6)

-   Network address: all host bits set to 0.
-   Host addresses: host bits range from ("Network address" + 1) to ("Broadcast address" - 1)
-   Broadcast address: all host bits set to 1.

6.  Define the following types of network addresses. (S13-15)

<!-- -->

a)  Unicast
    -   Sending a packet to one destination IP address.
b)  Broadcast
    -   Sending a packet to all IP addresses in the network.
c)  Multicast
    -   Sending a packet to a multicast address group.

<!-- -->

7.  Compare the public and private IPv4 addresses. (S16)

-   Public IPv4 addresses are globally routed between internet service provider (ISP) routers.
-   Private addresses are not globally routable.

8.  What are the Private address ranges? (S16)

| Network Address and Prefix | RFC 1918 Private Address Range |
|----------------------------|--------------------------------|
| 10.0.0.0/8                 | 10.0.0.0 - 10.255.255.255      |
| 172.16.0.0/12              | 172.16.0.0 - 172.31.255.255    |
| 192.168.0.0/16             | 192.168.0.0 - 192.168.255.255  |

9.  What does NAT stand for, and what is its function? (S17)

-   Network Address Translation (NAT) translates private IPv4 addresses to public IPv4 addresses.

10. What are the Loopback addresses and how are they used? (S18)

-   127.0.0.0/8 (127.0.0.1 to 127.255.255.254)
-   Commonly identified as only 127.0.0.1
-   Used on a host to test if TCP/IP is operational.

11. Complete the following table for the Classful Addressing. (12) (S19)

| Class | Default Subnet Mask/Prefix | Network Address Range | Number of<br>Hosts/Network |
|----|----|----|----|
| A | /8 | 0.0.0.0/8 to 127.0.0.0/8 | 16,777,214 |
| B | /16 | 128.0.0.0 /16 - 191.255.0.0 /16 | 65,534 |
| C | /24 | 192.0.0.0 /24 –223.255.255.0 /24 | 254 |

12. Compare switches and routers with respect to broadcast propagation. (S21)

-   Switches propagate broadcasts out all interfaces except the interface on which it was received.
-   Routers do not propagate broadcasts.

13. Explain the problem with large broadcast domains and how it can be resolved. (S22)

-   large broadcast domain is that these hosts can generate excessive broadcasts and negatively affect the network.
-   The solution is to reduce the size of the network to create smaller broadcast domains in a process called subnetting.

14. List three reasons for segmenting networks. (S23)

-   To reduces overall network traffic and improves network performance.
-   To implement security policies between subnets.
-   To group the users according to location, group/function, or device type.

15. Covert the following numbers: (S5-7)

-   10110 (Decimal) into Binary
-   101010012 (Binary) into Decimal

16. Write the subnet mask next to the following addresses. (S10)

|                 |     |
|-----------------|-----|
| 192.168.5.53/22 |     |
| 192.168.2.44/26 |     |
| 192.168.2.44/28 |     |

17. Write the prefix length next to the following subnet masks. (S10)

|                 |     |
|-----------------|-----|
| 255.255.255.128 |     |
| 255.255.252.0   |     |
| 255.255.248.0   |     |

18.Determine the address types and write the results in column 2. (S11-12)

#### Example 1

192.168.1.32/27 → Network

$$ 27 = 24 + 3 $$

The first 3 octets are common to host, broadcast, and network addresses.

$$ 32 = 00100000 $$ Note: $32$ is a *network* octet.

$$ 63 = 11100000 $$ Note: $63$ is a *broadcast* octet.

\begin{aligned}
N &= 192.168.1.32 \\
B &= 192.168.1.63
\end{aligned}

$$ \text{First address} = N + 1 = 192.168.1.33 $$ $$ \text{Last address} = B - 1 = 192.168.1.62 $$

------------------------------------------------------------------------

#### Example 2

200.25.36.200/25

$$ /25 \implies \text{Host bits} = 32 - 25 = 7 $$

The first 3 octets are common to host, broadcast, and network addresses.

-   Last octet of:
    a)  given ip address: 200 = 11001000
    b)  subnet mask: 10000000
    c)  ANDing a) and b) to get N's octet: $(10000000)_2 = (128)_{ 10 }$
    d)  Changing all host bits in c) to 1 to get B's octet: $(11111111)_2 = (255)_{ 10 }$

\begin{aligned}
N &= 200.25.36.128 \\
B &= 200.25.36.255
\end{aligned}

The given address is a host address

------------------------------------------------------------------------

#### Example 3

172.16.55.71/29

$$ /29 \implies \text{Host bits} = 32 - 29 = 3 $$

The first 3 octets are common to host, broadcast, and network addresses.

-   Last octet of:
    a)   given ip address: 71 = 01000111
    b)   subnet mask: 11111000
    c)   ANDing a) and b) to get N's octet: $(01000000)_2 = (64)_{ 10 }$
    d)   Changing all host bits in c) to 1 to get B's octet: $(01000111)_2 = (71)_{ 10 }$

\begin{aligned}
N &= 172.16.55.64 \\
B &= 172.16.55.71
\end{aligned}

The given address is a broadcast address

------------------------------------------------------------------------

#### Example 4

10.2.3.75/28
