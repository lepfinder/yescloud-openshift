#! /usr/bin/env python
#coding=utf-8
#*******************************************
# http://docs.jpush.cn/pages/viewpage.action?pageId=2621796
# 极光推送 服务器端api
#*******************************************
import urllib2, urllib, md5, json

class LogSender(object):
	def __init__(self,sendno,appkey,receiver_type,master_secret,msg_type,msg_content,platform):
		self.sendno = sendno
		self.appkey = appkey
		self.receiver_type = receiver_type
		self.master_secret = master_secret
		input_str = str(self.sendno) + str(self.receiver_type)  + self.master_secret
		self.verification_code = md5.new(input_str).hexdigest().upper()
		self.msg_type = msg_type
		self.msg_content = msg_content
		self.platform = platform

	def formatParams(self):
		params = {
				'sendno' : self.sendno,
				'app_key': self.appkey,
				'receiver_type':self.receiver_type,
				'verification_code':self.verification_code,
				'msg_type':self.msg_type,
				'msg_content':self.msg_content,
				'platform':self.platform,
		}
		return params

	def sendto(self):
		#print self.formatParams()['msg_content']
		print self.msg_content.decode("utf-8")
		print self.msg_content
		f = urllib2.urlopen(
				url     = 'http://api.jpush.cn:8800/sendmsg/v2/sendmsg',
				data    = urllib.urlencode(self.formatParams())
				)
		return f.read()

if __name__ == "__main__":
	
	sendno = 3
	appkey = '5f7bceda07dab8d14ddf7a91'
	receiver_type = 4
	master_secret = '323ef4d65ec3eca4ed5ecbb2'
	msg_type = 1
	msg_content = '{"n_content":"tomcat 挂了"}'
	platform = 'android'

	sender = LogSender(sendno,appkey,receiver_type,master_secret,msg_type,msg_content,platform)
	print "start send message"
	print sender.sendto()

