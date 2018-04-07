n=int(input())
while n>0:
    x=int(input())
    if x==0:
        print("NULL")
    elif x>0 and x%2==0:
        print("EVEN POSITIVE")
    elif x>0 and x%2!=0:
        print("ODD POSITIVE")
    elif x<0 and x%2==0:
        print("EVEN NEGATIVE")
    else:
        print("ODD NEGATIVE")
    n-=1