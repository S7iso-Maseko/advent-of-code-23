expenses = {
    "Jan" : 2200,
    "Feb" : 2350,
    "Mar" : 2600,
    "Apr" : 2130,
    "May" : 2190
}


expenses = [2200, 2350, 2600, 2130, 2190]


# 1
print(expenses[1] - expenses[0])

#2
total = 0
for i in range(3):
    total = total + expenses[i]
    
print(total)

# 3
for i in expenses:
    if i == 2000:
        print(True)
        break
    
# 4
expenses.append(1980)
print(expenses)

# 5
