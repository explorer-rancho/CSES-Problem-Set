t=int(input())
deadlines=0
durations=[0]*t

for i in range(t):
    a,d=map(int, input().split())
    deadlines+=d
    durations[i]=a

durations.sort()
s=durations[0]
for i in range(1,t):
    durations[i]=durations[i]+durations[i-1]
    s+=durations[i]

print(deadlines-s)





