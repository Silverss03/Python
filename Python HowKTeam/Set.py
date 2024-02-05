# Giới hạn bởi {}
#Ngăn cách bởi ,
#Không chứa các giá trị trùng lặp
#Chứa kiểu hash(Tuple,chuỗi),không chứa unhash(list,set)
a= {'captain',1082003,'Price'}
#Không thể tạo set rỗng bằng dấu ngoặc() nhưng có thể dùng constructor 1=set()
a={a for a in range(2)}
a=set('John MacTavish')
a={2,3} - {2}
a={2,3} & {3} # và
a={1,2,3} | {4,5} # hoặc
a={1,2,3} ^ {3,4,5} # bằng phép | trừ &
a.pop() #Lấy giá trị đầu tiên
b= set()
#b.pop() (Lỗi)
a.remove(2)
a.discard(1) # Giống remove nhưng không báo lỗi
a=b.copy()
a.add(1)
print(a)
print(id(a))
a.add(5)
print(id(a))
#-->set là hash
#set không hỗ trợ index
