from scapy.all import *
send(IP(dst="192.168.86.43")/ICMP())
sendp(Ether()/IP(dst="192.168.86.43",ttl=(1,4)), iface="enp0s3")
