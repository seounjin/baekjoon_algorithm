# 문제집

import sys
import heapq

input = sys.stdin.readline


N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]
check = [0] * (N+1)
h = []
answer = []

for x, y in array:
    graph[x].append(y)
    check[y] += 1

for index in range(1, N + 1):
    if check[index] == 0:
        heapq.heappush(h, (index))

while h:
    i = heapq.heappop(h)

    answer.append(i)
    for v in graph[i]:
        check[v] -= 1

        if check[v] == 0:
            heapq.heappush(h, (v))


print(' '.join(map(str, answer)))