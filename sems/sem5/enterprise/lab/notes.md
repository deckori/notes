To prevent issues with connectivity:

```
(config) no ip domain lookup
```


## Single Area OSPF

### Basic OSPF config

```
(config)#router ospf <process num>
(config-router)#router-id <ID>
```

Next, we should specify which interfaces will participate in the OSPF process. They can identified via their network pool:

```
(config-router)#network <ip network address> <wildcard mask> area <num>
```

Or the IP of the interface:

```
(config-router)#network <interface IP address> 0.0.0.0 area <num>
```

Or by going to each interface:

```
(config)#int <int ID>
(config-if)#ip ospf <process num> area <num>
```

### Optimizations

```
(config)#router ospf <process ID>
(config-route)#passive-interface <interface ID>     (Note: Can be run as many times as needed)
(config-route)#default-information originate    (Note: Static route propagation)
```

```
(config)#router ospf <process ID>
(config-route)#auto-cost reference-bandwidth <Reference Mbps like 10000 for 10Gb network or 1000 for 1Gb network>
#clear ip ospf process    (Note: to restart OSPF to implement above config)
```

```
(config)#int <int ID>
(config-if)#ip ospf network point-to-point
(config-if)#ip ospf cost <num>    (Note: used to manually set a cost to an interface)
(config-if)#ip ospf priority <0-255>   (Note: to control DR/BDR election)
(config-if)#ip ospf hello-interval <seconds>
(config-if)#ip ospf dead-interval <seconds>   (Note: not necessary as it is auto modified to be 4x the hello-interval. needed for documentation only)
```

### Testing:

```
#sh run | section ospf
```

## ACLs

### Standard ACLs

Standard ACL

```
Router(config)# access-list <1-99> {permit|deny} { <source-ip> <wildcard-mask> | host <source-ip> | any }
```

Named Standard ACL

```
Router(config)# ip access-list standard <ACL-NAME>
Router(config-std-nacl)# [sequence-number] {permit|deny} { <source-ip> <wildcard-mask> | host <source-ip> | any }
Router(config-std-nacl)# no [sequence-number]
```

### Extended ACLs

Extended ACL

```
(config)# access-list <100-199> {permit|deny} <protocol> { <source-ip> <wildcard-mask> | host <source-ip> | any } [operator <port>] { <dest-ip> <wildcard-mask> | host <dest-ip> | any } [operator <port>] [established]
(config)# access-list <100-199> permit ip any any
```

Named Extended ACL

```
(config)# ip access-list extended <ACL-NAME>
(config-ext-nacl)# [sequence-number] {permit|deny} <protocol> { <source-ip> <wildcard-mask> | host <source-ip> | any } [operator <port>] { <dest-ip> <wildcard-mask> | host <dest-ip> | any } [operator <port>] [established]
(config-ext-nacl)# no <sequence-number>
```

### Common ACL CMDs

Apply an ACL on an int:

```
(config)# interface <interface-id>
(config-if)# ip access-group { <100-199> | <ACL-NAME> } { in | out }
```

Testing:

```
# show access-lists
# show ip access-lists <ID/NAME>
# show ip interface <interface-id>
# show running-config | section access-list
```

## NAT


### Static NAT

Create a static link for static NAT

```
(config)# ip nat inside source static [inside-local-ip] [inside-global-ip]
```

### Dynamic NAT

```
(config)# access-list <1-99> permit <inside-local-network> <wildcard-mask>

(config)# ip nat pool [POOL_NAME] [start-ip] [end-ip] netmask [mask]

(config)# ip nat inside source list <num> pool [POOL_NAME]
```

### Single IP PAT

The inside global address will be the IP of the outside interface that the packet is meant to exit from.

Configure a standard IPv4 ACL for the inside local IPs that are eligible for translation.

```
(config)# ip nat inside source list <num> <int ID> overload
```

### IP Pool PAT

Configure a named standard IPv4 ACL for the inside local IPs that are eligible for translation

Configure NAT Pool. It is a list of inside global IPs that any inside local IP address can be translated to:

```
(config)# ip nat pool [POOL_NAME] [start-ip] [end-ip] netmask [mask]
```

Bind ACL to NAT Pool.

```
(config)# ip nat inside source list [ACL_NAME] pool [POOL_NAME] overload
```

### Common NAT CMDs

Configure inside and outside interfaces:

```
(config-if)# ip nat inside/outside
```

Testing:

```
# show ip nat translations
# show ip nat statistics
# clear ip nat translation *
```
