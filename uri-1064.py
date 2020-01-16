c = 0
a=0
i =1
while i <=6:
    x = float(input())
    if x >0:
        c +=1
        a +=x
    i = i+1
avg = a/c
print(c,"valores positivos")
print("%.1f"%avg)
        
