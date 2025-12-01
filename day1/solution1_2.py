
with open('day1/input1.txt', 'r') as file:
    turn = 50
    prev_turn = 50
    zeros_counter = 0
    for line in file.readlines():
        direction = line[0]
        nturns = line[1:]
        print(direction, nturns)

        if direction == "L":
            turn = prev_turn - int(nturns)
        else:
            turn = prev_turn + int(nturns)
            
        if turn < 0:
            if prev_turn == 0:
                zeros_counter += 0 + 1*(turn //-100)
            else:
                zeros_counter += 1 + 1*(turn //-100)
            turn = turn % 100
        elif turn > 99:
            zeros_counter += 1*(turn//100)
            turn = turn % 100
        elif turn == 0:
            zeros_counter += 1
        
        prev_turn = turn
        
    print(zeros_counter)


