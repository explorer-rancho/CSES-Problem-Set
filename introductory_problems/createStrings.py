import math
def find_permutations(s: list, choosen=set(), p=[], prev=None,ans=[]):
    if len(p)==len(s):
        ans.append(p[:])
        return ans
    
    for i in range(len(s)):
        if prev and prev==s[i]:
            continue
        if i not in choosen:
            p.append(s[i])
            choosen.add(i)
            prev=s[i]
            #print(p,choosen)
            find_permutations(s)
            p.pop()
            choosen.remove(i)
    return ans


if __name__=="__main__":
    s=input()
    ls=list(s)
    ls.sort()
    ans=find_permutations(ls)
    print(len(ans))
    for i in ans:
        print("".join(i))
    
   