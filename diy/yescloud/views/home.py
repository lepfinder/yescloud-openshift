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
from yescloud.models import Project,User
from yescloud import app
from yescloud.store import connection
from mongokit import ObjectId

@app.route("/")
@login_required
def index():
	projects = connection.Project.find()
	
	messages = connection.LogMessage.find().sort([("_id",-1)]).limit(10)
	
	return render_template("index.html",projects = projects,messages=messages)

@app.route("/about/")
@login_required
def about():
	return render_template("about.html")

@app.route("/login/",methods=["GET","POST"])
def login():
	if request.method == "POST" and "username" in request.form:
		username = request.form['username']
		password = request.form['password']
		user = connection.yescloud.user.one({'name':username,'password':password})

		if user:
			if login_user(User(user['_id'],user['name'],user['password'])):		
				flash("You are logged in successful!","success")
				return redirect(request.args.get("next") or url_for("index"))
		else:
			flash ("Sorry, please check your username or password!","error")
	return render_template("login.html")

@app.route("/logout/")
def logout():
	logout_user()
	return redirect(url_for("index"))

