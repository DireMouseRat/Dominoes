import random

# Domino_Set = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)}

# Create a set of all dominoes
Domino_Set = set()
for i in range(7):
    for j in range(i, 7):
        Domino_Set.add((i, j))

# Create a copy of the main set and shuffle it
Stock_Pieces = list(Domino_Set)
random.seed()
random.shuffle(Stock_Pieces)

# Pop pieces off the stack and give to the computer and the player
Computer_Pieces = list()
Player_Pieces = list()
for i in range(7):
    Computer_Pieces.append(Stock_Pieces.pop())
    Player_Pieces.append(Stock_Pieces.pop())

# Get the starting snake piece


# Print results
print("Stock pieces:", Stock_Pieces)
print("Computer pieces:", Computer_Pieces)
print("Player pieces:", Player_Pieces)

