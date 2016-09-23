#!/bin/env python
#-*- coding:utf-8 -*-

import util.net.iputil as iputil

log = logger.Logger(loglevel=1, logger="stdout").getlog()

class SqlHandler(tornado.web.RequestHandler):
    def get(self,action):
        log.info('action:'+action)
        if action=='index':


