n,k=map(int, input().split())
x,a,b,c=map(int, input().split())
 
arr=[0]*n
arr[0]=x
t=x
 
for i in range(1,k):
	arr[i]=(a*arr[i-1]+b)%c
	t^=arr[i]
	
ans=t
 
for i in range(k,n):
	arr[i]=(a*arr[i-1]+b)%c
	t=t^arr[i-k]^arr[i]
	ans^=t
	
print(ans)
