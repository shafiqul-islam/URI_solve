n=int(input())
while n>0:
    x,y=input().split()
    x,y=int(x),int(y)
    if y==0:
        print("divisao impossivel")
    else:
        r=x/y
        print("%.1f"%r)
    n-=1