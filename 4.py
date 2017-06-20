#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-17 09:46:02
# @Author  : Emiya
# @Link    : http://example.org
# @Version : $Id$

import os

#http://www.pythonchallenge.com/pc/def/linkedlist.php
import re
import urllib.request

i=0 
um=8022
while True:

	url ="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
	url2 ="https://www.baidu.com"
	url3 ="http://www.jb51.net/article/82105.htm"
	url4 ="https://zhidao.baidu.com/question/1445864973574728140.html"
#	q = url + ''.join(um)
	q = url + str(um)
	r = urllib.request.urlopen(q)

	

	html = r.read().decode('UTF-8')
#	print(i,um,q,html)
	pattern = re.compile(r'and the next nothing is ([0-9]*)')

	um =pattern.findall(html)[0]
	i=i+1
	print(i,html)