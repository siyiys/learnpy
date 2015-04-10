#!/usr/bin/env python
# encoding: utf-8
import  data_o
from  check_md5 import creat_checksum
files=data_o.enpaths(r"/root/test")
print files
print len(files)
dup=[]
record=[]
for line in files:
    com_key = creat_checksum(line)
    print line+'   md5 is :'+com_key
