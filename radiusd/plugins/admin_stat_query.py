#!/usr/bin/env python
#coding=utf-8
import json

def process(req=None,admin=None):
    data = admin.runstat.copy()
    data['msg_id'] = req.get('msg_id')
    admin.sendMessage(json.dumps(data),False) 


