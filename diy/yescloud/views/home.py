#! /usr/bin/env python
# -*- coding: UTF-8 -*-
#########################################################################
# File Name: blog.py
# Author: xiyang
# mail: sdlgxxy@gmail.com
# Created Time: Thu 07 Mar 2013 09:15:47 PM CST
########################################################################
from flask import render_template,request,redirect,url_for,flash
from flask.ext.login import LoginManager,current_user,login_required,login_user,logout_user
from yescloud.modules import Project
from yescloud import app,connection

@app.route("/")
@login_required
def index():
	projects = connection.Project.find()
	return render_template("index.html",projects = projects)

@app.route("/login/",methods=["GET","POST"])
def login():
	if request.method == "POST" and "username" in request.form:
		username = request.form['username']
		password = request.form['password']

		print username,password
		print app.config['ADMIN_USERNAME'],app.config['ADMIN_PASSWORD']
		if username == app.config['ADMIN_USERNAME']:
			if password == app.config['ADMIN_PASSWORD']:
				if login_user(app.config['USERS'].get(app.config['ADMIN_USERID'])):
					flash("Logged in!")
					return redirect(request.args.get("next") or url_for("index"))
			else:
				flash ("Sorry, please check your password!","error")
		else:
			flash("Invalid username!","error")
	return render_template("login.html")

@app.route("/logout/")
def logout():
	logout_user()
	return redirect(url_for("index"))

