# 게으른 백곰
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

array = [0] * 1000001

for _ in range(N):
    g, x = map(int, input().split())
    array[x] = g

L = K*2 + 1
save, answer = 0, 0

if K < 1000001:

    # 첨에 더함
    for i in range(L):
        save += array[i]

    # 그 뒤 윈도우 슬라이딩

    for i in range(L, 1000001):
        save -= array[i - L]
        save += array[i]
        answer = max(answer, save)

    print(answer)
else:
    print(sum(array))
