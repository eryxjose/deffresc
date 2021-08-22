#! /usr/bin/env python3

#from scapy.all import *
import scapy.all as scapy

def scan(ip):
    scapy.airping(ip)

scan("10.0.0.1")


