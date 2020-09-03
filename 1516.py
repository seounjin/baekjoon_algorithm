# 게임개발

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

array = [list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N + 1)]

check = [0] * (N+1)
answer = [0] * (N+1)

for index, info in enumerate(array):

    if len(info) == 2:
        answer[index + 1] = info[0]

    for i in range(1, len(info) - 1):
        # 1 -> 2
        graph[info[i]].append([index + 1, info[0]])
        check[index + 1] += 1

que = deque()

for i in range(1, N + 1):
    if check[i] == 0:
        que.append(i)

while que:
    v = que.popleft()

    for info in graph[v]:
        index = info[0]
        time = info[1]

        check[index] -= 1

        answer[index] = max(answer[index], answer[v] + time)

        if check[index] == 0:
            que.append(index)

print('\n'.join(list(map(str, answer[1:]))))