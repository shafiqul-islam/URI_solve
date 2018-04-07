
li=[]
c=0
sum=0
for i in range(6):
    li.append(float(input()))
    if li[i]>0:
        c=c+1
        sum=sum+li[i]
print(str(c) +" valores positivos")
average=sum/c
print("%.1f"%average)