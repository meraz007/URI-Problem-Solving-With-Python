i = 0
while True:
    X,Y = map(int,input().split())
    if X >Y:
        print("Decrescente")
    elif X<Y:
        print("Crescente")
    elif X==Y:
        break
    
