import datetime
x=datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))
print(x.month)

y=datetime.datetime(2001,5,3)  #library
print(y)

print(x.strftime("%B"))
print(x.strftime("%b"))

print(x.strftime("%w")) #weekday
print(x.strftime("%d")) #day
print(x.strftime("%m")) #month
print(x.strftime("%y")) #year
print(x.strftime("%Y")) #year full version
print(x.strftime("%H")) # 24hour
print(x.strftime("%I")) # 12hour
print(x.strftime("%p")) #pm
print(x.strftime("%M")) #minute
print(x.strftime("%S")) #second
print(x.strftime("%f")) #microsecond
# print(x.strftime("%z")) #
#print(x.strftime("%Z"))
print(x.strftime("%j")) # day number pof the year(367)
print(x.strftime("%U")) #week number of the year
print(x.strftime("%W")) #week number
print(x.strftime("%c"))
print(x.strftime("%C")) #century
print(x.strftime("%x"))#local version time
print(x.strftime("%X"))
print(x.strftime("%%"))
print(x.strftime("%G"))
print(x.strftime("%u"))
print(x.strftime("%V"))
