import random


class Dominoes(list):
    def __init__(self):
        super().__init__()

    def __str__(self):
        domino_string = str()
        for d in self:
            domino_string += str(d) + ', '
        return '[' + domino_string[:-2] + ']'

    def highest_double(self):
        hd = Domino()
        for d in self:
            hd = d if d.double and d > hd else hd
        return hd


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


# Initialize Variables and Seed Random
Ready_To_Start = False
Stock = Dominoes()
Computer = Dominoes()
Player = Dominoes()
Snake = Dominoes()
Status = str()
random.seed()

# Loop until a Snake is found
while not Ready_To_Start:
    # Create the stock of all dominoes
    for i in range(7):
        for j in range(i, 7):
            Stock.append(Domino(i, j))
    random.shuffle(Stock)

    # Pop pieces off the stack and give to the computer and the player
    for i in range(7):
        Computer.append(Stock.pop())
        Player.append(Stock.pop())

    # Get the starting snake piece
    C_Highest = Computer.highest_double()
    P_Highest = Player.highest_double()
    if C_Highest > P_Highest:
        Snake.append(C_Highest)
        Computer.remove(C_Highest)
        Status = "Status: It's your turn to make a move. Enter your command."
        Ready_To_Start = True
    elif P_Highest > C_Highest:
        Snake.append(P_Highest)
        Player.remove(P_Highest)
        Status = "Status: Computer is about to make a move. Press Enter to continue..."
        Ready_To_Start = True
    else:
        Stock = Dominoes()
        Computer = Dominoes()
        Player = Dominoes()

# Print menu
print('=' * 70)
print("Stock size:", len(Stock))
print("Computer pieces:", len(Computer))
print()
print(*Snake)
print()
print("Your pieces:")
for i in range(len(Player)):
    print(str(i + 1) + ':' + str(Player[i]))
print()
print(Status)
