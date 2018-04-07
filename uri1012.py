a,b,c=input().split()
a,b,c=float(a),float(b),float(c)

area=.5*a*c
print("TRIANGULO: %.3f"%area)

area_c=3.14159*c*c
print("CIRCULO: %.3f"%area_c)

area_t=.5*(a+b)*c
print("TRAPEZIO: %.3f"%area_t)

area_s=b*b
print("QUADRADO: %.3f"%area_s)

area_r=a*b
print("RETANGULO: %.3f"%area_r)