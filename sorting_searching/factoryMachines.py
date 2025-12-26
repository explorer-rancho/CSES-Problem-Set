import sys,math
input=sys.stdin.readline

def sufficient(time,produce):
    return sum(time//i for i in durations)>=produce

n,total=map(int, input().split())
durations=list(map(int, input().split()))

l=0
r=durations[0]*total
m=l
while l<=r:
    m=(l+r)//2
    if sufficient(m,total):
        r=m-1

    else:
        if sufficient(m+1, total):
            print(m+1)
            break
        l=m+1

else:
    print(l)