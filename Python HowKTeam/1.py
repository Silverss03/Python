def gen():
	for i in range(4):
		x = yield i
		print('value sent from you', x)
print(list(gen()))