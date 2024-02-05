#Chỉ có hai giá trị:True và False
print(3>1)
print((5 *0)!= 0)
print('Kteam' == "Kteam")
print('Free' == 'Education')
print(ord('a')) #python ss bằng cách đưa kí tự về dưới dạng số
#Khi so sánh bằng ==, >=, <= thì Python sẽ so sánh hết các phần tử.
#Còn >, <, != thì nhiều lúc Python sẽ không cần đi hết các giá trị. Nếu như ở vị trí nào mà đã hai giá trị không bằng nhau thì nó dừng lại.
lst = [1, 2, 3]
lst_ = [1, 2, 3]
print(lst ==lst_)
print(lst is lst_)
_lst = lst
print(lst is _lst)
#Các số từ -5 đến 256 hoặc là một số chuỗi có số kí tự dưới 20 thì các biến có cùng một giá trị sẽ có cùng một giá trị trả về từ hàm id.
#VD
a = -5
b = -5
a = 'abc'
b = 'abc'
print(a is b) 
print(bool (0)) #None và rỗng cx tương tự
