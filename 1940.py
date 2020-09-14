# 주몽

import sys
input = sys.stdin.readline

# 재료의 개수
N = int(input())

# 갑옷을 만드는데 필요한 수
M = int(input())

check = [0] * 100001

array = list(map(int, input().split()))

array.sort()


start = 0
end = len(array) - 1
answer = 0

while start < end:
    if array[start] + array[end] == M:
        answer += 1
        start += 1
        end -= 1

    elif array[start] + array[end] < M:
        start += 1

    elif array[start] + array[end] > M:
        end -= 1


print(answer)





