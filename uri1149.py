def main():
    li=list(map(int,input().split()))
    b=0
    x,n=li[0],li[1]
    if n<1:
        n=int(input())
    else:
        for i in range(1,n+1):
            b=b+x
            x+=1
    print(str(b))

if __name__=="__main__":
      main()

