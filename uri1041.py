x,y=input().split()
x,y=float(x),float(y)
if x==0 and y==0:
    print("Origem")
elif x!=0 and y==0:
    print("Eixo X")
elif x==0 and y!=0:
    print("Eixo Y")
elif x>0:
    if y>0.0:
        print("Q1")
    else:
        print("Q4")
elif y>0.0:
    print("Q2")
else:
    print("Q3")