# 각 행에서 가장 작은 수를 찾고, 그 수들 중 가장 큰 값을 찾기

n, m = map(int, input().split())
result = 0

for i in range(n):
  data = list(map(int, input().split()))
  data_min = min(data)
  result = max(result, data_min)

print(result)