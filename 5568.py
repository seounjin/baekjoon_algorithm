# 카드 놓기

# 두가지 방법

from itertools import permutations

n = int(input())
k = int(input())

array = []

for _ in range(n):
    array.append(input())

a = list(permutations(array, k))

answer = set([''.join(i) for i in a])
print(len(answer))


###########################################


n = int(input())
k = int(input())

array = []

for _ in range(n):
    array.append(input())

answer = []
check = [False] * n
def solution(cnt, N):

    if cnt == k:
        answer.append(N)
        return
    else:
        for i in range(n):
            if check[i] == False:
                check[i] = True
                solution(cnt + 1, N + array[i])
                check[i] = False


solution(0, '')
print(set(answer))
print(len(set(answer)))