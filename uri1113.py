while 1:
    x,y=input().split()
    x,y=int(x),int(y)
    if x>y:
        print("Decrescente")
    elif x<y:
        print("Crescente")
    else:
        break