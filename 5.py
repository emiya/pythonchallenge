#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-17 15:12:59
# @Author  : emiya
# @Link    : http://example.org
# @Version : $Id$

import os
import  pickle
import urllib.request
import pprint
#http://www.pythonchallenge.com/pc/def/peak.html
#
f=open(r'/home/mi/Downloads/pythonchallenge/5-text',"rb")
text =f.read()
# pickle 
f.close()
#bytes(text, encoding = "utf8")

# url = "http://www.pythonchallenge.com/pc/def/banner.p"
# text = urllib.request.urlopen(url).read()
i=0  
ok=pickle.loads(text)


for line in ok:
	ll=""
	for (c,n) in line:
		ll+=c*n
	print(ll)
	