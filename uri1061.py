#print("Dia " ,end="")
#start_day=input()
a,start_day=input().split()
start_day=int(start_day)
#print(str(start_day))
Start_hour,colon1,Start_minute,colon2,Start_second=input().split()
Start_hour,Start_minute,Start_second=int(Start_hour),int(Start_minute),int(Start_second)
#import math
#print("Dia " ,end="")
#end_day=input()
b,end_day=input().split()
end_day=int(end_day)
#print(str(start_day))
end_hour,colon3,end_minute,colon4,end_second=input().split()
end_hour,end_minute,end_second=int(end_hour),int(end_minute),int(end_second)

Start_time=start_day*24*60*60+Start_hour*60*60+Start_minute*60+Start_second
end_time=end_day*24*60*60+end_hour*60*60+end_minute*60+end_second

Time_Duration=end_time - Start_time
Second=Time_Duration%60
M_Duration=Time_Duration//60
Minute=M_Duration%60
H_Duration=M_Duration//60
Hour=H_Duration%24
Day=H_Duration//24
print(str(Day) +" dia(s)")
print(str(Hour) +" hora(s)")
print(str(Minute) +" minuto(s)")
print(str(Second) +" segundo(s)")

