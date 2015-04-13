#!/usr/bin/env python
# encoding: utf-8

import tarfile
tar  = tarfile.open('/tmp/temp.tar.gz','w|gz')
import os
for root,dir,files in os.walk('/root/test'):
    for file in files:
        fullpath = os.path.join(root,file)
        tar.add(fullpath)
tar.close()
