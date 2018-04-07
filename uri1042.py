
a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
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
print(str(list3[0]))
print(str(list3[1]))
print(str(list3[2]))

print("")
print(str(list2[0]))
print(str(list2[1]))
print(str(list2[2]))