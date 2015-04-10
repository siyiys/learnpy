#!/usr/bin/env python
# encoding: utf-8

import os
path = "/tmp"
def enpaths(path=path):
    ''' 文件加目录，绝对路径，不包含空的目录'''
    path_colle=[]
    for dirpath,dirnames,filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath,file)
            path_colle.append(fullpath)
    return path_colle
def  enfiles(path=path):
    '''所有的目录,不包含空文件夹'''
    file_colle=[]
    for dirpath,dirnames,filenames in os.walk(path):
        for file in filenames:
            file_colle.append(file)
    return  file_colle

def  endir(path=path):
    '''所有的文件名'''
    dir_colle=[]
    for dirpath,dirnames,filenames in os.walk(path):
        for file in filenames:
            dir_colle.append(dirpath)
    return   dir_colle


if __name__ == '__main__':
    print '\nlist of all paths in a dir:'
    for path in enpaths():
        print path
    print '\n--------------------------:'
    for path in endir():
        print path
    print '\n--------------------------file:'
    for path in enfiles():
        print path













