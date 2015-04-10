#!/usr/bin/env python
# encoding: utf-8


filename = r'/root/test/access2_log'
with open(filename) as f:
    conn=f.readlines()
    lines=len(conn)
#print lines
i = 1
buff = []
fout = open("output0.log",'wb')
for line in conn:
    fout.write(line)
    i+=1
    if  i%1024 ==0:
        fout.close()
        fout = open("output%d.log" %(i/1024),'wb')

fout.close()
total_file = lines/1024+1
print total_file
