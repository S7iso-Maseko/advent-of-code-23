file_path = './input.txt'

hands = []
bids = []

with open(file_path, 'r') as file:
    for line in file: 
        hands.append(line.split())

# Decided to map the cards to letters, that way I can sort them with using a Python sort function
cards1 = ["A", "K", "Q", "T", "J", "9", "8", "7", "6", "5", "4", "3", "2"]
cards2 = ["N", "M", "L", "K", "A", "I", "H", "G", "F", "E", "D", "C", "B"]

wins = []
updated_hands = []

for hand, bid in hands:
    for i in range(len(cards1)):
        hand = hand.replace(str(cards1[i]), cards2[i])
    updated_hands.append((hand, bid))

cards2 = ["N", "M", "L", "K", "I", "H", "G", "F", "E", "D", "C", "B"]

difset = []
for hand, bid in updated_hands:
    sets = []
    for i in cards2:
        if hand.count(str(i)) > 1:
            sets.append(hand.count(str(i)))
            difset.append(i)
    if 'A' in hand:
        sets = []
        if difset != []:
            if len(difset) == 2:
                if difset[0] > difset[1]:
                    sets.append(hand.count(difset[0]) + int(hand.count(str('A')))) 
                    sets.append(hand.count(difset[1]))
                else: 
                    sets.append(hand.count(difset[1]) + int(hand.count(str('A'))))
                    sets.append(hand.count(difset[0])) 
            else: sets.append(hand.count(difset[0]) + int(hand.count(str('A')))) 
        elif int(hand.count(str('A'))) + 1 <= 5:
            sets.append(int(hand.count(str('A'))) + 1)
        else: sets.append(int(hand.count(str('A'))))
    difset = []
        
    if sets == []:
        sets.append(1)
        
    wins.append((sorted(sets, reverse=True), hand, int(bid)))


wins = sorted(wins)
total = 0
       
for i in range(len(wins)):
    total += wins[i][2] * (i+1)

print(total)

