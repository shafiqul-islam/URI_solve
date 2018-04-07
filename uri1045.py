a,b,c=input().split()
a,b,c=float(a),float(b),float(c)
list1=[a,b,c]
list2=list1[0:]
#list1.sort()
#print(list1)
#print(list2)
def bubblesort(list1):
    for i in range(0,len(list1)-1):
        for j in range(0,len(list1)-1-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1
list3=bubblesort(list1)
list3.reverse()
# print(list3)
a=list3[0]
b=list3[1]
c=list3[2]

    
if a>=(b+c):
    print("NAO FORMA TRIANGULO")

elif (a*a)==((b*b)+(c*c)):
    print("TRIANGULO RETANGULO")
elif (a*a)>((b*b)+(c*c)):
    print("TRIANGULO OBTUSANGULO")
elif (a*a)<((b*b)+(c*c)):
    print("TRIANGULO ACUTANGULO")

if a==b and a==c:
    print("TRIANGULO EQUILATERO")

elif a==b or b==c:
    print("TRIANGULO ISOSCELES")
