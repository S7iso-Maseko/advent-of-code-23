import re
file_path = './input.txt'
import numpy as np

winning = []
myNumbers = []
totalWins = []
total = 0
i = 1

with open(file_path, 'r') as file:
    for line in file:
        line = line.replace(str(i) +":", '')
        split_result = line.split('|')
        
        winning = re.findall(r'\d+', split_result[0])
        myNumbers = re.findall(r'\d+', split_result[1])
        
        points = 0
        
        array = np.intersect1d(winning, myNumbers)
        for x in range(len(array)):
            points += 1
        
        totalWins.append(points)
                    
        i += 1

instances = [1]*len(totalWins)
counter = 1
count = 0
for x in totalWins:
    count += 1
    for v in range(x):
        instances[count+v] = instances[count-1] + instances[count+v]
        
for v in instances:
    total += v       
print(instances)
print(total)

