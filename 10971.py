# 외판원 순회2
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())

array = [list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if array[i][j] == 0:
            continue

        graph[i].append([j, array[i][j]])


check = [False] * N
result = sys.maxsize
def solution(i, cnt, answer, first):
    global result

    if cnt == N and first == i:
        result = min(result, answer)
        return

    for info in graph[i]:
        v = info[0]
        w = info[1]

        if not check[v]:
            check[v] = True
            if w + answer < result:
                solution(v, cnt + 1, w + answer, first)
            check[v] = False


solution(0, 0, 0, 0)

print(result)
