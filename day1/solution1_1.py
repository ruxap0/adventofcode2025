
with open('day1/input1.txt', 'r') as file:
    turn = 50
    zeros_counter = 0
    for line in file.readlines():
        direction = line[0]
        nturns = line[1:]
        print(direction, nturns)

        if direction == "L":
            turn -= int(nturns)
            while turn < 0:
                turn = 100 + turn
        else:
            turn += int(nturns)
            while turn > 100:
                turn -= 100
        
        if turn == 0 or turn == 100:
            zeros_counter += 1

    print(zeros_counter)


