#!/usr/bin/env python
# encoding: utf-8

import socket
import re
import sys

def  check_server(address,port):
    s = socket.socket()
    print "connetct to %s on prot  %s " % (address,port)
    try:
        s.conect((address,port))
        print "connetct to %s on port %s " % (address,port)
        return Ture
    except socket.error,e:
        print "connect to %s on port %s failed."  % (address,port)
if __name__ == '__main__':
    check=check_server('127.0.0.1','80')


