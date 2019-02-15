import pygame, time
class Timer:

	def __init__(self, x1, y1, w, h):
		self.count = 0
		self.upperLeftX = x1
		self.upperLeftY = y1
		self.width = w
		self.height = h
		self.startTime = time.time()

	def increaseCount(self):
		timeElapsed = time.time() - self.startTime
		self.count = int(timeElapsed)

	def render(self):
		outputString = str(self.count).zfill(4)
		print(outputString)