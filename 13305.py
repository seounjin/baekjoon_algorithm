# 주유소
import sys
input = sys.stdin.readline

N = int(input())

# 도로의 길이
road = list(map(int, input().split()))

# 도시당 가격
city = list(map(int, input().split()))

road_len = sum(road)
road += [0]
answer = [0] * 100000

answer[0] = city[0] * road[0]
temp = city[0]

for i in range(1, N):
    temp = min(temp, city[i])

    answer[i] = answer[i - 1] + temp * road[i]

print(answer[N - 1])