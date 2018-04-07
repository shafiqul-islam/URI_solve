a=int(input())
print(str(a))
n6=a%100
n5=a//100
print(str(n5) +" nota(s) de R$ 100,00")

n4=n6%50
n3=n6//50
print(str(n3) +" nota(s) de R$ 50,00")

n2=n4%20
n1=n4//20
print(str(n1) +" nota(s) de R$ 20,00")

n8=n2%10
n7=n2//10
print(str(n7) +" nota(s) de R$ 10,00")

n10=n8%5
n9=n8//5
print(str(n9) +" nota(s) de R$ 5,00")

n12=n10%2
n11=n10//2
print(str(n11) +" nota(s) de R$ 2,00")
n14=n12%1
n13=n12//1
print(str(n13) +" nota(s) de R$ 1,00")