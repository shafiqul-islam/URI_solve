n=int(input())
c=0
s=0
while n>0:
    x=int(input())
    if x>=10 and x<=20:
        c+=1
    else:
        s+=1
    n=n-1
print(str(c) +" in")
print(str(s) +" out")