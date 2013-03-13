#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: project.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sun 10 Mar 2013 01:26:54 PM CST
########################################################################

import datetime
from mongokit import *
from flask.ext.wtf import Form, TextField, TextAreaField, ValidationError, Required



class Project(Document):
	__collection__ = 'project'
	__database__ = 'yescloud'
	structure = {
			'name':unicode,
			'description':unicode,
			'monitor_group':unicode,
			'appkey':str,
			'date_creation':datetime.datetime
	}
	
	default_values = {'date_creation':datetime.datetime.utcnow}


class ProjectForm(Form):
	name = TextField('name',description="the project's name",validators=[Required()])
	description = TextAreaField('description',description = "description of this Project")
	monitor_group = TextField('monitor_group',description = "please select the project's monitors")


