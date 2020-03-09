# 숫자판 점프

import sys
sys.setrecursionlimit(10**6)
#오른쪽,왼쪽,위,아래
dx = [1,-1,0,0]
dy = [0,0,1,-1]

line = []

for _ in range(5):
    line.append(list(map(str, sys.stdin.readline().strip().split())))

answer = set()

def solution(x, y, index,c):

    if index == 6:
        answer.add(c)
        return

    for i in range(4):
        ex, ey = x + dx[i], y + dy[i]
        if ex >= 0 and ey >= 0 and ex < 5 and ey < 5:
            solution(ex, ey, index+1, c + line[ex][ey])


for i in range(5):
    for j in range(5):
        solution(i, j, 0, "")

print(len(answer))