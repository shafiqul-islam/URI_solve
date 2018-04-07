n=int(input())
if n%2==0:
    for i in range(1,12,2):
        n=n+i
        print(n)
        n=n-i
else:
    print(n)
    for i in range(2,12,2):
        n=n+i
        print(n)
        n=n-i
