# 모든 순열

N = int(input())

def solution(array,cnt):

    if cnt == N:
        print(' '.join(map(str, array)))
        return
    else:
        for num in range(1, N + 1):
            if num not in array:
                solution(array + [num], cnt + 1)

solution([], 0)