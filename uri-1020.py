x = int(input())

year = int(x/(12*30))
month = int((x-(year*365))/30)
day = int((x-(year*365)-(month*30)))
print(year,"ano(s)")
print(month,"mes(es)")
print(day,"dia(s)")
