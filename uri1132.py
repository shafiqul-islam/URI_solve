def main():
    x=int(input())
    y=int(input())
    sum=0
    if x>y:
        x,y=y,x
	
    for i in range(x,y+1,1):
        if i%13!=0:
            sum=sum+i
    print(str(sum))
	
	
if __name__=="__main__":
	main()

	
