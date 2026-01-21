from collections import deque
n,k=map(int, input().split())
x,a,b,c=map(int, input().split())

arr=[0]*n
arr[0]=x
window=deque()
window.append(x)

for i in range(1,k):
    arr[i]=(a*arr[i-1]+b)%c
    while window and window[-1]>arr[i]:
        window.pop()
    window.append(arr[i])

ans=window[0]
for i in range(k,n):
    arr[i]=(a*arr[i-1]+b)%c
    #pop the i-kth element
    if window and window[0]==arr[i-k]:
        window.popleft()
    #add arr[i]
    while window and window[-1]>arr[i]:
        window.pop()
    window.append(arr[i])
    ans=ans^window[0]

print(ans)