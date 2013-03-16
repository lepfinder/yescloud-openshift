#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: setting.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sun 10 Mar 2013 11:32:04 AM CST
########################################################################
import os

SITE_TITLE = "SERVER MONITOR"

JPUSH_CLIENT_APPKEY = '5f7bceda07dab8d14ddf7a91'
JPUSH_CLIENT_MASTER_SECRET = '323ef4d65ec3eca4ed5ecbb2'
JPUSH_CLIENT_RECEIVER_TYPE = 4 #
JPUSH_CLIENT_MSG_TYPE = 1
JPUSH_CLIENT_PLATFORM = 'android'

env = os.environ
if env.has_key('OPENSHIFT_APP_NAME'):
	print 'net envirment'
	MONGO_URL = env["OPENSHIFT_MONGODB_DB_URL"]
else:
	print "local envirment"
	os.environ['OPENSHIFT_INTERNAL_IP'] = "127.0.0.1"
	os.environ['OPENSHIFT_INTERNAL_PORT'] = "8888"	
	MONGO_URL = 'mongodb://admin:g7iEU2KxPaR9@127.0.0.1:27017/'
