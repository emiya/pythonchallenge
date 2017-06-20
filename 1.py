#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-11 01:37:30
# @Author  : emiya
# @Link    : http://example.org
# @Version : $Id$
# 
# 
#from string import maketrans
import os
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
intab ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
outtab ="CDEFGHIJKLMNOPQRSTUVWXYZAB"

#K-M O-Q E-G
trantab = str.maketrans(intab.lower(), outtab.lower())

print(text.translate(trantab))
print("http://www.pythonchallenge.com/pc/def/" + "map".translate(trantab) +".html")


  
# print (test_str.translate(str_trantab))