'''valor = input().split(" ")

a, b, c = valor
pi = 3.14159'''
import math

A,B,C=map(float,input().split())

tri = ((A*C)/2)
cir = math.pi *(C*C)
tra = C*((A+B)/2)
qua = B*B
ret =A*B
print("TRIANGULO: %.3f" % tri)
print("CIRCULO: %.3f" % cir)
print("TRAPEZIO: %.3f" % tra)
print("QUADRADO: %.3f" % qua)
print("RETANGULO: %.3f" % ret)
'''print("TRIANGULO: %0.3f\nCIRCULO: %0.3f\nTRAPEZIO: %0.3f\nQUADRADO: %0.3f\nRETANGULO: %0.3f" % (tri, cir, tra, qua, ret))
print(" TRIANGULO: %.3f\n" % tri)
print(" CIRCULO: %.3f\n" % cir)
print(" TRAPEZIO: %.3f\n" % tra)
print(" QUADRADO: %.3f\n" % qua)
print(" RETANGULO: %.3f\n" % ret)'''
