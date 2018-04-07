import math
a,b=input().split()
c,d=input().split()
a,b,c,d=float(a),float(b),float(c),float(d)
x=math.fabs(a-c)
y=math.fabs(d-b)
r=x*x
t=y*y
z=math.sqrt(r+t)
print("%.4f"%z)