t=int(input())

while t>0:
    x,y=input().split()
    x,y=int(x),int(y)
    if x>y:
        x,y=y,x
    sum=0

    for i in range(x+1,y):
        if i%2!=0:
            sum=sum+i
    print(str(sum))
    t-=1


