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

    def empty(self):
        return len(self) == 0

    def count_digit(self, digit):
        count = 0
        for d in self:
            count += 1 if d.x is digit else 0
            count += 1 if d.y is digit else 0
        return count


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


class Game:
    def __init__(self):
        random.seed()
        self.Stock = Dominoes()
        self.Computer = Dominoes()
        self.Player = Dominoes()
        self.Snake = Dominoes()
        self.Status = str()
        self.Players_Turn = False
        self.setup_board()
        self.game_loop()
        self.print_results()

    def setup_board(self):
        # Loop until a Snake is found
        ready_to_start = False
        while not ready_to_start:
            # Create the stock of all dominoes
            for i in range(7):
                for j in range(i, 7):
                    self.Stock.append(Domino(i, j))
            random.shuffle(self.Stock)

            # Pop pieces off the stack and give to the computer and the player
            for i in range(7):
                self.Computer.append(self.Stock.pop())
                self.Player.append(self.Stock.pop())

            # Get the starting snake piece
            c_highest = self.Computer.highest_double()
            p_highest = self.Player.highest_double()
            if c_highest > p_highest:
                self.Snake.append(c_highest)
                self.Computer.remove(c_highest)
                self.set_players_turn()
                ready_to_start = True
            elif p_highest > c_highest:
                self.Snake.append(p_highest)
                self.Player.remove(p_highest)
                self.set_computers_turn()
                ready_to_start = True
            else:  # No doubles were found, restart
                self.Stock = Dominoes()
                self.Computer = Dominoes()
                self.Player = Dominoes()

    def game_loop(self):
        while not self.game_over():
            self.print_board()
            if self.Players_Turn:
                self.players_turn()
            else:
                self.computers_turn()

    def print_board(self):
        print('=' * 70)
        print("Stock size:", len(self.Stock))
        print("Computer pieces:", len(self.Computer))
        self.print_snake()
        print("Your pieces:")
        for i in range(len(self.Player)):
            print(str(i + 1) + ':' + str(self.Player[i]))
        print()
        print(self.Status)

    def players_turn(self):
        # Loop for valid input
        # Play piece
        # Set computers turn
        pass

    def computers_turn(self):
        # Loop for valid input
        # Play random piece
        # Set to players turn
        pass

    def game_over(self):
        x = self.Player.empty
        return self.Player.empty() or self.Computer.empty() or self.draw_condition()

    def set_players_turn(self):
        self.Status = "Status: It's your turn to make a move. Enter your command."
        self.Players_Turn = True

    def set_computers_turn(self):
        self.Status = "Status: Computer is about to make a move. Press Enter to continue..."
        self.Players_Turn = False

    def print_results(self):
        pass

    def print_snake(self):
        print()
        print(*self.Snake)
        print()

    def draw_condition(self):
        if self.Snake[0].x == self.Snake[-1].y:
            if self.Snake.count_digit(self.Snake[0].x) == 8:
                return True
        return False


# Start the game
Game()
