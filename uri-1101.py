sum = 0
list=[]
M,N = map(int,input().split())
for i in range(N,M+1):
    sum +=i
    list.append(i)
print(list[0],"Sum=%d" %sum)
    
