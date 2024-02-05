a= open('Random.txt', mode= 'r+') #mode a+ con trỏ ở cuối file
a1= a.read() #readline:đọc theo hàng ngang
a.seek(0)
print(a1)
a2=a.read()
print(a2)
a.close()
a= open('Random.txt', mode= 'r+')
a1= a.readlines()
print(a1)
a2 =tuple(a1)
print(a2)
a.close()
a= open('Random.txt', mode= 'a+')
a1=a.write('  \nMe and the bois')
print(a1)
with open ('Random.txt') as a:
	a1=a.read()
print(a1)
