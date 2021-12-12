matrix = []
for i in range(10):
    matrix.append([None]*10)
# [[None]*10]*10
matrix[0][9] = '2'
matrix[1][1] = '3,1'
matrix[1][5] = '4,2'
matrix[3][3] = '2,2,1'
matrix[3][8] = '3,3'
matrix[4][1] = '4,2'
matrix[4][5] = '3,1,1'
matrix[6][3] = '4,2'
matrix[1][8] = 1

for i in range(10):
    for j in range(10):
        if matrix[i][j] == None:
            print(' ', end='')
        elif type(matrix[i][j]) == str:
            print('*', end='')
        elif matrix[i][j] == 1:
            print('1', end='')
    print()
