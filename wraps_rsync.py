#!/usr/bin/env python
# encoding: utf-8
from subprocess import call
import sys
import time
source = "/tmp/sync_dir_A/"
target = "/tmp/sync_dir_T/"
rsync = "rsync"
arguments = "-av"
cmd = "%s %s %s %s" % (rsync,arguments,source,target)
def sync():
    while 1:
        ret = call(cmd,shell=True)
        if ret !=0:
            print "resubmitting rsync"
            time.sleep(10)
        else:
            print "rsync was successful"
            call("echo 'rsync was successful' |mail -s 'jobs done' root@tbag",shell=True)
            sys.exit(0)
sync()
