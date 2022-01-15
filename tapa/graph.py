import itertools
import random
from collections import defaultdict


class Graph:
    def __init__(self, cells):
        self.cells = cells
        self.graph = defaultdict(set)
        for c in itertools.combinations(cells, 2):
            if (c[0].x - c[1].x) ** 2 + (c[0].y - c[1].y) ** 2 == 1:
                self.join(c[0], c[1])

    def join(self, c0, c1):
        self.graph[c0].add(c1)
        self.graph[c1].add(c0)

    def inspect(self):
        print(self)
        for cell in self.cells:
            print('  ', end='')
            cell.inspect()
            for j in self.graph[cell]:
                print('    -> ', end='')
                j.inspect()

    def visit(self, c0, visited):
        visited[c0] = True
        for c1 in self.graph[c0]:
            if visited[c1] == False:
                self.visit(c1, visited)

    def isa_tree(self):
        visited = dict(zip(self.graph.keys(), [False] * len(self.graph)))
        self.visit(random.choice(list(self.graph.keys())), visited)
        for c in self.graph.keys():
            if visited[c] == False:
                return False
        return True
