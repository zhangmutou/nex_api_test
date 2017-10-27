class Report(object):

	def __init__(self, result):
		self.result = result
		self.success_count = 0
		self.failure_count = 0
		self.error_count = 0
		self.totle_count = self.result.testsRun
		self.report = []

	def sort_result(self):
		rmap = {}
		classes = []
		for n,t,o,e in self.result.result:
			cls = t.__class__
			if not cls in rmap:
				rmap[cls] = []
				classes.append(cls)
			rmap[cls].append((n,t,o,e))
		self.success_count = self.result.success_count
		self.failure_count = self.result.failure_count
		self.error_count = self.result.error_count
		r = [(cls, rmap[cls]) for cls in classes]
		return r

	def generate_report(self):
		self.report = self.sort_result()
		return self.report
