def findBall(grid):
    if not grid:
        return []

    ball_possiblity = []

    def run_game(start_index):
        curr_row_index = 0
        while curr_row_index < len(grid):
            curr_row = grid[curr_row_index]
            curr_val = curr_row[start_index]

            # print(start_index, curr_val, curr_row[start_index + curr_val])

            if not (0 <= start_index + curr_val < len(curr_row)):
                return -1

            if curr_row[start_index + curr_val] == curr_val:
                start_index += curr_val
                curr_row_index += 1
                continue
            else:
                return -1
        return start_index

    # For Each Row run the game
    for i in range(len(grid[0])):
        ball_possiblity.append(run_game(i))

    return ball_possiblity

# Test Case
test_cases = [dict(input=dict(grid=[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]), output=[1,-1,-1,-1,-1]),
              dict(input=dict(grid=[[-1]]), output=[-1]),
              dict(input=dict(grid=[[-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1]]), output=[-1,-1,-1,2,3,4,5,6,-1,-1,9,10,11,14,-1,-1,15,16,19,20,-1,-1,21,24,-1,-1,25,-1,-1,28,29,30,31,32,33,34,35,-1,-1,-1,-1,40,41,42,43,44,45,-1,-1,48,-1,-1,-1,-1,53,56,-1,-1,-1,-1,59,60,61,64,65,66,67,68,-1,-1,71,72,-1,-1,75,76,-1,-1,77,78,-1,-1,-1,-1,83,86,-1,-1,87,-1,-1,-1,-1,94,95,-1,-1,96,97,98])]

for index, data in enumerate(test_cases, 1):
    act_output = findBall(**data['input'])
    print("Test Case:{} Validity:{}".format(index, act_output == data['output']))
    print("Input:{} Expected:{} Act:{}".format(data['input'], data['output'], act_output))