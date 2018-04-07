import math
a,b,c=input().split()
a,b,c=float(a),float(b),float(c)
pithaok=b*b-4*a*c

if a!=0 and pithaok>0 :
	r1=(-b + math.sqrt(pithaok))/(2*a)
	r2=(-b - math.sqrt(pithaok))/(2*a)
	print("R1 = %.5f"%r1)
	print("R2 = %.5f"%r2)
else:
	print("Impossivel calcular")