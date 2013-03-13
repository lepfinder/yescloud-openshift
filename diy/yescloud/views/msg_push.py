#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: msg_push.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sat 09 Mar 2013 11:29:47 AM CST
########################################################################
import json

from flask import request,render_template,redirect,url_for,flash
from flask.ext.login import LoginManager,current_user,login_required
from yescloud import app,connection
from yescloud.modules import LogMessage,SendNo
from yescloud.util import LogSender
from mongokit import ObjectId

@app.route("/sendmsg/",methods=["POST"])
def send_msg():
	msg = connection.LogMessage()
	msg['appkey'] = request.form['appkey']
	msg['msg_title'] = request.form['msg_title']
	msg['msg_content'] = request.form['msg_content']
	
	project = connection.Project.find_one({"appkey":msg['appkey']})
	msg['project_name'] = project['name']
	
	msg.save()
	
	
	sendno = 1
	sendno_object = connection.SendNo.find_one()
	if sendno_object:
		sendno = int(sendno_object['val'])
		connection.yescloud.send_no.update({"name":'send_no'},{"$inc":{"val":1}})
	else:
		sendno_object = connection.SendNo()
		sendno_object['name'] = 'send_no'
		sendno_object['val'] = 1
		sendno_object.save()		
	
	appkey = app.config['JPUSH_CLIENT_APPKEY']
	receiver_type = app.config['JPUSH_CLIENT_RECEIVER_TYPE']
	master_secret = app.config['JPUSH_CLIENT_MASTER_SECRET']
	msg_type = app.config['JPUSH_CLIENT_MSG_TYPE']
	
	msg_content = u'{"n_content":"%s","n_extras":{"msg_id":"%s"}}' % ("".join(['[',project['name'],']',msg['msg_title'].strip()]),msg['_id'])
	platform = app.config['JPUSH_CLIENT_PLATFORM']

	sender = LogSender(sendno,appkey,receiver_type,master_secret,msg_type,msg_content,platform)
	
	msg['send_status'] = sender.sendto()
	print msg['send_status']
	msg.update()
	
	return "success"

@app.route("/getmsg/<id>")
def get_msg(id):
	msg = connection.LogMessage.find_one({'_id':ObjectId(id)})
	print msg
	if msg:
		return msg.to_json()
	else:
		return ""

@app.route("/recentmsg/")
def get_recent_msg():
	msgCur = connection.LogMessage.find().sort([("_id",-1)]).limit(10)
	msgList = []
	for msg in msgCur:
		msgList.append(msg.to_json())

	return "".join(["[",",".join(msgList),"]"])
