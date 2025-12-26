def main():
    t=int(input())
    for _ in range(t):
        a,b=map(int, input().split())
        #(2k1 + k2, 2k2 + k1)=(a,b) find k1 and k2
        k1=(2*a-b)
        k2=(4*b-2*a)

        if k1%3==0 and k2%6==0 and k1>=0 and k2>=0:
            print('YES')
        else:
            print('NO')


if __name__=="__main__":
    main()