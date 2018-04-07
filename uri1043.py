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

a=list3[0]
b=list3[1]
c=list3[2]
if (a+b)>c:
    x=a+b+c
    print("Perimetro = %.1f"%x)
else:
    x=.5*(list2[0]+list2[1])*list2[2]
    print("Area = %.1f"%x)