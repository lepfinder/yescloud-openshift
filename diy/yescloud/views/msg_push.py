#########################################################################
# File Name: msg_push.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sat 09 Mar 2013 11:29:47 AM CST
########################################################################
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
from flask import request,render_template,redirect,url_for,flash
from flask.ext.login import LoginManager,current_user,login_required
from yescloud import app,connection
from yescloud.modules import LogMessage
from yescloud.util import LogSender

@app.route("/sendmsg/",methods=["POST"])
def send_msg():
	msg = connection.LogMessage()
	msg['appkey'] = str(request.form['appkey'])
	msg['message'] = str(request.form['message'])
	msg.save()

	sendno = 1
	appkey = app.config['JPUSH_CLIENT_APPKEY']
	receiver_type = app.config['JPUSH_CLIENT_RECEIVER_TYPE']
	master_secret = app.config['JPUSH_CLIENT_MASTER_SECRET']
	msg_type = app.config['JPUSH_CLIENT_MSG_TYPE']
	msg_content = msg['message']
	platform = app.config['JPUSH_CLIENT_PLATFORM']
	print msg_content

	sender = LogSender(sendno,appkey,receiver_type,master_secret,msg_type,msg_content,platform)
	print sender.sendto()
	return "success"


