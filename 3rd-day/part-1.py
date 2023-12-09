import re
file_path = './input.txt'
board = []

with open(file_path, 'r') as file:
    for line in file:
        board_row = []
        for col in range(len(line)):
            if line[col] != '\n':
                board_row.append(line[col])
        board.append(board_row)

change = False
total = 0
n = ""
values = []

number = []
new_total = 0
stars = {}

for row in range(len(board)):
    for col in range(len(board[row])):
        if str(board[row][col]).isdigit():
            n += str(board[row][col])
            values.append((row, col))
        elif n != "":
            change = True
            for i in values:
                man = []
                if i[1] -1 >= 0 and str(board[i[0]][i[1]-1]) == "*":
                    print(n)
                    if stars.get((i[0], i[1]-1)):
                        print(stars[(i[0], i[1]-1)])
                        new_total += int(stars.get((i[0], i[1]-1))) * int(n)
                        del stars[(i[0], i[1]-1)]
                    else:
                        stars.update({(i[0], i[1]-1):n})
                    break
                if i[1] +1 < len(board[row]) and str(board[i[0]][i[1]+1]) == "*":
                    print(n)
                    if stars.get((i[0], i[1]+1)):
                        print
                        new_total += int(stars.get((i[0], i[1]+1))) * int(n)
                        del stars[(i[0], i[1]+1)]
                    else:
                        stars.update({(i[0], i[1]+1):n})
                    break
                if i[0] +1 < len(board) and str(board[i[0]+1][i[1]]) == "*":
                    print(n)
                    if stars.get((i[0]+1, i[1])):
                        new_total += int(stars.get((i[0]+1, i[1]))) * int(n)
                        del stars[(i[0]+1, i[1])]
                    else:
                        stars.update({(i[0]+1, i[1]):n})
                    break
                if i[0] -1 >= 0 and str(board[i[0]-1][i[1]]) == "*":
                    print(n)
                    if stars.get((i[0]-1, i[1])):
                        new_total += int(stars.get((i[0]-1, i[1]))) * int(n)
                        del stars[(i[0]-1, i[1])]
                    else:
                        stars.update({(i[0]-1, i[1]):n})
                    break
                
                if i[0] +1 < len(board) and i[1] +1 < len(board[row]) and str(board[i[0]+1][i[1]+1]) == "*":
                    print(n)
                    if stars.get((i[0]+1, i[1]+1)):
                        new_total += int(stars.get((i[0]+1, i[1]+1))) * int(n)
                        del stars[(i[0]+1, i[1]+1)]
                    else:
                        stars.update({(i[0]+1, i[1]+1):n})
                    break
                if i[0] +1 < len(board) and i[1] -1 >= 0 and str(board[i[0]+1][i[1]-1]) == "*":
                    print(n)
                    if stars.get((i[0]+1, i[1]-1)):
                        new_total += int(stars.get((i[0]+1, i[1]-1))) * int(n)
                        del stars[(i[0]+1, i[1]-1)]
                    else:
                        stars.update({(i[0]+1, i[1]-1):n})
                    break
                
                if i[0] -1 >= 0 and i[1] +1 < len(board[row]) and str(board[i[0]-1][i[1]+1]) == "*":
                    print(n)
                    if stars.get((i[0]-1, i[1]+1)):
                        new_total += int(stars.get((i[0]-1, i[1]+1))) * int(n)
                        del stars[(i[0]-1, i[1]+1)]
                    else:
                        stars.update({(i[0]-1, i[1]+1):n})
                    break
                if i[0] -1 >= 0 and i[1] -1 >= 0 and str(board[i[0]-1][i[1]-1]) == "*":
                    print(n)
                    if stars.get((i[0]-1, i[1]-1)):
                        new_total += int(stars.get((i[0]-1, i[1]-1))) * int(n)
                        del stars[(i[0]-1, i[1]-1)]
                    else:
                        stars.update({(i[0]-1, i[1]-1):n})
                    break
            n = ""
        if change:
            values= []
            change = False  

# new_total = 0

print(stars)


# for i in number:
#     for v in number:
#         if i[1] == v[1] and v[0] != i[0]:
#             new_total += int(v[0]) * int(i[0])
#             number.remove((i[0], i[1]))
#             break

print(new_total)          
