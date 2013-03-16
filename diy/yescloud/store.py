#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: store.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sat 09 Mar 2013 11:12:47 AM CST
########################################################################
from mongokit import Connection
from setting import *

connection = Connection(MONGO_URL)
