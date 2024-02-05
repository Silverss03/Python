def towerofHN(n, source, destination, intermediate):
    if(n == 1):
        print(source + " -> " + destination)
        return
    towerofHN(n - 1, source, intermediate, destination)
    print(source + " -> " + destination)
    towerofHN(n - 1, intermediate, destination, source)
    
towerofHN(int(input()), 'A', 'C', 'B')