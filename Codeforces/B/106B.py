from sys import*
input= stdin.readline
t=int(input())
l=[]
cost=[]
for i in range(t):
    a,b,c,d=map(int,input().split())
    l.append([a,b,c])
    cost.append(d)
for i in range(t):
    for j in range(t):
        if(i!=j):
            if(l[i][0]<l[j][0] and l[i][1]<l[j][1] and l[i][2]<l[j][2]):
                cost[i]=10000
                break
print(cost.index(min(cost))+1)