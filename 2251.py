# 물통

import sys
from collections import deque

A, B, C = map(int, sys.stdin.readline().strip().split())

check = [[False] * 201 for _ in range(201)]
que = deque()
que.append([0, 0, C])
answer = []
while que:

    a, b, c = que.popleft()

    if check[b][c]:
        continue

    check[b][c] = True

    if a == 0:
        answer.append(c)

    # c에서 b 로 옮기기
    if c != 0 and b != B:
        if b+c > B:
            que.append([a, B, c-(B-b)])
        else:
            que.append([a, b+c, 0])

    # c에서 a로
    if c != 0 and a != A:
        if a + c > A:
            que.append([A, b, c-(A-a)])
        else:
            que.append([a+c, b, 0])

    # b에서 a
    if b != 0 and a != A:
        if a+b > A:
            que.append([A, b-(A-a), c])
        else:
            que.append([a+b, 0, c])

    # b에서 c
    if b != 0 and c != C:
        if b+c > C:
            que.append([a, b-(C-c), C])
        else:
            que.append([a, 0, b+c])

    # a에서 c
    if a != 0 and c != C:
        if a+c > C:
            que.append([a-(C-c), b, C])
        else:
            que.append([0, b, c+a])

    # a에서 b
    if a != 0 and b != B:
        if a+b > B:
            que.append([a-(B-b), B, c])
        else:
            que.append([0, b+a, c])


answer.sort()
for n in answer:
    print(n,end=' ')