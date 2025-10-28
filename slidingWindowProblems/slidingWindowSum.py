n,k=map(int, input().split())
x,a,b,c=map(int, input().split())
s=x
arr=[0]*n
arr[0]=x

for i in range(1,k):
    arr[i]=(a*arr[i-1]+b)%c
    s+=arr[i]

ans=s
for i in range(k,n):
    arr[i]=(a*arr[i-1]+b)%c
    s=s-arr[i-k]+arr[i]
    ans^=s

print(ans)

        
        

    
    
    
    