import sys

input=sys.stdin.readline

n=int(input())


if 1<n<=3:
    print('NO SOLUTION')

else:
    for i in range(1,n,2):
        print(i, end=" ")
    for i in range(2,n,-2):
        print(i,end=" ")

