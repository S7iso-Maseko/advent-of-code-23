import re
file_path = './input.txt'

def sequence(mylist, lv):
    newlist = []
    total = 0
    
    lv.append(mylist[len(mylist)-1])
    for i in range(len(mylist)):
        if i + 1 < len(mylist):
            newlist.append(mylist[i+1] - mylist[i])
            total += mylist[i+1] - mylist[i]  
    
    if len(newlist) >= 1 and total != 0:
        sequence(newlist, lv)  

    return sum(lv)
 
total = 0

with open(file_path, 'r') as file:
    for line in file:  
        mylist = re.findall(r'-?\d+', line)
        newlist = [int(char) for char in mylist]    
        # Just reversed the list
        total += sequence(newlist[::-1], [])
        
print(total)
