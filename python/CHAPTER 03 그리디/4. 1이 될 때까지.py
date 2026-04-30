# N에서 1을 빼거나
# N을 K로 나누거나 (나누어 떨어질 때만)
# 최소 횟수 구하기

n, k = map(int, input().split())
count = 0

while (True):
  if (n==0):
    break

  mod = n % k

  if (mod != 0):
    n -= mod
    count += mod
  else:
    n = int (n / k)
    count += 1

print(count-1)