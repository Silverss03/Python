def Dosomething(isaid,leave='I must go all out'):#isaid là parameter
												 #leave là 1 default argument, default 
	print(leave,isaid,'!!!')
	#print('You underestimated my power!')
	#print("You're supposed to destroy the Sith not join them")

Dosomething('To make things better') #to make things better là argument
Dosomething('to ensure their future','I must do something')
def positionalkeyword(positionalitem,*,keargs): #dấu * để báo hiệu sau nó là 1 keyword
	print(positionalitem + keargs)
	print(keargs)
positionalkeyword('The mighty',keargs=' Thor')
def iam(what,i,want,to,be):
	print(what)
	print(i)
	print(want)
	print(to)
	print(be)
solution=('Do','what','you','want')
iam(*solution,'to do')	# * dùng để unpacking dưới dạng positional argument, nhưng với dict chỉ unpack đc key
def iam(*args,keargs):	# * lúc này dùng để packing các g.trị vào biến args dưới dạng tuple, sau pack lúc này là các keyword argument
	print(args)
iam('Sure','why','not',keargs="Let's go")
dict={'Name':'Mạnh'}
def iam(Name):
	print(Name)
iam(**dict)	# unpacking dict
def iam(**kwargs): #packing dưới dạng dict
	#global local # nhưng nếu dùng hàm global thì sẽ có thể sử dụng ở bên ngoài hàm
	local2= 'Another thing to print'
	print(kwargs)
	local= 'Random Local stuff' # các biến chỉ được sử dụng trong hàm của nó và được gọi là hàm local
	return local,local2 # 1 cách khác là sử dụng return để ném giá trị của biến ra ngoài 
	print(kwargs) # các câu lệnh sau return sẽ bị bỏ qua
iam(Name='Mạnh')
Hứng= iam()
print(Hứng)
#Lưu ý:không được phép bỏ các positional parameter sau biến packing mà có ** giống như với *
def yieldcreate():
	for i in range(4):
		print('Tôi là số ', i)
		yield i 
for a in yieldcreate():
	print(a)
def lmda():
	return lambda x : x**2
a=lmda()
print(a(2))
mapobj=[1,2,3,4]
print(list(map(lambda x: x **2,mapobj)))
print(tuple(filter(lambda x: x%2 ==0,mapobj)))
from functools import reduce
plus=lambda x,y:x *y
print(reduce(plus,mapobj))