# -*- coding:UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/31 10:35
# @Author  : ailsabe@126.com
# @Site    : 
# @File    : run.py

from scrapy import cmdline

name = 'xiaohuar'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
