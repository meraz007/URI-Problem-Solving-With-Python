N = int(input())
list =[]
count_in = 0
count_out = 0
i = 1
while i<=N:
    X = int(input())
    list.append(X)
    i = i+1
for j in list:
    if j >=10 and j <=20:
        count_in +=1
    else:
        count_out +=1
      
print(count_in,"in")
print(count_out,"out")
