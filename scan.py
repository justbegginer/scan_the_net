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
    #print(arp_request.summary()) #print Arp request
    #print(arp_request.show())#show args
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") #make broadcast req
    broadcast_request = broadcast/arp_request# / means concatenation
    #scapy.ls(scapy.Ether) #information about current class
    answered = scapy.srp(broadcast_request ,timeout = 1 ,verbose = False)[0] # the second element of array is a unanswered list
    #print(scapy.ls(scapy.srp))
    return parse_resp(answered)

def parse_resp(response):
    book = {}
    for i in response:
        ip = i[1].psrc#parse ip
        mac_address = i[1].hwsrc# parse mac
        # how i parse? i is an element of response , it contains sent information and get information
        book[ip] = mac_address
    return book

def print_info(book):
    shift = 15
    print(f"Mac{shift *' '}Ip")
    for i in book:
        shift_for_current_line = shift-len(i)+3
        print(40*"-")# shift + len("Mac") + len("Ip")+20(extra)
        print(f"{i}{shift_for_current_line * ' '}{book[i]}")


#scan("192.168.0.1")
book_of_ips_mac = scan("192.168.0.1/24")# /24 -> that part doesn't work correct like ARP who has ?? says ??
print_info(book_of_ips_mac)
#for i in range(1 , 256):
#    scan("192.168.0."+str(i))