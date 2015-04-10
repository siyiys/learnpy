#!/usr/bin/env python
# encoding: utf-8

def dead_loop():
        while True:
                    pass
import threading
t = threading.Thread(target=dead_loop)
t.start()
dead_loop()
t.join()
