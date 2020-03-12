# 알파벳
import sys
input = sys.stdin.readline

# 오른쪽,왼쪽,위,아래
dx = [1,-1,0,0]
dy = [0,0,-1,1]

N, M = map(int, input().split())

alp = set()

array = [list(input().rstrip()) for _ in range(N)]

answer = 1
dic = {}
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for index in range(26):
    dic[a[index]] = 0

def dfs(x, y,cnt):
    global answer

    dic[array[x][y]] = 1
    for i in range(4):
        ex, ey = x + dx[i], y + dy[i]
        if ex >= 0 and ey >= 0 and ex < N and ey < M and dic[array[ex][ey]] == 0:
            dic[array[ex][ey]] = 1
            dfs(ex, ey, cnt+1)
            dic[array[ex][ey]] = 0
            answer = max(answer, cnt+1)

dfs(0, 0, 1)  # x,y,cnt

print(answer)