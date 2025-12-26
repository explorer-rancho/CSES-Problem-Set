def main():
    n=int(input())
    ans=0
    i=1

    while (k:=n//(5**i))>=1:
        ans+=k
        i+=1
    print(ans)

if __name__=="__main__":
    main()