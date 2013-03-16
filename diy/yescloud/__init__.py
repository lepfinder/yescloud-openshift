#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: __init__.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sat 09 Mar 2013 11:12:47 AM CST
########################################################################
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import (LoginManager,current_user,login_required,
		login_user,logout_user,UserMixin,AnonymousUser,confirm_login)
from setting import *
from yescloud.store import connection
from mongokit import ObjectId

app = Flask(__name__)
app.debug = True

SECRET_KEY = 'nishigedachunlv'
Bootstrap(app)

app.config.from_object(__name__)
app.config['BOOTSTRAP_USE_CDN'] = False

if not connection.yescloud.user.one({"name":'admin'}):
	print "init admin user"
	connection.yescloud.user.insert({'name':'admin','password':'default'})

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = u"Please Login First!"

import views,models,util

@login_manager.user_loader
def load_user(id):
	user = connection.yescloud.user.one({"_id":ObjectId(id)})
	if user:
		return models.User(user['_id'],user['name'],user['password'])
	else:
		return None

login_manager.setup_app(app)

