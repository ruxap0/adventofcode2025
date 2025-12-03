with open("day3/input3.txt", 'r') as f:
    solution = 0

    for line in f:
        line = line.strip()
        l = list(line)

        nb = ['0', '0']

        for i in range(len(l)):
            cur = l[i]
            if int(cur) > int(nb[0]) and i < len(l) -1:
                nb[0] = cur
                nb[1] = '0'
            elif int(cur) > int(nb[1]):
                nb[1] = cur

        print(''.join(nb))
        solution += int(''.join(nb))

print(solution)