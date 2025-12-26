n=int(input())
print(2**n - 1)
if n==1:
    print(1,3)
else:
    ls=[[1,3]]
    for i in range(1,n):
        for i in ls:
            if i[0]==2 or i[0]==3:
                if i[0]==2:
                    i[0]+=1
                else:
                    i[0]-=1
            if i[1]==2 or i[1]==3:
                if i[1]==2:
                    i[1]+=1
                else:
                    i[1]-=1
        ls.append([1,3])
        for i in range(len(ls)-1):
            ls.append([ls[i][0]+1 if ls[i][0] != 3 else 1 , ls[i][1]+1 if ls[i][1] != 3 else 1])

    for i in ls:
        print(*i)