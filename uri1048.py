a=float(input())
x15=a*.15
x12=a*.12
x10=a*.1
x7=a*.07
x4=a*.04
if a>=0 and a<=400:
    a15=a+x15
    print("Novo salario: %.2f"%a15)
    print("Reajuste ganho: %.2f"%x15)
    print("Em percentual: 15 %")
elif a>400 and a<=800:
    a12=a+x12
    print("Novo salario: %.2f"%a12)
    print("Reajuste ganho: %.2f"%x12)
    print("Em percentual: 12 %")
elif a>800 and a<=1200:
    a10=a+x10
    print("Novo salario: %.2f"%a10)
    print("Reajuste ganho: %.2f"%x10)
    print("Em percentual: 10 %")
elif a>1200 and a<=2000:
    a7=a+x7
    print("Novo salario: %.2f"%a7)
    print("Reajuste ganho: %.2f"%x7)
    print("Em percentual: 7 %")
else:
    a4=a+x4
    print("Novo salario: %.2f"%a4)
    print("Reajuste ganho: %.2f"%x4)
    print("Em percentual: 4 %")