a=float(input())
if a>=0 and a<=2000:
    print("Isento")
elif a>2000 and a<=3000:
    x=a-2000
    tax=x*.08
    print("R$ %.2f"%tax)
elif a>3000 and a<=4500:
    x=a-3000
    tax=(.08*1000)+(x*.18)
    print("R$ %.2f"%tax)
else:
    x=a-4500
    tax=(.08*1000)+(.18*1500)+(.28*x)
    print("R$ %.2f"%tax)