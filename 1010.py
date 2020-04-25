# 다리 놓기
N = int(input())

array = [[0] * 31 for _ in range(31)]


def cal():
    for i in range(1, 31):
        array[1][i] = i

    for i in range(2, 31):
        for j in range(i, 31):
            for k in range(j, i-1, -1):
                array[i][j] += array[i - 1][k-1]

cal()

for i in range(N):
    a, b = map(int, input().split())
    print(array[a][b])
