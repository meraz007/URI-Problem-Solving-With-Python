c =0
total_a = 0

while True:
    x = int(input())
    if x<0:
        break
    else:
        c +=1
        total_a +=x
avg = total_a / c
print("%0.2f" %avg)
