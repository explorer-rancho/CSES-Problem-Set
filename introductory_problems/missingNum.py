import sys

input=sys.stdin.readline

def main():
    n=int(input())
    ans=(n*(n+1))//2-sum(list(map(int, input().split())))
    return ans

print(main())
