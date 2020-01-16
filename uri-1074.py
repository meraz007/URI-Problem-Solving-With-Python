N = int (input())
list =[]
i = 1
while i<=N:
    M =int(input())
    list.append(M)
    i= i +1
for j in list:    
    if j %2 ==0 and j < 0:
        print("EVEN NEGATIVE")
    elif j % 2==1 and j <0:
        print("ODD NEGATIVE")
    elif j == 0:
        print("NULL")
    elif j % 2 ==1:
        print("ODD POSITIVE")
    elif j% 2==0:
        print("EVEN POSITIVE")
