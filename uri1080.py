li=[]
for i in range(100):
    li.append(int(input()))

#print(li)

x=max(li)
print(str(x))
for i in range(100):
    if x==li[i]:
        print(str(i+1))