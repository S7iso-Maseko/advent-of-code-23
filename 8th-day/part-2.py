file_path = './input.txt'
import math
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

endswithA = [key for key in network.keys() if key.endswith('A')]
endswithZ = [key for key in network.keys() if key.endswith('Z')]

destination = []

greater = []
            
while not found:
    for i in instructions:
        total += 1
        destination = []
        for node in endswithA:
            destination.append(network.get(node).get(i))
                    
        endswithA = destination
       
        for x in endswithA:
            if x in endswithZ:
                greater.append(total)
                endswithA.remove(x)
        
        if len(greater) == len(endswithZ):
            found = True  
            break       

distances = sorted(greater, reverse=True)
print(distances)

lcm = math.lcm(distances[0], distances[1], distances[2], distances[3], distances[4], distances[5])    


    
            
print(lcm)
