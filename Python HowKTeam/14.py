Tên1,Cao1=input().split()
Tên2,Cao2=input().split()
Cao1=int(Cao1)
Cao2=int(Cao2)

if Cao1==Cao2 :
    print('2 ông cao như nhau')
elif Cao1>Cao2:
    print(Tên1+' cao hơn '+Tên2)
elif Cao2 or Cao1<=0:
    print('Chiều cao phải lớn hơn 0!')
else :
    print(Tên2 +' cao hơn '+ Tên1)