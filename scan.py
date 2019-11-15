#!/usr/bin/env python

import scapy.all as scapy

#TODO easy version

def easy_scan(ip):
    return scapy.arping(ip)

#print(easy_scan("192.168.0.1/24"))
#TODO hard version
def scan(ip):
    arp_request =scapy.ARP(pdst = ip) # get arp request. pdst - ip
    broadcast = scapy.Ether("ff:ff:ff:ff:ff:ff")
    scapy.ls(scapy.Ether)#information about current class
print(scan("0.0.0.0/255"))