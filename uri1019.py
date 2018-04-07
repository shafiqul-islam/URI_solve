a=int(input())

second=a%60
minit=a//60
mint=minit%60
hour=minit//60
print(str(hour) +":" + str(mint) +":" +str(second))