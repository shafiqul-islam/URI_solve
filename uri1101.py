
while 1:
    a,b=input().split()
    a,b=int(a),int(b)
    sum=0

    if a>0 and b>0:
        if a>b:
           a,b=b,a
        for i in range(a,b+1):
            sum+=i
            print(str(i) ,end=" ")
        print("Sum=" +str(sum))
    else:
        break