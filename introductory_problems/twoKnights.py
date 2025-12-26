import math
n=int(input())
print(0)
bad_locs=0

for i in range(1,n):
    print(math.comb((i+1)**2,2)-bad_locs)
    bad_locs+=8*i

    
