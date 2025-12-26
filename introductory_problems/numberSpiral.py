import sys
input=sys.stdin.readline

tests=int(input())
for i in range(tests):
    row,col=map(int, input().split())
    ref=max(row,col)

    ref_r,ref_c=0,0
    if ref%2==0:
        ref_r,ref_c=ref,1

    else:
        ref_r,ref_c=1,ref

    diff=abs(ref_r-row)+abs(ref_c-col)
    print(ref**2-diff)
