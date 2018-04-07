a,b,c,d=input().split()
a,b,c,d=float(a),float(b),float(c),float(d)
average=(a*2+b*3+c*4+d*1)/(10)
print("Media: %.1f"%average)
if average>=7:
    print("Aluno aprovado.")
elif average>=5:
    print("Aluno em exame.")
    Nota=float(input())
    print("Nota do exame: %.1f"%Nota)
    average2=(average+Nota)/2
    if average2>=5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f"%average2)
else:
    print("Aluno reprovado.")

