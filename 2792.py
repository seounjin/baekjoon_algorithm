# 보석 상자
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

box = []

for _ in range(M):
    box.append(int(input()))

answer = 1000000000

left = 1
right = max(box)

while left <= right:
    mid = (left + right) // 2

    people = 0

    for i in range(M):
        if box[i] % mid:
            people += (box[i] // mid) + 1
        else:
            people += box[i] // mid

    if people > N:
        left = mid + 1
    else:
        right = mid - 1
        answer = min(answer, mid)

print(answer)













