# Yonsei TOTO

import sys
input = sys.stdin.readline

room = []
temp = []
answer = 0

# 과목수 , 마일리지
n, m = map(int, input().split())

for i in range(n):
    # 신청한 사람수, 수강인원
    P, L = map(int, input().split())

    room.append(list(map(int, input().split())))

    if P < L:
        temp.append(1)
    else:
        room[i].sort(reverse=True)
        temp.append(room[i][L - 1])


temp.sort()

for i in range(len(temp)):
    if m < temp[i]:
        break
    else:
        m = m - temp[i]
        answer += 1

print(answer)


