x = int(input())
hour = int(x /3600)
minit = int(x/60-(hour*60))
sec = int(x %60)
print("{0}:{1}:{2}".format(hour,minit,sec))
