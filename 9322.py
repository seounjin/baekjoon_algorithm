# 철벽보안알고리즘

a = int(input())

for i in range(a):
    b = int(input())
    one = list(map(str, input().split()))
    two = list(map(str, input().split()))
    password = list(map(str, input().split()))

    dic = {}
    for i in range(b):
        dic[one[i]] = i

    check = [0] * b

    for i in range(b):
        check[i] = dic[two[i]] - i

    answer = [''] * b

    for i in range(b):
        answer[i + check[i]] = password[i]

    print(' '.join(answer))