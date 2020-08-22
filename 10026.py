from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())

array = []

for _ in range(N):
    array.append(list(input()))


check = [[False] * N for _ in range(N)]

def solution(x ,y, color):

    check[x][y] = True
    que = deque()
    que.append([x, y])

    while que:
        x, y = que.popleft()
        for i in range(4):
            ex, ey = x + dx[i], y + dy[i]
            if ex >= 0 and ey >= 0 and ex < N and ey < N:
                if check[ex][ey] == False and array[ex][ey] == color:
                    check[ex][ey] = True
                    que.append([ex, ey])

    return 1

def solution2(x ,y, color):

    check[x][y] = True
    que = deque()
    que.append([x, y])

    while que:
        x, y = que.popleft()
        for i in range(4):
            ex, ey = x + dx[i], y + dy[i]
            if ex >= 0 and ey >= 0 and ex < N and ey < N:
                if color == 'B':
                    if check[ex][ey] == False and array[ex][ey] == color:
                        check[ex][ey] = True
                        que.append([ex, ey])
                else:
                    if check[ex][ey] == False and array[ex][ey] != 'B':
                        check[ex][ey] = True
                        que.append([ex, ey])


    return 1


case_1 = 0
case_2 = 0

for i in range(N):
    for j in range(N):
        if check[i][j] == False:
            case_1 += solution(i, j, array[i][j])


check = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if check[i][j] == False:
            case_2 += solution2(i, j, array[i][j])

print(case_1, case_2)