#!/usr/bin/env python
# encoding: utf-8

from  check_md5 import creat_checksum
if creat_checksum(r"/tmp/file0.txt") == creat_checksum(r"/tmp/file00.txt"):
        print "Ture"
else:
         print "fasle"

print '11111111111'
