x = float(input())
a=15
b= 12
c=10
d=7
e=4
if x > 0 and x <= 400:
    m = x * (a/100)
    n = x +m
    print("Novo salario: %0.2f"%n)
    print("Reajuste ganho: %0.2f"%m)
    print("Em percentual:",a,"%")
elif x >400 and x<=800:
    m = x * (b/100)
    n = x +m
    print("Novo salario: %0.2f"%n)
    print("Reajuste ganho: %0.2f"%m)
    print("Em percentual:",b,"%")
elif x >800 and x<=1200:
    m = x * (c/100)
    n = x +m
    print("Novo salario: %0.2f"%n)
    print("Reajuste ganho: %0.2f"%m)
    print("Em percentual:",c,"%")
elif x >1200 and x<=2000:
    m = x * (d/100)
    n = x +m
    print("Novo salario: %0.2f"%n)
    print("Reajuste ganho: %0.2f"%m)
    print("Em percentual:",d,"%")
elif x >2000 :
    m = x * (e/100)
    n = x +m
    print("Novo salario: %0.2f"%n)
    print("Reajuste ganho: %0.2f"%m)
    print("Em percentual:",e,"%")
