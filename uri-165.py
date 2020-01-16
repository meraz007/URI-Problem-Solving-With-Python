a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
count = 0
if (a%2 ==0):
    count +=1
else:
    count +=0
if (b%2 ==0):
    count +=1
else:
    count +=0
if (c%2 ==0):
    count +=1
else:
    count +=0
if (d%2 ==0):
    count +=1
else:
    count +=0
if (e%2 ==0):
    count +=1
else:
    count +=0
'''lista = [a,b,c,d,e]
i = 0
while(i < len(lista)):
    if (lista[i] %2 ==0):
        count +=1
    i = i+1'''
print("%d valores pares" %count)    
