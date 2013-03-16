#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: projects.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Sun 10 Mar 2013 11:24:12 AM CST
########################################################################

import uuid
from flask import request,render_template,redirect,url_for,flash
from flask.ext.login import login_required,current_user
from yescloud.models import Project,ProjectForm,LogMessage

from yescloud import app,connection

@app.route("/project/create/",methods=['POST','GET'])
@login_required
def project_create():
	form = ProjectForm()
	if form.validate_on_submit():
		flash("Create Project Success!")
		if form.data:
			project = connection.Project()
			project['name'] = form.data['name']
			project['description'] = form.data['description']
			project['monitor_group'] = form.data['monitor_group']
			project['appkey'] = str(uuid.uuid4())

			project.save()
		return redirect(url_for("index"))
	return render_template("project_create.html",form=form)


@app.route("/project/<appkey>/setting")
@login_required
def project_setting(appkey):
	project = connection.Project.find_one({"appkey":appkey})
	return render_template("project_setting.html",p = project)


@app.route("/project/<appkey>")
@login_required
def project_detail(appkey):
	project = connection.Project.find_one({"appkey":appkey})
	messages = connection.LogMessage.find({"appkey":appkey})
	return render_template("project_detail.html",p = project,messages = messages)

