
li=[]
c=0
o=0
p=0
n=0
for i in range(5):
    li.append(int(input()))
    if li[i]%2==0:
        c=c+1
    if li[i]%2!=0:
        o=o+1
    if li[i]>0:
        p=p+1
    if li[i]<0:
        n=n+1

print(str(c) +" valor(es) par(es)")
print(str(o) +" valor(es) impar(es)")
print(str(p) +" valor(es) positivo(s)")
print(str(n) +" valor(es) negativo(s)")
