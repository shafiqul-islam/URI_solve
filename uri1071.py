a=int(input())
b=int(input())
sum=0

if a>b:
    x,y=b,a
    for i in range(x+1,y):
        if i%2!=0:
            sum=sum+i
else:
    for i in range(a+1,b):
        if i%2!=0:
            sum=sum+i
print(sum)
