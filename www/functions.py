#!/bin/env python
#-*- coding:utf-8 -*-

from errorcode import *
import json

def genresp(errno,data):
    if errno==0:
        res={"code":0,"data":data}
    else:
        res={"code":errno,"msg":errtab[errno]}
    res= json.dumps(res)
    return res
