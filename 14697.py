# 방 배정하기

A, B, C, N = map(int, input().split())

DP = [1] + [0] * 400

for i in range(N):
    if DP[i] == 0:
        continue
    DP[i+A] = 1
    DP[i+B] = 1
    DP[i+C] = 1

print(DP[N])