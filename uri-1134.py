alco = 0
gas = 0
dies = 0
while True:
    x = int(input())
    if x ==1:
        alco +=1
    elif x==2:
        gas +=1
    elif x==3:
        dies +=1
    elif x==4:
        break
       
print("MUITO OBRIGADO")
print("Alcool:",alco)
print("Gasolina:",gas)
print("Diesel:",dies)
