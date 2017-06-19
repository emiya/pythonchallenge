#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-16 20:38:03
# @Author  : KID
# @Link    : http://example.org
# @Version : $Id$

import os
import re
# http://www.pythonchallenge.com/pc/def/equality.html
url = "http://www.pythonchallenge.com/pc/def/equality.html"
f=open('3-str','r')
s=f.read()
f.close()

#print(s)
# pattern = re.compile('[A-Z][a-z][A-Z]')

# match = pattern.match(s)

# if match:
#     # 使用Match获得分组信息
#     print(match.group())
#print(s)
#pattern = re.compile(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]|[/n][A-Z]{3}[a-z][A-Z]{3}[a-z]|[a-z][A-Z]{3}[a-z][A-Z]{3}[/n]')
pattern = re.compile(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]')
from collections import Counter
match =pattern.findall(s)

# if match:
#     # 使用Match获得分组信息
#     print(match.groups()
print(match)

newurl = "".join(match)

url.replace(newurl,"equality")
print(url)
#ok=[]
# for strs in match:
# 	# pattern2 = re.compile('[a-z]')
# 	# match2 =pattern.findall(strs)
	
# 	# print(match2)
  
#  	print(strs[4])
#  	#ok.append(strs[3])
# #print(ok)
# b=Counter(ok)
# print(b)