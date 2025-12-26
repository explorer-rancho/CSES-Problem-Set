import sys

input=sys.stdin.readline

n=int(input())


if 1<n<=3:
    print('NO SOLUTION')

else:
    x=n-1 if n%2==0 else n
    y=n if n%2==0 else n-1

    for i in range(x,0,-2):
        print(i, end=" ")
    for i in range(y,0,-2):
        print(i, end=" ")

    print()
