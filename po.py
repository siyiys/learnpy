#!/usr/bin/env python
# encoding: utf-8

import subprocess
pingP=subprocess.Popen(args='ping -c 4 www.baidu.com',shell=True)
pingP.wait()
print pingP.pid
print pingP.returncode
