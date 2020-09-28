from threading import Thread

class Counter:
	def __init__(self, start = 0):
		self.start = start
		self.count = 0
		self.running = False
	def startCount(self):
		self.running = True
		Thread(target = self.countUp, args = ()).start()
		return self
	def resetCount(self):
		self.count = 0
	def countUp(self):
		while True:
			if self.running:
				self.count = self.count + 1
			else:
				return
	def stopCount(self):
		self.running = False
	def resumeCount(self):
		self.running = True
	def value(self):
		return (self.count+self.start)