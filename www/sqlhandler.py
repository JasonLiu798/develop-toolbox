#!/bin/env python
#-*- coding:utf-8 -*-

'''
@name sql handler
@desc process sql
'''

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import util.db.sqlgen as sqlgen
import util.log.logger as logger

from functions import *

log = logger.Logger(loglevel=1, logger="stdout").getlog()

class SqlHandler(tornado.web.RequestHandler):
    def get(self,action):
        log.info('action:'+action)
        if action=='index':
            self.index()
        elif action=='gen':
            self.genmultitab()
    #index
    def index(self):
        self.render(
            "sql.html",
            page_title = "Tools",
        )
    #gen multi tab
    def genmultitab(self):
        sql=self.get_argument("sql")
        tabcount=self.get_argument("tabcount")
        fmt = sqlparse.parse("fmt")
        log.info('sql:'+sql+',tabcount:'+tabcount+",fmt"+fmt)
        errno=0
        if not tabcount.isdigit() or int(tabcount)>1000 or int(tabcount)<1:
            errno=1001
        else
            data=sqlgen.generateMultiTab(sql,int(tabcount),'H')
            if data==None:
                errno=10001
        res=genresp(errno,data)
        self.write(res)







