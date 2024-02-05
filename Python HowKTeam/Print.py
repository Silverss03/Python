print('Obiwan','Kenobi',sep='-',end='\n')
from time import sleep
print(1,end='',flush=False)
sleep(1)
print(3)
print('Captain \n','Jack',end='+')
sleep(1)
print('Sparrow')
with open('Random 2.txt','w') as a :
	print('Hello there', file=a)


your_name = "Henry"
your_great = "Hello! My name is "

for y in your_great + your_name:
    print(y, end='', flush=True)
    sleep(0.1)
print()
hoa_qua = ['chuoi', 'tao', 'xoai', 'cam', 'le']
for qua in hoa_qua + list(your_name) :
      print(qua,end='',flush=True)
      sleep(0.1)
print()
