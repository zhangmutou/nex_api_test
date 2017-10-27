import unittest
from nex_session import NexSession

s = NexSession()
none_session = s.none_session
admin_session = s.admin_session
super_session = s.super_session
normal_session = s.normal_session

class NexBTest(unittest.TestCase):

	def setUp(self):
		self.url = 'https://qa.bnex.com'
		self.none_session = none_session
		self.admin_session = admin_session
		self.super_session = super_session
		self.normal_session = normal_session

	def run_test(self, case):
		role = case['role']
		if role == 1: print(self.super_session.get(self.url+'/user/getCurrentAccount').json())
		print('test1')

	@staticmethod
	def add_test_func(case):
		def func(self):
			self.run_test(case)
		return func

# /user/ 账户管理模块
class UserTest(NexBTest):
	# /user/add 	添加账户
	# /user/list 	用户列表
	# /user/getRoleList 	获取角色列表
	pass


class RoleTest(NexBTest):
	pass

class LogTest(NexBTest):
	pass

class InvoceTest(NexBTest):
	pass

class ChargeTest(NexBTest):
	pass

class ConsumeTest(NexBTest):
	pass

class RemainTest(NexBTest):
	pass

class ApplyTest(NexBTest):
	pass

class ApproveTest(NexBTest):
	pass

class DspTest(NexBTest):
	pass

class StatisticsTest(NexBTest):
	pass

class PositionTest(NexBTest):
	pass

class IndustryTest(NexBTest):
	pass

class AuditingTest(NexBTest):
	pass