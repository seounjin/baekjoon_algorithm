# 색종이

import sys
N = int(sys.stdin.readline())
array = []

for _ in range(N):
    array.append(list(map(int, input().split())))

area = [[0]*101 for _ in range(101)]

answer = [0]*(N+1)

cnt = 1
for s in array:
    a = s[0]
    b = s[1]
    c = s[2] + s[0]
    d = s[3] + s[1]
    for i in range(a, c):
        for j in range(b, d):
            area[i][j] = cnt

    cnt += 1

for i in range(101):
    for j in range(101):
        if area[i][j] != 0:
            answer[area[i][j]] += 1

for i in range(1,N+1):
    print(answer[i])