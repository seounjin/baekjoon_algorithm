# 최소비용 구하기

import sys
import heapq

input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
check = [0] * (N + 1)

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

start, end = map(int, input().split())

for i in range(1, N + 1):
    check[i] = 100000000

h = []
check[start] = 0
heapq.heappush(h, (check[start], start))

while h:
    info = heapq.heappop(h)
    weight = info[0]
    node = info[1]

    for g in graph[node]:
        w = g[1]
        n = g[0]

        if check[n] > check[node] + w:
            check[n] = check[node] + w
            heapq.heappush(h, (check[n], n))


print(check[end])