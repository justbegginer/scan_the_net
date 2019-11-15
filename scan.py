#!/usr/bin/env python

import scapy

import scapy.all as scapy

#TODO easy version

def easy_scan(ip):
    return scapy.arping(ip) #simle arp ping

#print(easy_scan("192.168.0.1/24"))
#TODO hard version
def scan(ip):
    arp_request = scapy.ARP(pdst = ip) # get arp request. pdst - ip
    print(arp_request.summary()) #print Arp request
    print(arp_request.show())#show args
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") #make broadcast req
    print(broadcast.summary())
    print(broadcast.show())
    broadcast_req = broadcast/arp_request# / means concatenation
    #scapy.ls(scapy.Ether) #information about current class

scan("192.168.0.1")
#scan("192.168.0.1/24")# /24 -> that part doesn't work
#for i in range(1 , 256):
#    scan("192.168.0."+str(i))