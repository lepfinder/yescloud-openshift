#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: user.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sun 10 Mar 2013 11:43:54 AM CST
########################################################################

from flask.ext.login import UserMixin

class User(UserMixin):
	def __init__(self,name,id,password,active=True):
		self.name = name
		self.id = id
		self.password = password
		self.active = active
	
	def is_active(self):
		return self.active
