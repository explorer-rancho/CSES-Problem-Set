n,t=map(int, input().split())
arr=list(map(int, input().split()))

s=0
cnt=0
l,r=0,0
flag=0

while l<=r:
    if not flag:
        s+=arr[r]
    
    if s==t:
        cnt+=1
        s-=arr[l]
        l+=1
    
    elif s>t:
        s-=arr[l]
        l+=1
        flag=1
        if r >= l:
            continue

    r+=1
    flag=0
    if r >= n:
        break
print(cnt)

