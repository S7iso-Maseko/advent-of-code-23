import re
file_path = './input.txt'
pp = {}
i = 0
counter = 0



with open(file_path, 'r') as file:
    for line in file:
        i += 1 
        
        line = line.replace('Game ' + str(i), '')
        substring = re.search(r':\s*(.*?);', line)
                
        matches = re.findall(r'(\b\d+\b)\s*([a-zA-Z]+)', substring[1])
        numbers = [int(match[0]) for match in matches]
        colors = [match[1] for match in matches]
        
        pp.update({i:{counter:{}}})
        for num in range(len(numbers)):
            pp.get(i).get(counter).update({colors[num]: numbers[num]})
        counter += 1
        pp.get(i).update({counter:{}})
                    
        line = line.replace(substring.group(0), '')
        while re.search(r'(\s*(.*?);)', line):
            substring = re.search(r'(\s*(.*?);)', line)
            
            matches = re.findall(r'(\b\d+\b)\s*([a-zA-Z]+)', substring[1])
            numbers = [int(match[0]) for match in matches]
            colors = [match[1] for match in matches]
            
            for num in range(len(numbers)):
                pp.get(i).get(counter).update({colors[num]: numbers[num]})
            counter += 1
            pp.get(i).update({counter:{}})
            
            line = line.replace(substring.group(0), '')
        
            
        matches = re.findall(r'(\b\d+\b)\s*([a-zA-Z]+)', line)
        numbers = [int(match[0]) for match in matches]
        colors = [match[1] for match in matches]
        
        for num in range(len(numbers)):
            pp.get(i).get(counter).update({colors[num]: numbers[num]})
        
        counter = 0
    
        
print(pp.get(1), "\n")
print(pp.get(1).get(0), "\n")

imposible = 0
total = 0

for u in range(i):
    total += u +1
    
print(total)



for v in range(i):
    for x in pp.get(v+1):
        if pp.get(v+1).get(x).get("blue"):
            blue = pp.get(v+1).get(x).get("blue")
            if blue > 14:
                imposible += v+1
                break
       
        if pp.get(v+1).get(x).get("red"):
            red = pp.get(v+1).get(x).get("red")
            if red > 12:
                imposible += v+1
                break
            
        if pp.get(v+1).get(x).get("green"):
            green = pp.get(v+1).get(x).get("green")
            if green > 13:
                imposible += v+1
                break
            
max_blue = 0
max_red = 0
max_green = 0

result = 0
            
for v in range(i):
    for x in pp.get(v+1):
        if pp.get(v+1).get(x).get("blue"):
            if pp.get(v+1).get(x).get("blue") > max_blue:
                max_blue = pp.get(v+1).get(x).get("blue")
       
        if pp.get(v+1).get(x).get("red"):
            if pp.get(v+1).get(x).get("red") > max_red:
                max_red = pp.get(v+1).get(x).get("red")
            
        if pp.get(v+1).get(x).get("green"):
            if pp.get(v+1).get(x).get("green") > max_green:
                max_green = pp.get(v+1).get(x).get("green")
            
    result += max_blue * max_green * max_red
    max_blue = 0
    max_red = 0
    max_green = 0
    
print(result)


        
#     for d in range(len(x)):
#         print
         
        # print(updated_string)
        



# import re

# def extract_and_remove_substring(input_string):
#     # Use a regular expression to find the substring between a colon and a semicolon
#     match = re.search(r':\s*(.*?);', input_string)

#     if match:
#         substring_between_colon_and_semicolon = match.group(1).strip()
#         print(f"Extracted Substring: '{substring_between_colon_and_semicolon}'")

#         # Remove the extracted substring from the input string
#         updated_string = input_string.replace(match.group(0), '')

#         return updated_string.strip()

#     return input_string.strip()

# # Example usage
# input_string = "1: 1 yellow, 14 black, 23 orange; 12 yellow, 1 black, 3 orange"
# updated_string = extract_and_remove_substring(input_string)

# if updated_string:
#     print(f"Updated String: '{updated_string}'")
# else:
#     print("String is empty after extraction.")
