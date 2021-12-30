class Cell:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.value = None
		self.is_seed = False

	def set(self, value):
		self.value = value
		if type(value) == str:
			self.is_seed = True

	def print(self):
		if self.is_seed:
			print('*', end='')
		elif self.value == None:
			print('?', end='')
		else:
			print(self.value, end='')