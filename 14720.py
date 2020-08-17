# 우유축제

N = int(input())
array = list(map(int, input().split()))

dp = [[0] * 3 for _ in range(N)]

if array[0] == 0:
    dp[0][0] = 1

for i in range(1, N):
    milk = array[i]

    if milk == 0:
        dp[i][0] = dp[i - 1][2] + 1
    else:
        dp[i][0] = dp[i - 1][0]
    
    # 전에 까지 마셧던 우유 수량이 그 다음 먹을 우유 수량보다 작다면 먹을 필요가 없음  
    if milk == 1 and dp[i][2] < dp[i][0]:
        dp[i][1] = dp[i - 1][0] + 1
    else:
        dp[i][1] = dp[i - 1][1]

    if milk == 2 and dp[i][0] < dp[i][1]:
        dp[i][2] = dp[i - 1][1] + 1
    else:
        dp[i][2] = dp[i - 1][2]


print(max(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))
