while True:
	try:
		sinput = input().strip()
		inlist = list(map(int,sinput.split()))
		x = inlist[0]
		n = inlist[1]
		b = 0
		k = 2
		while n<=0:
			n = inlist[k]
			k = k+1
		mrange = n + x -1;
		x = x - 1
		result = mrange*(mrange + 1)/2 - x*(x+1)/2
		print(int(result))
	except EOFError:
		break	
