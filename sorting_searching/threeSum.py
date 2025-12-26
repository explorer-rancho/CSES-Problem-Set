n, target=map(int, input().split())
arr=list(map(int, input().split()))
mapp=[(i,arr[i]) for i in range(n)]
mapp=sorted(mapp, key=lambda x: x[1])
arr=[mapp[i][1] for i in range(n)]
mapp={j:mapp[j][0] for j in range(n)}

for i in range(n):
    t=target-arr[i]
    j=i+1
    k=n-1
    flag=0
    
    while j<k:
        s=arr[j]+arr[k]
        if s==t:
            flag=1
            break
        elif s>t:
            k-=1
        else:
            j+=1
    if flag:
        print(mapp[i]+1,mapp[j]+1,mapp[k]+1)        
        break
    continue
else:
    print("IMPOSSIBLE")



