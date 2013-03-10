#########################################################################
# File Name: __init__.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sat 09 Mar 2013 11:12:47 AM CST
########################################################################
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import (LoginManager,current_user,login_required,
		login_user,logout_user,UserMixin,AnonymousUser,confirm_login)
from mongokit import Connection

from setting import *


app = Flask(__name__)

SECRET_KEY = 'nishigedachunlv'
app.debug = True
Bootstrap(app)

app.config.from_object(__name__)
app.config['BOOTSTRAP_USE_CDN'] = False

connection = Connection(app.config['MONGO_URL'])
connection.register([modules.Project,modules.LogMessage])

login_manager = LoginManager()

login_manager.login_view = "login"
login_manager.login_message = u"Please Login First!"

@login_manager.user_loader
def load_user(id):
	return USERS.get(int(id))

login_manager.setup_app(app)

import views,modules,util
