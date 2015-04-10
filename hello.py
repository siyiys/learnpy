#!/usr/bin/env python
# encoding: utf-8

import threading
import datetime
class ThreadClass(threading.Thread):
    def run(self):
        now = datetime.datetime.now()
        print "%s say hello word at time:%s" % (self.getName(),now)
for i in range(2):
    t = ThreadClass()
    t.start()
