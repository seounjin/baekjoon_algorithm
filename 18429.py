# 근손실
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

array = list(map(int, input().split()))

check = [False] * N

answer = 0
def solution(cnt, weight):
    global answer

    if cnt == N:
        answer += 1
        return
    else:
        for i in range(N):
            if check[i] == False:
                check[i] = True

                if weight + array[i] - K >= 500:

                    solution(cnt + 1, weight + array[i] - K)

                check[i] = False

solution(0, 500)
print(answer)