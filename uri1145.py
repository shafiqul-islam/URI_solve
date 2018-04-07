x,y=input().split()
x,y=int(x),int(y)
b=0
for i in range(1,y+1):
    b+=1
    if b==x:
        print(str(i) +" ",end="")
    else:
        print(str(i) +" " ,end="")
    if b==x:
        b=0
        print()

