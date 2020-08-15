# 지뢰찾기

N = int(input())

array = []

for _ in range(N):
    array.append(list(input()))

dx = [1,-1,0,0, 1, -1, 1, -1]
dy = [0,0,1,-1, -1, -1, 1, 1]

answer = 0

def solution(x ,y):

    for i in range(8):
        ex, ey = x + dx[i], y + dy[i]
        if array[ex][ey] == '0':
            array[x][y] = ''
            return False
    return True


for i in range(1, N - 1):
    for j in range(1, N - 1):

        if solution(i, j):
            for index in range(8):
                ex, ey = i + dx[index], j + dy[index]
                if array[ex][ey] > '0' and array[ex][ey] <= '3':
                    array[ex][ey] = str(int(array[ex][ey]) - 1)

for i in range(1, N - 1):
    for j in range(1, N - 1):
        if array[i][j] == '#':
            answer += 1

print(answer)