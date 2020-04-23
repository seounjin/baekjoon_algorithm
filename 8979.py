# 올림픽
N, K = map(int, input().split())

array = []
a = 0
b = 0
c = 0
for _ in range(N):
    q, w, e, r = map(int, input().split())
    if q == K:
        a = w
        b = e
        c = r
    array.append([q,w,e,r])

array.sort(key=lambda a:(a[1],a[2],a[3]),reverse=True)

cnt = 1
for index, o in enumerate(array):
    if o[1] == a and o[2] == b and o[3] == c:
        print(cnt)
        break
    cnt += 1