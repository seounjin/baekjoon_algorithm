# 도서관

N, M = map(int, input().split())

array = list(map(int, input().split()))

array.sort()

answer = 0

for i in range(0, N, M):
    if array[N-1-i] > 0:
        answer += array[N-1-i]

    if array[i] < 0:
        answer += (-array[i])

answer = answer*2 - max(abs(array[0]), abs(array[N-1]))
print(answer)