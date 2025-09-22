import sys
input=sys.stdin.readline

n=int(input())
arr=map(int, input().split())
freq=set()
count=0
for i in arr:
    if i not in freq:
        freq.add(i)
        count+=1

print(count)

