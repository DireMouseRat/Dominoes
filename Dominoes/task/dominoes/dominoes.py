import random


def shuffle(dominoes: list):

    return dominoes


# Domino_Set = {(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 3), (3, 4), (3, 5), (3, 6), (4, 4), (4, 5), (4, 6), (5, 5), (5, 6), (6, 6)}
# Set of Tuples
Domino_Set = set()
for i in range(7):
    for j in range(i, 7):
        Domino_Set.add((i, j))
print(len(Domino_Set))
print(Domino_Set)

# List of Shuffled Tuples
Domino_Stack = list(Domino_Set)
print(Domino_Stack)
random.seed()
random.shuffle(Domino_Stack)
print(Domino_Stack)


Stock_Pieces = Domino_Stack[:]
Computer_Pieces = list()
Player_Pieces = list()
for i in range(7):
    Computer_Pieces.append(Stock_Pieces.pop())
    Player_Pieces.append(Stock_Pieces.pop())

print(Stock_Pieces)
print(Computer_Pieces)
print(Player_Pieces)
print(Domino_Stack)
