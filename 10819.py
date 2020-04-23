# 차이를 최대로
import sys
N = int(input())

array = list(map(int, input().split()))

answer = -sys.maxsize
def solution(num, cnt):
    global answer
    if N == cnt:
        cmp = 0
        for i in range(N - 1):
            cmp += abs(array[num[i]] - array[num[i+1]])
        answer = max(answer, cmp)
        return
    else:
        for n in range(N):
            if n not in num:
                solution(num + [n], cnt+1)

solution([], 0)

print(answer)