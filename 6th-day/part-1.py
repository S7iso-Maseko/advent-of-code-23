import re
file_path = './input.txt'

times = []
distance = []
instances = []
count = 0
total = 1

t = ""
d = ""

with open(file_path, 'r') as file:
    for line in file:
        if "Time:" in line:
            times = re.findall(r'\d+', line)
        else: distance = re.findall(r'\d+', line)

for i in times:
    t += i
    
for i in distance:
    d += i

print(t)
print(d)
   
for x in range(int(t)):
    if ((int(t) - x) * x) > int(d):
        count += 1
        
print(count)

# counter = 0
# for x in times: 
#     count = 0
#     for i in range(int(x)):
#         if (int(x) - int(i)) * int(i) > int(distance[counter]):
#             count += 1
#     total *= count
#     counter += 1
    
# print(total)