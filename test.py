import tapa

matrix = tapa.Matrix(10, 10)
matrix.print()

print('')

print("matrix.surroundings(4, 0)")
for cell in matrix.surroundings(4, 0):
    print(cell, cell.x, cell.y)

print('')

print("matrix.surroundings(0, 0)")
for cell in matrix.surroundings(0, 0):
    print(cell, cell.x, cell.y)

print('')

print("matrix.checksurroundings(9, 4),(0, 9)")
matrix.checksurroundings(9, 4)
# matrix.checksurroundings(0, 9)
matrix.print()
