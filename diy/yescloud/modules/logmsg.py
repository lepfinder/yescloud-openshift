#########################################################################
# File Name: logmsg.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sun 10 Mar 2013 01:26:54 PM CST
########################################################################
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import datetime
from mongokit import *

class LogMessage(Document):
	__collection__ = 'log_message'
	__database__ = 'yescloud'
	structure = {
			'appkey':str,
			'message':str,
			'appkey':str,
			'date_creation':datetime.datetime
	}
	
	default_values = {'date_creation':datetime.datetime.utcnow}



