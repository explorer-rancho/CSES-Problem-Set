import sys

input=sys.stdin.readline
n=int(input())
arr=list(map(int, input().split()))

max_sum=arr[0]
min_sum=0
running_sum=0
#using prefix sums

for i in arr:
    running_sum+=i
    max_sum=max(max_sum,running_sum-min_sum)
    min_sum=min(min_sum,running_sum)

print(max_sum)