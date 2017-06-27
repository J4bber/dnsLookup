#!/usr/bin/env python

"""

v0.4 - dev4

"""


import subprocess, re
import sys,time,types,getopt
from dns import resolver,reversename,exception
import traceback
from subprocess import call




def main(argv):
    myResolver = resolver.Resolver() #create a new instance named 'myResolver'
    myResolver.nameservers = ['192.168.28.132']
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
        for line in f:
            ip=line.rstrip('\r\n')
            # try:
                # rev_name = reversename.from_address(ip)
                # myAnswers = myResolver.query(rev_name,"PTR").__iter__().next().to_text()[:-1]
                # nameToIP = myResolver.query(myAnswers,"A").__iter__().next().to_text()[:-1]
                # print "%s,%s,%s,%s"%(ip,rev_name,myAnswers,nameToIP)
            # except resolver.NXDOMAIN: 
                # print "%s,NXDOMAIN"%(ip)
            # except KeyboardInterrupt:
                # exit()
            # except:
                # print sys.exc_info()
                # print "%s: UNSPECIFIED ERROR\n"%(ip)
            call(["ls", "-l"])



if __name__ == "__main__":
    main(sys.argv[1:])
