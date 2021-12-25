matrix = []
for i in range(10):
    matrix.append([None]*10)
matrix[0][9] = '2'
matrix[1][1] = '3,1'
matrix[1][5] = '4,2'
matrix[3][3] = '2,2,1'
matrix[3][8] = '3,3'
matrix[4][0] = '4,2'
matrix[4][5] = '3,1,1'
matrix[6][3] = '4,2'
matrix[6][7] = '2,4'
matrix[7][1] = '2,3'
matrix[7][9] = '2'
matrix[8][6] = '2,2'
matrix[9][4] = '4'
# matrix[1][8] = 1


def output(a, b):
    if matrix[a][b] == None:
        return '?'
    elif type(matrix[a][b]) == str:
        return '*'
    elif matrix[a][b] == 0:
        return '0'
    elif matrix[a][b] == 1:
        return '1'


def check(a, b):
    if type(matrix[a][b]) == str:
        info = []
        flag = 0
        exist_ranges = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        surroundings = [[a-1, b-1], [a-1, b], [a-1, b+1],
                        [a, b+1], [a+1, b+1], [a+1, b], [a+1, b-1], [a, b-1]]
        for i in surroundings:
            if i[0] not in exist_ranges or i[1] not in exist_ranges:
                flag = 1
                break
            info.append(i)
        if flag == 1:
            for i in reversed(surroundings):
                if i[0] not in exist_ranges or i[1] not in exist_ranges:
                    flag = 2
                    break
                info.insert(0, i)
        if flag == 2:
            for i in surroundings:
                if i[0] in exist_ranges and i[1] in exist_ranges:
                    info.append(i)
        for i in range(len(info)):
            print(info[i], end='')


for i in range(10):
    for j in range(10):
        print(output(i, j), end='')
    print()

check(4, 0)
