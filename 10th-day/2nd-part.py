board = []
board2 = []
scol = 0
srow = 0
row_counter = 0
from numpy import * 

with open('input.txt', 'r') as file:
    for line in file:
        board_row = []
        board_row2 = []
        for col in line.replace('\n', ''):
            if col == 'S':
                srow = row_counter
                scol = line.index('S')
            board_row.append(col)
            board_row2.append(col)
        board.append(board_row)
        board2.append(board_row2)
        row_counter += 1
        
next_coords = []

# Start
next_coords.append((srow, scol))

found = False
board2[srow][scol] = '0'
board[srow][scol] = '0'
pos = 1
total = 0

d_up = ['|', '7', 'F']
s_up = ['|', 'L', 'J']

s_down = ['|', '7', 'F']
d_down = ['|', 'L', 'J']

d_left = ['-', 'L', 'F'] 
s_left = ['-', '7', 'J']

d_right = ['-', '7', 'J']
s_right = ['-', 'L', 'F']

while not found:
    new_coords = []
    for coords in next_coords:
        # down
        if coords[0] + 1 < len(board) and board[coords[0]+1][coords[1]] != '.':
            if coords[0] == srow and coords[1] == scol and board[coords[0]+1][coords[1]] in d_down:
                board2[coords[0]+1][coords[1]] = str(pos)                
                new_coords.append((coords[0] + 1, coords[1]))
            elif board[coords[0]][coords[1]] in s_down and board[coords[0]+1][coords[1]] in d_down:
                board[coords[0]][coords[1]] = board2[coords[0]][coords[1]]
                board2[coords[0]+1][coords[1]] = str(pos)                
                new_coords.append((coords[0] + 1, coords[1]))
        # up
        if coords[0] - 1 >= 0 and board[coords[0]-1][coords[1]] != '.': 
            if coords[0] == srow and coords[1] == scol and board[coords[0]-1][coords[1]] in d_up:
                board2[coords[0]-1][coords[1]] = str(pos)
                new_coords.append((coords[0] - 1, coords[1]))
            elif board[coords[0]][coords[1]] in s_up and board[coords[0]-1][coords[1]] in d_up:
                board[coords[0]][coords[1]] = board2[coords[0]][coords[1]]
                board2[coords[0]-1][coords[1]] = str(pos)
                new_coords.append((coords[0] - 1, coords[1]))
        # left
        if coords[1]-1 >= 0 and board[coords[0]][coords[1]-1] != '.': 
            if coords[0] == srow and coords[1] == scol and board[coords[0]][coords[1]-1] in d_left:
                board2[coords[0]][coords[1]-1] = str(pos)
                new_coords.append((coords[0], coords[1]-1))
            elif board[coords[0]][coords[1]] in s_left and board[coords[0]][coords[1]-1] in d_left:
                board[coords[0]][coords[1]] = board2[coords[0]][coords[1]]
                board2[coords[0]][coords[1]-1] = str(pos)
                new_coords.append((coords[0], coords[1]-1))
        # right
        if coords[1]+1 < len(board[coords[0]]) and board[coords[0]][coords[1]+1] != '.':
            if coords[0] == srow and coords[1] == scol and board[coords[0]][coords[1]+1] in d_right:
                board2[coords[0]][coords[1]+1] = str(pos)
                new_coords.append((coords[0], coords[1]+1))
            elif board[coords[0]][coords[1]] in s_right and board[coords[0]][coords[1]+1] in d_right:
                board[coords[0]][coords[1]] = board2[coords[0]][coords[1]]
                board2[coords[0]][coords[1]+1] = str(pos)
                new_coords.append((coords[0], coords[1]+1))  
                
    next_coords = new_coords   
    
    if new_coords == []:
        total = pos - 1
        found = True 
        break
    
    pos += 1  
        
for rows in board2:
    for row in rows:
        print(row, '    ', end='')
    print() 
print()   

print(total)