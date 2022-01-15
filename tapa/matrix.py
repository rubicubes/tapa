from tapa.graph import Graph
from tapa.cell import Cell
import itertools


class Matrix:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.m = []
        for i in range(x):
            n = []
            for j in range(y):
                n.append(Cell(i, j))
            self.m.append(n)
        self.seeds = set()
        self.load()

    def cell(self, x, y):
        if 0 <= x <= self.x - 1 and 0 <= y <= self.y - 1:
            return self.m[x][y]
        else:
            return None

    def seed(self, cell, value):
        self.seeds.add(cell)
        cell.set(value)

    def load(self):
        self.seed(self.cell(0, 9), '2')
        self.seed(self.cell(1, 1), '3,1')
        self.seed(self.cell(1, 5), '4,2')
        self.seed(self.cell(3, 3), '2,2,1')
        self.seed(self.cell(3, 8), '3,3')
        self.seed(self.cell(4, 1), '4,2')
        self.seed(self.cell(4, 5), '3,1,1')
        self.seed(self.cell(6, 3), '4,2')
        self.seed(self.cell(6, 7), '2,4')
        self.seed(self.cell(7, 1), '2,3')
        self.seed(self.cell(7, 9), '2')
        self.seed(self.cell(8, 6), '2,2')
        self.seed(self.cell(9, 4), '4')

    def print(self):
        for i in range(self.x):
            for j in range(self.y):
                self.m[i][j].print()
            print('')

    def is_cell_at_the_edge(self, cell):
        if cell.x == 0 or cell.x == self.x - 1:
            return True
        if cell.y == 0 or cell.y == self.y - 1:
            return True
        return False

    def surroundings(self, x, y):
        ss = []
        stack = []
        offsets = [[-1, 1], [0, 1], [1, 1], [1, 0],
                   [1, -1], [0, -1], [-1, -1], [-1, 0]]
        for offset in offsets:
            cell = self.cell(x + offset[0], y + offset[1])
            if cell == None:
                if not stack and ss:
                    stack, ss[:] = ss[:], []
            else:
                ss.append(cell)
        if stack:
            ss.extend(stack)
        return ss

    def checksurroundings(self, x, y):		# whose value is single number
        surroundings = self.surroundings(x, y)
        value = int(self.cell(x, y).value)
        c = list(itertools.combinations(range(len(surroundings)), value))
        cells_list = []
        for i in c:
            cells = []
            for j in range(len(surroundings)):
                if j in i:
                    cells.append(surroundings[j])
            cells_list.append(cells)
        print(cells_list)
        surroundings_true = []
        for cells in cells_list:
            graph = Graph(cells)
            if graph.isa_tree():
                surroundings_true.append(cells)
        for i in surroundings_true:
            for j in i:
                print(j, j.x, j.y)
        s = set(surroundings_true[0])
        for i in surroundings_true:
            s &= set(i)
        print(list(s))
        for i in list(s):
            self.seed(self.cell(i.x, i.y), 1)
