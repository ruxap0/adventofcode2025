'''
Pour position i de 0 à 11:
    - Calculer combien de chiffres restent à choisir après : reste = 12 - i
    - Chercher le maximum parmi les chiffres disponibles dans la fenêtre 
      [position_actuelle, n - reste + 1]
    - Prendre ce maximum et avancer la position_actuelle juste après
'''

with open("day3/input3.txt", 'r') as file:
    solution = 0
    for line in file.readlines():
        line = line.strip()
        l = list(line)

        result = []
        pos = 0

        for i in range(12):
            reste = 12 - i
            max_digit = '0'
            max_pos = pos

            for j in range(pos, len(l) - reste + 1):
                if l[j] > max_digit:
                    max_digit = l[j]
                    max_pos = j

            result.append(max_digit)
            pos = max_pos + 1

        print(''.join(result))
        solution += int(''.join(result))
    
    print(solution)