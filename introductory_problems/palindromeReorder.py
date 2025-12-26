from collections import Counter
def main():
    s=input()
    cnt=Counter(s)
    ans=""
    k=0
    mid=""
    for i in cnt.keys():
        if cnt[i]%2!=0:
            k+=1
            mid=i*cnt[i]
            if k>=2:
                print('NO SOLUTION')
                return
        else:  
            ans+=i*(cnt[i]//2)
        
    print(ans+mid+ans[::-1])
        
    
if __name__=="__main__":
    main()