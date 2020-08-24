# 친구
from collections import deque

N = int(input())

array = []
for i in range(N):
    array.append(list(input()))

graph = [[] for _ in range(N + 1)]

for i in range(N):
    for j in range(N):
        if array[i][j] == 'Y':
            graph[i + 1].append(j + 1)


def solution(v):

    check = [False] * (N + 1)

    que = deque()
    que.append([v, 0])

    check[v] = True
    cnt = 0
    while que:

        a, b = que.popleft()

        if b > 2:
            continue

        if b == 1 or b == 2:
            cnt += 1

        for g in graph[a]:
            if check[g] == False:
                check[g] = True
                que.append([g, b + 1])

    return cnt

answer = 0

for i in range(N):
    answer = max(answer, solution(i + 1))

print(answer)