# 격자상의 경로
# 로봇은 한번에 오른쪽에 인접한 칸또는 아래에 인전한 칸으로 이동
# 격자에 동그라미로 표시된 칸이 있는 경우 로봇은 반드시 지나야함

N, M, K = map(int, input().split())

dp = [(M+1)*[0] for _ in range(N+1)]

x = 1
y = 1
cnt = 0
flag = 0
for i in range(N):
    ex = 0
    for j in range(M):
        cnt += 1
        if cnt == K:
            x += i
            y += j
            flag = 1
            break
    if flag == 1:
        break

dp[1][0] = 1
trace = 0

for i in range(1, N+1):  # x
    for j in range(1, M+1):  # y
        if i-1 == x and j == y:
            trace = 2

        if trace is 0:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        if trace is 1:
            dp[i][j] = dp[i][j-1]

        if trace is 2:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        if i == x and j == y:
            trace = 1

print(dp[N][M])