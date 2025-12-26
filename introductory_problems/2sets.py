def main():
    n=int(input())
    total_sum=n*(n+1)//2
    if total_sum%2 != 0:
        print('NO')

    else:
        #problem is to find a subsequence whose sum is equal to the half sum
        half_sum=total_sum//2
        print('YES')
        set1,set2=[],[]

        for i in range(n,0,-1):
            if i<=half_sum:
                set1.append(i)
                half_sum-=i
            else:
                set2.append(i)

        print(len(set1))
        print(*set1)
        print(len(set2))
        print(*set2)


if __name__=="__main__":
    main()