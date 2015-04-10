#!/usr/bin/env python
# encoding: utf-8

import os
from hashlib import sha256
from hmac import HMAC
def encrypt_password(password,salt=None):
    if salt is None:
        salt = os.urandom(8)
    assert 8 ==len(salt)
    assert isinstance(salt,str)
    if isinstance(password,unicode):
        password = password.encode('UTF-8')
    assert isinstance(password,str)
    result = password
    for i in xrange(10):
        result = HMAC(result,salt,sha256).digest()
    return salt+result

hashd = encrypt_password('luojun')
print hashd

def dec_password(hashd,input_password):
    return hashd == encrypt_password(input_password,salt=hashd[:8])
a=dec_password(hashd,'luoiijun')
print a

