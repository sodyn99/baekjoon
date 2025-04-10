S = list(input())

cnt = 0
for s in range(1, len(S)):
  if S[s] != S[s-1]:
    cnt += 1

if cnt - 1 >= 0:
  cnt /= 2
  if cnt > int(cnt):
    cnt += 1

print(int(cnt))