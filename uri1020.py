a=int(input())
year=a//365
day1=a%365
month=day1//30
day=day1%30
print(str(year) +" ano(s)")
print(str(month) +" mes(es)")
print(str(day) +" dia(s)")