
N1,N2,N3,N4 = map(float,input().split())

nota_exame = 0.0
MEDIA = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

print('Media: %.1f' %MEDIA)

if(MEDIA >= 7.0):
    print("Aluno aprovado.")

if(MEDIA < 5.0):
    print("Aluno reprovado.")

if(MEDIA >= 5.0 and MEDIA <= 6.9):
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame: %.1f" %nota_exame)
    MEDIA = (MEDIA + nota_exame)/2
    
    if(MEDIA >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print('Media final: %.1f' %MEDIA)
'''val = input().split()
N1 = float(N1)
N2 = float(N1)
N3 = float(N1)
N4 = float(N1)

ki = (N1*2+N2*3+N3*4+N4)/10
print("Media:",ki)
if ki >= 7.0:
    print("Aluno aprovado.")
elif ki >= 5.0:
    print("Aluno em exame.")
    a=float(input())
    print("Nota do exame:",a)
    if (a + ki/2) > 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final:",(a+ki)/2.0)    
else:
    print("Aluno reprovado.")'''
    
    
