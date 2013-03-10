#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: setting.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sun 10 Mar 2013 11:32:04 AM CST
########################################################################
import os
from modules import User

SITE_TITLE = "APP MONITOR"

USERS = {
	1:User(u"admin",1,u"admin")
}

ADMIN_USERID = 1
ADMIN_USERNAME = u'admin'
ADMIN_PASSWORD = u'admin'

JPUSH_CLIENT_APPKEY = '0a6c14b65be8bbb486a5c60f'
JPUSH_CLIENT_MASTER_SECRET = '5e2d97047d3e6a93db252a1f'
JPUSH_CLIENT_RECEIVER_TYPE = 4 #
JPUSH_CLIENT_MSG_TYPE = 1
JPUSH_CLIENT_PLATFORM = 'android'

env = os.environ
if env.has_key('OPENSHIFT_INTERNAL_IP'):
	print 'net envirment'
	MONGO_URL = env["OPENSHIFT_MONGODB_DB_URL"]
else:
	print "local envirment"
	MONGO_URL = 'mongodb://admin:g7iEU2KxPaR9@127.0.0.1:27017/'
