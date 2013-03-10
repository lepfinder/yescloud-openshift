#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: manage.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sat 09 Mar 2013 09:30:18 AM CST
########################################################################
from flask.ext.script import Manager

from yescloud import app

manager = Manager(app)

if __name__ == "__main__":
	manager.run()