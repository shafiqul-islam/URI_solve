while True:
    x=int(input())
    if x==0:
        break
    else:
        for i in range(1,x+1):
            if i==x:
                print(str(i) ,end="")
            else:
                print(str(i) +" " ,end="")
    print()
