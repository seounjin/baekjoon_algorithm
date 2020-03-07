# 선긋기
import sys

N = int(sys.stdin.readline())

line = []

for i in range(N):
    line.append(list(map(int, sys.stdin.readline().strip().split())))

line.sort()
line_start = line[0][0]
line_end = line[0][1]

answer = 0
for index in range(1, len(line)):

    if line_end < line[index][0]:
        answer += (line_end - line_start)
        line_start = line[index][0]
        line_end = line[index][1]
    else:
        line_end = max(line[index][1], line_end)

answer += line_end - line_start
print(answer)