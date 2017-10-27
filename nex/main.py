import threading
import queue
import result
import report
import unittest

test_queue = queue.Queue()
result_queue = queue.Queue()

class ThreadTest(threading.Thread):

	def __init__(self, test_queue, result_queue):
		threading.Thread.__init__(self)
		self.test_queue = test_queue
		self.result_queue = result_queue

	def run(self):
		while True:
			TestCase = self.test_queue.get()
			run_case(TestCase)
			# self.result_queue.put(result)
			self.test_queue.task_done()

class ThreadResult(threading.Thread):

	def __init__(self, result_queue):
		threading.Thread.__init__(self)
		self.result_queue = result_queue

	def run(self):
		while True:
			result = self.result_queue.get()
			self.result_queue.task_done()

r = result.Result()
def run_case(TestCase):
	suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
	suite.run(r)

def test(cases):
	# print('用例入队！')
	for case in cases:
		test_queue.put(case)

	# print('用例入队完毕，生成用例线程')

	for i in range(5):
		t = ThreadResult(test_queue)
		t.setDaemon(True)
		t.start()

	test_queue.join()



