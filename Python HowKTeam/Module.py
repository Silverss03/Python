import Modulex
Modulex.sth('I')
from Modulex import * # * để import hết
sth('Woops')
del lst[1]
print(lst)
randomnum=3,4,5
import Modulex
print(Modulex.randomnum)
Modulex.randomnum=3,4,5
import Modulex
print(Modulex.randomnum)
from importlib import reload
reload(Modulex)
print(Modulex.randomnum) #Nếu không dùng reload thì chỉ có thể import attribute 1 lần còn nếu from import rồi mới import có thể reset lại giá trị attribute
from Modulex import randomnum as num 
print(num)