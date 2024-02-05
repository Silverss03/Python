for t in range(int(input())):
    n = int(input())
    print("1 * ", end = "")
    times = 0
    emp_list = []
    while(n % 2 == 0):
        times += 1
        n = (int)(n/2)
    if(times > 0):
        emp_list.append("2^" + str(times))
    for i in range(3,int(n**0.5) + 1,2):
        times = 0
        while(n % i == 0):
            times+=1
            n = (int)(n/i)
        if(times > 0):
            emp_list.append(str(i) +"^" + str(times))
    if(n > 1):
        emp_list.append(str(n) + "^1")
    for i in range(len(emp_list) - 1):
        print(emp_list[i],end = " * ")
    print(emp_list[-1])