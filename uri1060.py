
li=[]
c=0
for i in range(6):
    li.append(float(input()))
    if li[i]>0:
        c=c+1
print(str(c) +" valores positivos")