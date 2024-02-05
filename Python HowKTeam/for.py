a= (k for k in range(3))
for m in a:
	print('->',m)
howkteam = {'name': 'Kteam', 'kter': 69}
print(dict(howkteam.items()))
for a,b in howkteam.items():
	if a == 'name' :
		#break
		continue
	else :print(a,'->',b)
a= 'How I met your mother'
for k in a:
	if k == ' ':
		#break
		continue
	else:
		print(k)
else:
	print('Nightmare before Christmas') #break sẽ bỏ qua else
print(list(range(4,1,-1)))
k = range(999999)
lst = list(k)
#print(lst)
#print(k)
#print(9999999999 in k)
#print(9999999999 in lst)
a= ['Akharam',(1,3,5,7,9),'Lost in action']
for k in range(len(a)) :
	print(a[k])
random=[1,2,3]
for value in random:
	value +=1
print(random)
for anothervalue in range(len(random)):
	random[anothervalue] +=1 
print(random) #range dùng để update và xử lí list
print([''.join((a.capitalize(), b.lower(), c.upper())) for a, b, c in [('holy', ' CRAP IS', ' batman')]])
a={key:value for key,value in (('Name','Akharam'),('Age',18),('Status','Alive'))}
print(a)
gen=enumerate(a)
print(list(gen))
