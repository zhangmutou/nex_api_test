import unittest
import threading
import queue
import time
from nex_b_admin import NexBAdmin
import result
import report

def make_nexb_obj():
	# HomeTest = type('HomeTest', (NexBAdmin,), {})
	# RtbReportTest = type('RtbReportTest', (NexBAdmin,), {})
	# PdbReportTest = type('PdbReportTest', (NexBAdmin,), {})
	# ContrastReportTest = type('ContrastReportTest', (NexBAdmin,), {})
	# for i in range(5):
	# 	setattr(HomeTest, 'test_{}'.format(i), HomeTest.set_test_func(i))
	# 	setattr(RtbReportTest, 'test_{}'.format(i), RtbReportTest.set_test_func(i))
	# 	setattr(PdbReportTest, 'test_{}'.format(i), PdbReportTest.set_test_func(i))
	# 	setattr(ContrastReportTest, 'test_{}'.format(i), ContrastReportTest.set_test_func(i))

	# return [HomeTest, RtbReportTest, PdbReportTest, ContrastReportTest]
	# HomeTest = None
	HomeTest = type('HomeTest', (NexBAdmin,), {})
	HomeTestTest = type('HomeTestest', (NexBAdmin,), {})
	print(HomeTest.__name__ == 'HomeTest')
	case1 = {'url':'/user/getCurrentAccount', 'method':'get', 'name':'test3', 'data':{}}
	case2 = {'url':'/user/add', 'method':'post', 'name':'test1', 'data':{'userName': "dddeddf", 'email': "ddddedf@163.com", 'roleIds': 2}}
	case3 = {'url':'/user/getCurrentAccount', 'method':'get', 'name':'test4', 'data':{}}
	case4 = {'url':'/user/add', 'method':'post', 'name':'test2', 'data':{'userName': "dddeddf", 'email': "ddddedf@163.com", 'roleIds': 2}}
	setattr(HomeTest, 'test_{}'.format(case1['name']), HomeTest.add_test_func(case1))
	setattr(HomeTest, 'test_{}'.format(case2['name']), HomeTest.add_test_func(case2))
	setattr(HomeTest, 'test_{}'.format(case3['name']), HomeTest.add_test_func(case3))
	setattr(HomeTest, 'test_{}'.format(case4['name']), HomeTest.add_test_func(case4))
	setattr(HomeTestTest, 'test_{}'.format(case1['name']), HomeTestTest.add_test_func(case1))
	setattr(HomeTestTest, 'test_{}'.format(case2['name']), HomeTestTest.add_test_func(case2))
	setattr(HomeTestTest, 'test_{}'.format(case3['name']), HomeTestTest.add_test_func(case3))
	setattr(HomeTestTest, 'test_{}'.format(case4['name']), HomeTestTest.add_test_func(case4))

	return HomeTest, HomeTestTest

def run_case(TestCase):
	suite = unittest.TestLoader().loadTestsFromTestCase(TestCase[0])
	r = result.Result()
	suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase[1])
	# runner = unittest.TextTestRunner()
	# print(suite.countTestCases())
	# print(TestCase.defaultTestResult())
	# runner.run(suite)
	suite.run(r)
	suite1.run(r)
	print(r.success_count)
	# print(r.result)
	print(r.testsRun)
	rep = report.Report(r)
	# rep.add_result(r)
	a = rep.generate_report()
	# suite.run()
	# result = r.__dict__
	# a = sortResult(r.result)
	return a

def sortResult(result_list):
    # unittest does not seems to run in any particular order.
    # Here at least we want to group them together by class.
    rmap = {}
    classes = []
    for n,t,o,e in result_list:
        cls = t.__class__
        if not cls in rmap:
            rmap[cls] = []
            classes.append(cls)
        rmap[cls].append((n,t,o,e))
    r = [(cls, rmap[cls]) for cls in classes]
    return r

case_queue = queue.Queue()
result_queue = queue.Queue()

class ThreadTest(threading.Thread):

	def __init__(self, case_queue, result_queue):
		threading.Thread.__init__(self)
		self.case_queue = case_queue
		self.result_queue = result_queue

	def run(self):
		while True:
			TestCase = self.case_queue.get()
			result = run_case(TestCase)
			self.result_queue.put(result)
			self.case_queue.task_done()

class ThreadResult(threading.Thread):

	def __init__(self, result_queue):
		threading.Thread.__init__(self)
		self.result_queue = result_queue

	def run(self):
		while True:
			result = self.result_queue.get()
			print(result['testsRun'])
			self.result_queue.task_done()

def put_case_to_queue(obj):
	for o in obj:
		case_queue.put(o)

def create_test_thread(thread_num):
	for i in range(thread_num):
		t = ThreadTest(case_queue, result_queue)
		t.setDaemon(True)
		t.start()

def create_result_thread(thread_num):
	for i in range(thread_num):
		t = ThreadResult(result_queue)
		t.setDaemon(True)
		t.start()

def main(thread_num):
	obj = make_nexb_obj()
	create_test_thread(thread_num)
	create_result_thread(thread_num)
	put_case_to_queue(obj)

if __name__ == '__main__':
	# thread_num = 2
	# main(thread_num)
	# case_queue.join()
	# result_queue.join()
	# print(1)
	obj = make_nexb_obj()
	a = run_case(obj)
	print(a)