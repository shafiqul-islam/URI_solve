n=int(input())
sum=0
c=0
r=0
s=0
while n>0:
    a,b=input().split()

    a=int(a)
    sum+=a

    if b=='C':
        c=c+a
    elif b=='R':
        r=r+a
    else:
        s=s+a

    n-=1
print("Total: " +str(sum) +" cobaias")
print("Total de coelhos: " +str(c))
print("Total de ratos: " +str(r))
print("Total de sapos: " +str(s))

c_per=(c/(c+r+s))*100
r_per=(r/(c+r+s))*100
s_per=(s/(c+r+s))*100
print("Percentual de coelhos: %.2f"%c_per +" %")
print("Percentual de ratos: %.2f"%r_per +" %")
print("Percentual de sapos: %.2f"%s_per +" %")
