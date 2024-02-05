import sys
while True :
	n = int(input())
	if(n == 0):
		break
	else:
		min = sys.maxsize
		max = -sys.maxsize 
		while(n > 0):
			tmp = int(input())
			n -= 1
			if(min > tmp):
				min = tmp 
			if(max < tmp):
				max = tmp 
		if(min == max):
			print("BANG NHAU")
		else:
			print("{} {}".format(min, max))
