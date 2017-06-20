#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-11 02:08:19
# @Author  : emiya
# @Link    : http://example.org
# @Version : $Id$

import os
from collections import Counter

f=open(r'/home/mi/Downloads/pythonchallenge/2-text',"r")
ok=f.read().replace('\n','')
o=open('2-str','w')
b=Counter(ok)
print(b)
o.write(ok)
f.close()
o.close()

# f=open('2-str','r')
# s=Counter(f.read())
# f.close()
# print(s)