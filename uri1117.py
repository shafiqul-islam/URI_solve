c=0
sum=0
while c<2:
    
    a=float(input())
    if a<0 or a>10:
        print("nota invalida")

    else:
        sum+=a
        c+=1
av=sum/2

print("media = %.2f"%av)
       