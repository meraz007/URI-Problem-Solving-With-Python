x = eval(input())
x = float("%.2f" % x)

hun = int(x /100)
fif = int((x-(hun*100))/50)
twn = int((x - (hun*100)-(fif*50))/20)
ten = int((x - (hun*100)-(fif*50)-(twn*20))/10)
fiv = int((x - (hun*100)-(fif*50)-(twn*20)-(ten*10))/5)
two = int((x - (hun*100)-(fif*50)-(twn*20)-(ten*10)-(fiv*5))/2)

one = int((x - (hun*100)-(fif*50)-(twn*20)-(ten*10)-(fiv*5)-(two*2))/1)
point_five = int((x - (hun*100)-(fif*50)-(twn*20)-(ten*10)-(fiv*5)-(two*2)-(one*1))/0.50)
point_tf = int((x - (hun*100)-(fif*50)-(twn*20)-(ten*10)-(fiv*5)-(two*2)-(one*1)-(point_five*.50))/0.25)
point_t = int((x - (hun*100)-(fif*50)-(twn*20)-(ten*10)-(fiv*5)-(two*2)-(one*1)-(point_five*.50)-(point_tf*.25))/0.10)
point_of = int((x - (hun*100)-(fif*50)-(twn*20)-(ten*10)-(fiv*5)-(two*2)-(one*1)-(point_five*.50)-(point_tf*.25)-(point_t*.10))/0.05)
point_oo = int((x - (hun*100)-(fif*50)-(twn*20)-(ten*10)-(fiv*5)-(two*2)-(one*1)-(point_five*.50)-(point_tf*.25)-(point_t*.10)-(point_of*0.05))/0.01)

print("NOTAS:")
print ("%d nota(s) de R$ 100.00" %hun)
print ("%d nota(s) de R$ 50.00" %fif)
print ("%d nota(s) de R$ 20.00" %twn)
print ("%d nota(s) de R$ 10.00" %ten)
print ("%d nota(s) de R$ 5.00" %fiv)
print ("%d nota(s) de R$ 2.00" %two)
print("MOEDAS:")
print ("%d moeda(s) de R$ 1.00" %one)
print ("%d moeda(s) de R$ 0.50" %point_five)
print ("%d moeda(s) de R$ 0.25" %point_tf)
print ("%d moeda(s) de R$ 0.10" %point_t)
print ("%d moeda(s) de R$ 0.05" %point_of)
print ("%d moeda(s) de R$ 0.01" %point_oo)
