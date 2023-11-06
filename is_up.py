from os import system
from sys import argv

def ping(ip):
    if system(f"ping -c 1 {ip}") == 0:
        return("UP !")
    else:
        return("DOWN !")