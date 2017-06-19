#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-17 10:52:05
# @Author  : KID
# @Link    : http://example.org
# @Version : $Id$


#url = "https://wiki.gentoo.org/wiki/Handbook:Main_Page"
# import urllib.parse
# import urllib.request
# url = 'https://zhidao.baidu.com/question/1445864973574728140.html'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'name' : 'WHY',    
#          'location' : 'SDU',    
#          'language' : 'Python',
#          'ie' : 'utf-8',
#          'wd' : 'python' }
# headers = { 'User-Agent' : user_agent }
# data = urllib.parse.urlencode(values)
# #data=data.encode(encoding='UTF8')
# req = urllib.request.Request(url+'?'+data)
# #, data, headers)
# response = urllib.request.urlopen(req)
# the_page = response.read()
# # print(the_page.decode('UTF8'))
# print(the_page)

# import urllib.request
# url ="http://www.baidu.com"
# url2 ="https://www.baidu.com"
# url3 ="http://www.jb51.net/article/82105.htm"
# url4 ="https://zhidao.baidu.com/question/1445864973574728140.html"
# r = urllib.request.urlopen(url)
# html = r.read().decode('UTF-8')
# print(html)
import urllib.request
url ="https://wiki.gentoo.org/wiki/Handbook:Main_Page/zh-cn"
content = urllib.request.urlopen(url).read()
print(content)