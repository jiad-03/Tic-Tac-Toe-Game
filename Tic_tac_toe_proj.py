p1 = input("Enter Name of Player 1: ")
p2 = input("Enter Name of Player 2: ")

matrix = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def winner_check(matrix):
    for row in matrix:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col] and matrix[0][col] != ' ':
            return matrix[0][col]
 
    if matrix[0][0] == matrix[1][1] == matrix[2][2] and matrix[0][0] != ' ':
        return matrix[0][0]
    
    if matrix[0][2] == matrix[1][1] == matrix[2][0] and matrix[0][2] != ' ':
        return matrix[0][2]

    return None  

turn = 0  
while turn < 9: 
    player = p1 if turn % 2 == 0 else p2  
    symbol = "o" if turn % 2 == 0 else "x"  
    print(f"\n{player}'s turn ({symbol}).")

    while True:
        print("Where to put this?\n 1. Top row\n 2. Middle row\n 3. Lower row")
        place = input("Enter here: ").lower()

        if place in ["top row", "top"]:
            row_index = 0
        elif place in ["middle row", "middle"]:
            row_index = 1
        elif place in ["lower row", "lower"]:
            row_index = 2
        else:
            print("Invalid row! Try again.")
            continue

        print("Where to place", symbol, "in the row?\n a. Left\n b. Middle\n c. Right")
        pr = input("Enter here: ").lower()

        if pr == "left":
            col_index = 0
        elif pr in ["mid", "middle"]:
            col_index = 1
        elif pr == "right":
            col_index = 2
        else:
            print("Invalid column! Try again.")
            continue

        if matrix[row_index][col_index] == ' ':
            matrix[row_index][col_index] = symbol
            break  
        else:
            print("That spot is already taken! Try again.")

    print("\nCurrent Board:")
    for row in matrix:
        print(row)

    
    winner = winner_check(matrix)
    if winner:
        if winner == "o":
            print(f"\n🎉 {p1} wins! 🎉")
        else:
            print(f"\n🎉 {p2} wins! 🎉")
        break  

    turn += 1  


if turn == 9 and not winner:
    print("\n🤝 It's a Draw! 🤝")
