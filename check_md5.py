#!/usr/bin/env python
# encoding: utf-8

import hashlib
def creat_checksum(path):
    fp = open(path)
    checksum = hashlib.md5()
    while 1:
        buff = fp.read(8192)
        if not buff:break
        checksum.update(buff)
        fp.close()
        checksum = checksum.hexdigest()
        return checksum
#A = creat_checksum(r"/tmp/file0.txt")
#print A
