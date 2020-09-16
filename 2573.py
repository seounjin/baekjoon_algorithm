# 빙산

import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

# 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
# 두 덩이리 이상으로 분리

def ice_check(x, y, check):

    cnt = 0

    for i in range(4):
        ex, ey = x + dx[i], y + dy[i]

        if ex < 0 or ey < 0 or ex >= N or ey >= M:
            continue

        if array[ex][ey] == 0 and not check[ex][ey]:
            cnt += 1

    return cnt

def solution(i, j, check):

    que = deque()

    que.append([i, j])
    check[i][j] = True

    while que:
        x, y = que.popleft()

        cnt = ice_check(x, y, check)

        if array[x][y] - cnt < 0:
            array[x][y] = 0
        else:
            array[x][y] -= cnt

        for i in range(4):
            ex, ey = x + dx[i], y + dy[i]

            if ex < 0 or ey < 0 or ex >= N or ey >= M:
                continue

            if check[ex][ey] == False and array[ex][ey]:
                check[ex][ey] = True
                que.append([ex, ey])

    return 1

answer = 0
while True:
    cnt = 0
    check = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if array[i][j] and not check[i][j]:
                cnt += solution(i, j, check)

    answer += 1

    if cnt >= 2:
        print(answer - 1)
        break
    elif cnt == 0:
        print(0)
        break

