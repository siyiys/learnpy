#!/usr/bin/env python
# encoding: utf-8
import  data_o
import os
import hashlib
def creat_checksum(path):
    fp = open(path)
    checksum = hashlib.md5()
    while 1:
        buff = fp.read(8192)
        if not buff:break
        checksum.update(buff)
        fp.close()
        checksum = checksum.digest()
        return checksum

files=data_o.enpaths(r"/tmp/dum")
print files
#print len(files)
dup=[]
record={}
for line in files:
    com_key = (os.path.getsize(line),creat_checksum(line))
    if com_key in record:
        dup.append(line)
    else:
        record[com_key] = line
print  dup
