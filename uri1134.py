print("MUITO OBRIGADO")
al=0
gs=0
di=0
while True:
    a=int(input())
    if a>0 and a<5:
        if a==1:
            al=al+1
        if a==2:
            gs=gs+1
        if a==3:
            di=di+1
        if a==4:
            break
    else:
        continue
print("Alcool: " +str(al))
print("Gasolina: " +str(gs))
print("Diesel: " +str(di))
