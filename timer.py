import pygame, time
class Timer:

	def __init__(self, x1, y1, w, h):
		self.count = 0
		self.upperLeftX = x1
		self.upperLeftY = y1
		self.width = w
		self.height = h
		self.startTime = time.time_ns()

	def increaseCount(self):
		timeElapsed = time.time_ns() - self.startTime
		self.count = int(timeElapsed/100000000)

	def render(self):
		outputString = str(self.count).zfill(6)
		#print(outputString)
		return outputString
