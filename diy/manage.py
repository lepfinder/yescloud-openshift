#########################################################################
# File Name: manage.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sat 09 Mar 2013 09:30:18 AM CST
########################################################################
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import os
here = os.path.dirname(os.path.abspath(__file__))
os.environ['PYTHON_EGG_CACHE'] = os.path.join(here, '..', 'misc/virtenv/lib/python2.7/site-packages')
os.environ['PYTHONPATH'] = os.path.join(here, '..', 'misc/virtenv/lib/python2.7/site-packages')
virtualenv = os.path.join(here, '..', 'misc/virtenv/bin/activate_this.py')
execfile(virtualenv, dict(__file__=virtualenv))

from flask.ext.script import Manager

from yescloud import app

manager = Manager(app)

if __name__ == "__main__":
	manager.run()

