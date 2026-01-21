#This was getting TLE with Cpython compiler
import sys
input=sys.stdin.readline
#idea is to use the largest coins but sometimes smaller coins gives optimal solutions too
#we can create an arr upto n tracking optimal ways to build k from 1 to n
#if we have optimal ways to build later numbers we can combine with coins to build the required n
n,x=map(int, input().split())
coins=list(map(int, input().split()))
dp=[int(1e9)]*(x+1)
dp[0]=0

for i in coins:
    for j in range(x-i+1):
        dp[i+j]=min(dp[i+j],1+dp[j])

print(dp[x] if dp[x]!=int(1e9) else -1)
