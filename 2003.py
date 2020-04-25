# 수들의 합2

N, M = map(int, input().split())

array = list(map(int, input().split()))

first = 0
move = 0
s = 0
answer = 0

while first < N:
    if s == M:
        if move == N:
            answer += 1
            break
        else:
            answer += 1
            s += array[move]
            move += 1
    elif s > M:
        s -= array[first]
        first += 1
    else:
        if move == N:
            s -= array[first]
            first += 1
        else:
            s += array[move]
            move += 1

print(answer)