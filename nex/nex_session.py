import configparser
import requests
import redis
import json
import urllib3
# 忽略因请求https而忽略证书时的警告
urllib3.disable_warnings()


class NexSession(object):
	def __init__(self):
		self.config_path = '../nex_b.config'
		self.config = self._read_config()
		self.admin_session = self.create_session('admin')
		self.normal_session = self.create_session('normal')
		self.none_session = self.create_session('none')
		self.super_session = self.create_session('superadmin')


	def _read_config(self):
		config = configparser.ConfigParser()
		with open(self.config_path, 'r') as conf:
			config.readfp(conf)
		return config

	def create_session(self, role):
		config = self.config
		url = config['url']['base_url']
		if role == 'admin':
			username = config['admin']['username']
			password = config['admin']['password']
		elif role == 'none':
			username = config['none']['username']
			password = config['none']['password']
		elif role == 'normal':
			username = config['normal']['username']
			password = config['normal']['password']
		elif role == 'superadmin':
			username = config['superadmin']['username']
			password = config['superadmin']['password']

		host = config['redis']['host']
		port = config['redis']['port']
		password = config['redis']['password']

		s = requests.session()
		s.get(url+'/module_password/login.html', verify=False)
		s.get(url+'/common/getVerifyCode')

		k = s.cookies['NEXSESSION']
	    # 从redis获取验证码
		rds = redis.Redis(host=host, port=port, password=password)
		v = rds.get('session:ad.nex.b:%s' % k)
		verifyCode = v[-5:-1].decode()

		req = {
			'userName': username,
			'password': password,
			'verifyCode': verifyCode
		}

		headers = {
			"content-type": "application/json",
			"Accept": "application/json; text/plain, */*",
			"Accept-Encoding": "gzip, deflate, sdch"
		}

		s.post(url+'/user/login', data=json.dumps(req), headers=headers)

		return s