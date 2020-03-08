# 알바생 강호
import sys

N = int(sys.stdin.readline())

array = []
for _ in range(N):
    array.append(int(sys.stdin.readline()))

# 월래 주려는 돈 - (받은등수 - 1)
# 돈이 큰순서로 정렬
array.sort(reverse=True)

answer = 0

for index in range(N):
    if array[index] - index > 0:
        answer += array[index] - index

print(answer)