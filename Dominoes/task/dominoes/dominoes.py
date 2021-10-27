import random


class Dominoes(list):
    def __init__(self):
        super().__init__()


class Domino:

    def __init__(self, x=-1, y=0):
        self.x = x
        self.y = y
        self.double = x == y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __int__(self):
        return self.x + self.y

    def __gt__(self, other):
        return int(self) > int(other)


def highest_double(dominoes: list):
    hd = Domino()
    for d in dominoes:
        hd = d if d.double and d > hd else hd
    return hd


def print_dominoes(dominoes: list):
    output = str()
    for d in dominoes:
        output += str(d) + " "
    print(f"[{output}]")


# Initialize Variables and Seed Random
done = False
Stock = list()
Domino_Set = set()
C_Dominoes = list()
P_Dominoes = list()
Snake = list()
Status = str()
random.seed()

# Create a set of all dominoes
for i in range(7):
    for j in range(i, 7):
        Domino_Set.add(Domino(i, j))

# Loop until a Snake is found
while not done:
    # Create a copy of the main set and shuffle it
    Stock = list(Domino_Set)
    random.shuffle(Stock)

    # Pop pieces off the stack and give to the computer and the player
    for i in range(7):
        C_Dominoes.append(Stock.pop())
        P_Dominoes.append(Stock.pop())

    # Get the starting snake piece
    C_Highest = highest_double(C_Dominoes)
    P_Highest = highest_double(P_Dominoes)
    if C_Highest > P_Highest:
        Snake.append(C_Highest)
        C_Dominoes.remove(C_Highest)
        Status = "player"
        done = True
    elif P_Highest > C_Highest:
        Snake.append(P_Highest)
        P_Dominoes.remove(P_Highest)
        Status = "computer"
        done = True

# Print results
print("Stock pieces:", *Stock)
print("Computer pieces:", *C_Dominoes)
print("Player pieces:", *P_Dominoes)
print("Domino snake:", *Snake)
print("Status:", Status)
