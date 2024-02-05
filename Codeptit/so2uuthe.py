for t in range(int(input())):
	n = int(input())
	queue = []
	queue.append('1')
	queue.append('2')
	while(True):
		if(n == 0):
			break
		s = queue.pop(0)
		if(s.count('2') > len(s)/2):
			print(s, end = " ")
			n -= 1
		queue.append(s + '0')
		queue.append(s + '1')
		queue.append(s + '2')
	print()
		