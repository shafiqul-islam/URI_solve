a,b=input().split()
a,b=int(a),int(b)
if a!=b:
    if a<b:
        x=b-a
        print("O JOGO DUROU " +str(x) +" HORA(S)")
    else:
        x=(b+24)-a
        print("O JOGO DUROU " +str(x) +" HORA(S)")
else:
    print("O JOGO DUROU 24 HORA(S)")