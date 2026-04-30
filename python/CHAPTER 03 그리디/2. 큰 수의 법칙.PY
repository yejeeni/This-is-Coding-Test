# 배열의 크기 n. m=8, k=3 이면 6+6+6+5+6+6+6+5
# m번 더하는데 중복은 k번만 가능

n, m, k = map(int, input().split())
list = list(map(int, input().split()))

list.sort()
first = list[n-1]
second = list[n-2]

first_sum_count = int((m / k)) * k

sum = 0
sum += first_sum_count * first
sum += (m - first_sum_count) * second

print(sum)