with open('day2/input2.txt', 'r') as file:
    first, last, solution = 0, 0, 0
    herewegoagain = True

    lines = file.read().split(',')
    
    for line in lines:
        first, last = line.split('-')

        for i in range(int(first), int(last) + 1):
            i_str = str(i)

            ind = 2
            
            while((len(i_str) // ind) != 0):
                part_len = len(i_str) // ind
                parts = [i_str[j:j + part_len] for j in range(0, len(i_str), part_len)]

                first_part = parts[0]
                all_equal = all(part == first_part for part in parts)

                if all_equal:
                    print("Found one : ", i)
                    solution += i
                    break

                ind += 1



    
    print(solution)


