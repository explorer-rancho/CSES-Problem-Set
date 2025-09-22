import sys
input=sys.stdin.readline

def main():
    s=input()
    mx=1
    ans=1

    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            mx+=1
            if mx>ans:
                ans=mx
        else:
            mx=1
    return ans

    
print(main())
