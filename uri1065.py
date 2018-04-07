
li=[]
c=0
for i in range(5):
    li.append(int(input()))
    if li[i]%2==0:
        c=c+1
print(str(c) +" valores pares")