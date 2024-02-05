a=0
if a - 1 < 0:
     print('a nhỏ hơn 1')
a=10
if a - 1 < 0: # False, tiếp tục
     print('a nhỏ hơn 1')
elif a - 2 < 0: # False, tiếp tục
     print('a nhỏ hơn 2')
elif a - 3 < 0: # False, tiếp tục
     print('a nhỏ hơn 3')
elif a - 4 < 0: # True, kết thúc
     print('a nhỏ hơn 4')
elif a - 5 < 0:
     print('a nhỏ hơn 5')
else :
	print('nhập số khác')