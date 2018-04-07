a,b,c,d=input().split()
a,b,c,d=int(a),int(b),int(c),int(d)
start_time=a*60+b
end_time=c*60+d

if start_time!=end_time:
    if start_time<end_time:
        x=end_time-start_time
        minute=x%60
        hour=x//60
        print("O JOGO DUROU " +str(hour) +" HORA(S) E " +str(minute) +" MINUTO(S)")
    else:
        x=(end_time+24*60)-start_time
        minute=x%60
        hour=x//60
        print("O JOGO DUROU " +str(hour) +" HORA(S) E " +str(minute) +" MINUTO(S)")
        
else:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")