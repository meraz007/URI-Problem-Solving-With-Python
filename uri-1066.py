ev =0
od =0
po = 0
ne = 0
i = 1
while i<=5:
    x = int(input())
    if x %2==0:
        ev +=1
    else:
        od +=1
    if x >0:
        po +=1
    if x<0:
        ne +=1
    i = i+1
print(ev,"valor(es) par(es)")
print(od,"valor(es) impar(es)")
print(po,"valor(es) positivo(s)")
print(ne,"valor(es) negativo(s)")

