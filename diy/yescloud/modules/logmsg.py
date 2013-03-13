#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: logmsg.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sun 10 Mar 2013 01:26:54 PM CST
########################################################################

import datetime
from mongokit import *


class LogMessage(Document):
	__collection__ = 'log_message'
	__database__ = 'yescloud'
	structure = {
			'appkey':unicode,
	        'project_name':unicode,
	        'msg_title' :unicode,
			'msg_content':unicode,
			'date_creation':datetime.datetime,
	        'send_status':unicode,
	}
	
	default_values = {'date_creation':datetime.datetime.utcnow}


class SendNo(Document):
	__collection__ = 'send_no'
	__database__ = 'yescloud'
	structure = {
	    'name':str,
	    'val':int
	}


