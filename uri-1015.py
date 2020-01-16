import math
linha1 = (input()).split()
linha2 = (input()).split()
x1,y1 =linha1
x2,y2 =linha2
p1 = float(x2)-float(x1)
p2 = p1**2
q1 = float(y2)-float(y1)
q2 = q1**2
s =p2 +q2
w = math.sqrt(s)
print("%0.4f" %w)

