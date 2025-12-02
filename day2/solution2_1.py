with open('day2/input2.txt', 'r') as file:
    first, last, solution = 0, 0, 0
    herewegoagain = True

    lines = file.read().split(',')
    
    for line in lines:
        first, last = line.split('-')

        for i in range(int(first), int(last) + 1):
            i_str = str(i)

            mid = len(i_str) // 2
            i1 = i_str[:mid]
            i2 = i_str[mid:]

            if i1 == i2:
                print("Found one : ", i)
                solution+=i
                



    
    print(solution)


