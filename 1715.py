# 카드 정렬하기

import sys
import heapq

input = sys.stdin.readline

N = int(input())

h = []
for _ in range(N):
    heapq.heappush(h, (int(input())))

answer = 0
while h:
    if len(h) == 1:
        break
    else:
        n = heapq.heappop(h)
        m = heapq.heappop(h)
        answer += (n+m)
        heapq.heappush(h, (n + m))


print(answer)
