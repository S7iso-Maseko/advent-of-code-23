import re
file_path = './input.txt'
import numpy as np

winning = []
myNumbers = []
i = 1
total = 0

with open(file_path, 'r') as file:
    for line in file:
        line = line.replace(str(i) +":", '')
        print(line)
        split_result = line.split('|')
        
        winning = re.findall(r'\d+', split_result[0])
        myNumbers = re.findall(r'\d+', split_result[1])
        
        points = 0
        
        array = np.intersect1d(winning, myNumbers)
        for x in range(len(array)):
            points = 2**(x)
        
        print(len(winning))
        print(winning)
                    
        i += 1
        total += points

print(total)