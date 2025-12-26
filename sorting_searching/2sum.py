import sys
input=sys.stdin.readline

n,target=map(int, input().split())
arr=list(map(int, input().split()))
pairs=[(i+1, arr[i]) for i in range(n)]
pairs=sorted(pairs, key=lambda x: x[1])


i=0
j=n-1
while i<j:
    s=pairs[i][1]+pairs[j][1]
    if s==target:
        print(pairs[i][0], pairs[j][0])
        break

    elif s>target:
        j-=1
    else:
        i+=1
else:
    print("IMPOSSIBLE")
