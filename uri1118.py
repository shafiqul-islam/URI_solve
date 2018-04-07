while 1:
    y=1
    x=1
    a=float(input())
    if a<0 or a>10:
        print("nota invalida")
        continue
    
    while x==1:
        b=float(input())
        if b<0 or b>10:
            print("nota invalida")
            continue
        x+=2
        c=(a+b)/2
        print("media = %.2f"%c)
        print("novo calculo (1-sim 2-nao)")
    while y==1:
        g=int(input())
        if g<1 or g>2:
            print("novo calculo (1-sim 2-nao)\n")
            continue
        y+=2
    if g==2:
        break