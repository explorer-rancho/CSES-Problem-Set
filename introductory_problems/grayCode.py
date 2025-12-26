def gray_codes(n):

    for i in range(2**n):
        print(f"{i^(i>>1):0{n}b}")
        

if __name__=="__main__":
    n=int(input())
    gray_codes(n)
