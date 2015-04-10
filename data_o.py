#!/usr/bin/env python
# encoding: utf-8
import os
def enpaths(path):
    ''' 文件加目录，绝对路径，不包含空的目录'''
    path_colle=[]
    for dirpath,dirnames,filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath,file)
            path_colle.append(fullpath)
    return path_colle
