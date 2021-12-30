from tapa.cell import Cell

class Matrix:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.m = []
		for i in range(x):
			n = []
			for j in range(y):
				n.append(Cell())
			self.m.append(n)
		self.seeding()

	def seeding(self):
		self.m[0][9].set('2')
		self.m[1][1].set('3,1')
		self.m[1][5].set('4,2')
		self.m[3][3].set('2,2,1')
		self.m[3][8].set('3,3')
		self.m[4][0].set('4,2')
		self.m[4][5].set('3,1,1')
		self.m[6][3].set('4,2')
		self.m[6][7].set('2,4')
		self.m[7][1].set('2,3')
		self.m[7][9].set('2')
		self.m[8][6].set('2,2')
		self.m[9][4].set('4')

	def print(self):
		for i in range(self.x):
			for j in range(self.y):
				self.m[i][j].print()
			print('')
