# DNA 비밀번호

S, P = map(int, input().split())

DNA = input()

A, C, G, T = map(int, input().split())

dic = {}
dic['A'] = A
dic['C'] = C
dic['G'] = G
dic['T'] = T

answer = 0

for i in range(P):
    dic[DNA[i]] -= 1

if dic['A'] <= 0 and dic['C'] <= 0 and dic['G'] <= 0 and dic['T'] <= 0:
    answer += 1

for i in range(P, S):
    dic[DNA[i]] -= 1
    dic[DNA[i - P]] += 1

    if dic['A'] <= 0 and dic['C'] <= 0 and dic['G'] <= 0 and dic['T'] <= 0:
        answer += 1


print(answer)