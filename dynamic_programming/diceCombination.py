inp=int(input())
dp=[0]*inp
dp[0]=1
s=1
for i in range(1,inp):
    if i<=5:
        dp[i]=s+1
    else:
        s-=dp[i-7]
        dp[i]=s%(10**9+7)
    s+=dp[i]

print(dp[inp-1])

