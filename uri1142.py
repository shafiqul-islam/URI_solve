a=int(input())
c=1
d=4
for i in range(1,a+1,1):
    for j in range(c,d+1,1):
        if j%4==0:
            print("PUM")
        else :
            print(str(j), end=" ")
    c=c+4
    d=d+4
