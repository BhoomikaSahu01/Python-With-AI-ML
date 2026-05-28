'''# list comprehension
row = []
for i in range(8):
    row.append("WHITE_PAWN")
print(row)


row = ["WHITE_PAWN" for i in range(8)]
print(row)


row = ["WHITE_PAWN" for i in range(8)]
squares = [x ** 2 for x in range(1, 11)]
print(row)
print(squares)

row = ["WHITE_PAWN" for i in range(8)]// 0 to 7 
squares = [x ** 2 for x in range(1, 11)]
twos = [2 ** index for index in range(8)]
print(twos)

squares = [index ** 2 for index in range(1,11)]
odds = [element for element in squares if element % 2 != 0]
print(odds)

# Two dimensional list
board = []
for i in range(8):
    row = ["EMPTY" for i in range(8)]
    board.append(row)
    
#print(board)
for index in board:
    print(index)
print(len(board))

#print(board[0][3]) #row and column 
board[0][0] = "R00K"
board[0][7] = "R00K"
board[7][0] = "R00K"
board[7][7] = "R00K"

board[0][1] = "KNIGHT"
board[0][6] = "KNIGHT"
board[7][1] = "KNIGHT"
board[7][6] = "KNIGHT"

for index in board:
    print(index)
    
    #multi dimensional array
    
temps = [[0.0 for h in range(24) if h == 11]for d in range(31)]
for element in temps:
    print(element)
    
temps = [[0.0 for h in range(24)] for d in range(31)]

temp1 = 19
temp2 = 32
count = 0

for days in temps:
    if count == 0:
        days[11] = temp1
        count = 1
    else:
        days[11] = temp2
        count = 0
        
for element in temps:
    print(element)
    
total = 0.0
for day in temps:
    total += day[11]
average = total/31
print("Average temperature at noon:",average)

highest = -100.0
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
print("the highest temperature was:", highest)

hot_days = 0
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
print(hot_days,"days were hot days in the month.")'''

rooms = [[[False for r in range(20)] for f in range(15)]for t in range(3) ]
print(rooms)
rooms[1][9][13] = True

rooms[1][9][1] = True

vacancy = 0
for room_number in range(20):
    if not rooms[1][9][room_number]:
        vacancy += 1
print("vacancy in 3rd 15th floor of 3rd Building",vacancy)

    


























