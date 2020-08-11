# 달팽이는 올라가고싶다

A, B, V = map(int, input().split())

left, right = 0, V

answer = 1000000001

while left <= right:
    mid = (left + right) // 2

    # 하루 + 마지막날 점심
    if V <= mid * (A - B) + A:
        answer = min(answer, mid + 1)
        right = mid - 1
    else:
        left = mid + 1

print(answer)
