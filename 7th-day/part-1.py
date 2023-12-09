file_path = './input.txt'

hands = []
bids = []

with open(file_path, 'r') as file:
    for line in file: 
        hands.append(line.split())

cards = ["E", "D", "C", "B", "A", 9, 8, 7, 6, 5, 4, 3, 2]

wins = []

counter = 0
for hand, bid in hands:
    hand = hand.replace('A', 'E')
    hand = hand.replace('T', 'A')
    hand = hand.replace('J', 'B')
    hand = hand.replace('Q', 'C')
    hand = hand.replace('K', 'D')
    
    sets = []
    for i in cards:
        if hand.count(str(i)) > 1:
            sets.append(hand.count(str(i)))
    if sets == []:
        sets.append(1)
    wins.append((sorted(sets, reverse=True), hand, int(bid)))


wins = sorted(wins)
print(wins)

total = 0
       
for i in range(len(wins)):
    total += wins[i][2] * (i+1)

print(total)