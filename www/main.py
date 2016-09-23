#!/bin/env python
#-*- coding:utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import os
import datetime
from tornado.options import define, options

import sqlHandler

define("port", default=8090, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # (r"/(\w+)", sqlhandler.SqlHandler),
            # (r"/api",TestHandler),
            # (r"/sqlgen/search",sqlhandler.SqlHandler),
            (r"/test",TestHandler),
            (r"/index",IndexHandler),
            (r"/sqlgen/(.*)",sqlHandler.SqlHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            autoescape=None
            )
        tornado.web.Application.__init__(self, handlers, **settings)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "header.html",
            page_title = "Tools",
        )

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('aaa')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()











