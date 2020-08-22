import sys
sys.setrecursionlimit(500000000)
input = sys.stdin.readline


N, r1, r2 = map(int, input().split())

graph = [[] for _ in range(100001)]
check = [False] * 100001

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

trace = False
def solution(start, answer, m_weight):
    global trace

    if trace:
        return

    if start == r2:
        print(answer - m_weight)
        trace = True
        return

    check[start] = True

    for info in graph[start]:
        v = info[0]
        w = info[1]

        if check[v] == False:
            solution(v, answer + w, max(m_weight, w))


if N == 1:
    print(0)
elif N == 2:
    print(0)
else:
    solution(r1, 0, 0)