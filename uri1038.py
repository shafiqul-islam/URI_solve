a,b=input().split()
a,b=int(a),int(b)
r1=b*4.00
r2=b*4.50
r3=b*5.00
r4=b*2.00
r5=b*1.50
if a==1:
	print("Total: R$ %.2f"%r1)
elif a==2:
	print("Total: R$ %.2f"%r2)
elif a==3:
	print("Total: R$ %.2f"%r3)
elif a==4:
	print("Total: R$ %.2f"%r4)
else:
	print("Total: R$ %.2f"%r5)