#!/usr/bin/env python
# encoding: utf-8

import tarfile

tar = tarfile.open('largefile.tar','w')
tar.add("largefile.txt")
tar.close()
