import sys

input_data = sys.stdin.read().split()

if input_data:
    n = int(input_data[0])
    moves = [int(x) for x in input_data[1:n+1]]
    
    white_keys = {
        0: 'C', 2: 'D', 4: 'E', 5: 'F', 
        7: 'G', 9: 'A', 11: 'B'
    }

    start_notes = [9, 11, 0, 2, 4, 5, 7]

    for start in start_notes:
        current = start
        is_valid = True
        
        for move in moves:
            current = (current + move) % 12

            if current not in white_keys:
                is_valid = False
                break

        if is_valid:
            print(f"{white_keys[start]} {white_keys[current]}")