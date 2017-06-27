#!/usr/bin/env python

"""

Updated: 2016-03-14 frankb1

"""


import subprocess, re, sys, getopt
import socket

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:",["ifile="])
    except getopt.GetoptError:
        print '\n Usage: dnsLookup.py -i <inputfile>\n\n'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print '\n Usage: dnsLookup.py -i <inputfile>\n\n'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    if inputfile == '' :
        print '\n Input file required\n'
        sys.exit(2)

    with open(inputfile) as f:
        for hostname in f:
            hostname=hostname.rstrip('\r\n')
            try:
            
                addr = socket.gethostbyname(hostname)
                print hostname+","+addr

            except:
                print "something broke with: " + hostname
                
if __name__ == "__main__":
    main(sys.argv[1:])

    
    
