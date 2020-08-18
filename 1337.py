# 올바른 배열

N = int(input())

array = []
for _ in range(N):
    array.append(int(input()))

def solution():
    array.sort()

    cnt = 1
    start = 0
    answer = 1

    for i in range(1, N):

        cnt += 1
        while array[i] - array[start] > 4:
            start += 1
            cnt -= 1

        answer = max(answer, cnt)

    if cnt > 5:
        print(5)
        return

    print(5 - answer)

solution()
