#!/usr/bin/env python
# encoding: utf-8

import tarfile
import os
import time
target='/root/test'
gzfile='/tmp/test.tar.gz'
tar  = tarfile.open(gzfile,'w|gz')
#循环需要压缩的目录,不包含空的文件夹,返回文件的绝对路径列表
def enpaths(path):
            path_colle=[]
            for dirpath,dirnames,filenames in os.walk(path):
                if '^.[\s\S]*' in dirnames:
                    dirnames.remove('^.[\s\S]*')
                for file in filenames:
                    fullpath = os.path.join(dirpath,file)
                    path_colle.append(fullpath)
            return path_colle
lista=enpaths(target)
#循环列表，添加压缩文件
for i in lista:
    tar.add(i)
tar.close()

###获取文件的大小和mtime即ll看到的时间
def get_file_info(info):
    dict_info={}
    for file in info:
        size_list=[]
        mtime_list=[]
        size=os.path.getsize(file)
        mtime=os.path.getmtime(file)
        mtime_format=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(mtime))
        size_list.append(size)
        mtime_list.append(mtime_format)
        dict_info[file]=[size_list,mtime_list]
    return  dict_info
info=get_file_info(lista)
for key  in info:
    print key,info[key][0],info[key][1]
