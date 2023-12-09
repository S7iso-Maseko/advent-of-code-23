file_path = './input.txt'
import re

instructions = ""
network = {}
newline = False

with open(file_path, 'r') as file:
    for line in file: 
        if not newline:
            instructions = line.replace('\n', '')
            newline = True
        elif line != "\n":
            key = re.match(r'([^\s]+)', line)
            left = re.search(r'\(([^,]+),', line)
            right = re.search(r',\s([^)]+)', line)
            network.update({key.group(0):{'L': left.group(1), 'R': right.group(1)}})
            
found = False
total = 0
newkey = 'AAA'

while not found:
    for i in instructions:
        total += 1
        newkey = network.get(newkey).get(i)               
        if newkey == 'ZZZ':
            found = True  
            break        
             
print(total)
