a=float(input())
print("NOTAS:")
# n6=a%100
n5=a//100
n6=a-(n5*100)
n5a=int(n5)
print(str(n5a) +" nota(s) de R$ 100.00")

#n4=n6%50
n3=n6//50
n4=n6-(n3*50)
n3a=int(n3)
print(str(n3a) +" nota(s) de R$ 50.00")

#n2=n4%20
n1=n4//20
n2=n4-(n1*20)
n1a=int(n1)
print(str(n1a) +" nota(s) de R$ 20.00")

#n8=n2%10
n7=n2//10
n8=n2-(n7*10)
n7a=int(n7)
print(str(n7a) +" nota(s) de R$ 10.00")

#n10=n8%5
n9=n8//5
n10=n8-(n9*5)
n9a=int(n9)
print(str(n9a) +" nota(s) de R$ 5.00")

#n12=n10%2
n11=n10//2
n12=n10-(n11*2)
n11a=int(n11)
print(str(n11a) +" nota(s) de R$ 2.00")

print("MOEDAS:")
#n24=n12%1
n23=n12//1
n24=n12-(n23*1)
n23a=int(n23)
print(str(n23a) +" moeda(s) de R$ 1.00")

#n22=n24%.50
n21=n24//.50
n22=n24-(n21*.50)
n21a=int(n21)
print(str(n21a) +" moeda(s) de R$ 0.50")

#n20=n22%.25
n19=n22//.25
n20=n22-(n19*.25)
n19a=int(n19)
print(str(n19a) +" moeda(s) de R$ 0.25")

#n18=n22%.10
n17=n20//.10
n18=n20-(n17*.10)
n17a=int(n17)
print(str(n17a) +" moeda(s) de R$ 0.10")

#n16=n18%.05
n15=n18//.05
n16=n18-(n15*.05)
n15a=int(n15)
print(str(n15a) +" moeda(s) de R$ 0.05")

#n14=n16%.01

n13=n16//.01

n13a=int(n13)
print(str(n13a) +" moeda(s) de R$ 0.01")
