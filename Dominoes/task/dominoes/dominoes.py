import random


class Dominoes(list):
    def __init__(self):
        super().__init__()

    def __str__(self):
        string = str()
        for d in self:
            string += str(d)
        return string

    def greatest_double(self):
        hd = Domino()
        for d in self:
            hd = d if d.double and d > hd else hd
        return hd

    def empty(self):
        return len(self) == 0

    def count_digit(self, digit):
        count = 0
        for d in self:
            count += 1 if d.left is digit else 0
            count += 1 if d.right is digit else 0
        return count

    def pop_random(self):
        return self.pop(random.randrange(0, len(self)))


class Domino:
    def __init__(self, left=-1, right=0):
        self.left = left
        self.right = right
        self.double = left == right

    def __str__(self):
        return f"[{self.left}, {self.right}]"

    def __int__(self):
        return self.left + self.right

    def __gt__(self, other):
        return int(self) > int(other)

    def __lt__(self, other):
        return int(self) < int(other)

    def rotate(self):
        self.left, self.right = self.right, self.left


class Game:
    def __init__(self):
        random.seed()
        self.Stock = Dominoes()
        self.Computer = Dominoes()
        self.Player = Dominoes()
        self.Snake = Dominoes()
        self.Status = str()
        self.Players_Turn = False
        self.setup_game()
        self.game_loop()

    def setup_game(self):
        ready_to_start = False
        while not ready_to_start:
            # Create the starting stock of all dominoes
            for i in range(7):
                for j in range(i, 7):
                    self.Stock.append(Domino(i, j))
            random.shuffle(self.Stock)

            # Distribute dominoes to the computer and the player
            for i in range(7):
                self.Computer.append(self.Stock.pop_random())
                self.Player.append(self.Stock.pop_random())

            # Get the starting snake piece
            c_double = self.Computer.greatest_double()
            p_double = self.Player.greatest_double()
            if c_double > p_double:
                self.Snake.append(c_double)
                self.Computer.remove(c_double)
                self.prep_players_turn()
                ready_to_start = True
            elif p_double > c_double:
                self.Snake.append(p_double)
                self.Player.remove(p_double)
                self.prep_computers_turn()
                ready_to_start = True
            # No doubles were found, restart
            else:
                self.Stock = Dominoes()
                self.Computer = Dominoes()
                self.Player = Dominoes()

    def game_loop(self):
        while not self.game_over():
            self.display_playing_field()
            if self.Players_Turn:
                self.players_turn()
            else:
                self.computers_turn()
        # When the game ends, display the field one last time
        self.display_playing_field()

    def display_playing_field(self):
        print('=' * 70)
        print("Stock size:", len(self.Stock))
        print("Computer pieces:", len(self.Computer))
        print()
        self.print_snake()
        print()
        print("Your pieces:")
        for i in range(len(self.Player)):
            print(str(i + 1) + ':' + str(self.Player[i]))
        print()
        print(self.Status)

    def players_turn(self):
        legal_move = False
        while not legal_move:
            move = self.get_players_move()
            index = abs(move) - 1
            try_domino = self.Player.index(index)
            if move > 0:  # Try to append to Snake
                self.Snake.append(self.Player.pop(index))
            elif move < 0:  # Prepend to Snake
                self.Snake.insert(0, self.Player.pop(index))
            else:  # Take from Stock
                self.Player.append(self.Stock.pop_random())
        self.prep_computers_turn()

    def append_to_snake(self, domino):
        return False

    def prepend_to_snake(self, domino):
        return False

    def get_players_move(self):
        move = int()
        menu_length = len(self.Player)
        valid_input = False
        while not valid_input:
            try:
                move = int(input())
                if -menu_length <= move <= menu_length:
                    valid_input = True
                else:
                    raise ValueError
            except ValueError:
                print("Invalid Input. Please try again.")
        return move

    def computers_turn(self):
        input()  # Press Enter to Continue...
        if random.choice([True, False]):  # Append to Snake
            self.Snake.append(self.Computer.pop_random())
        else:  # Prepend to Snake
            self.Snake.insert(0, self.Computer.pop_random())
        self.prep_players_turn()

    def game_over(self):
        if self.Player.empty():
            self.Status = "Status: The game is over. You won!"
            return True
        elif self.Computer.empty():
            self.Status = "Status: The game is over. The computer won!"
            return True
        elif self.draw_condition():
            self.Status = "Status: The game is over. It's a draw!"
            return True
        return False

    def prep_players_turn(self):
        self.Status = "Status: It's your turn to make a move. Enter your command."
        self.Players_Turn = True

    def prep_computers_turn(self):
        self.Status = "Status: Computer is about to make a move. Press Enter to continue..."
        self.Players_Turn = False

    def print_snake(self):
        snake = str()
        length = len(self.Snake)
        if length <= 6:
            snake = str(self.Snake)
        else:
            for i in range(0, 3):
                snake += str(self.Snake[i])
            snake += '...'
            for i in range(length - 3, length):
                snake += str(self.Snake[i])
        print(snake)

    def draw_condition(self):
        first = self.Snake[0].left
        last = self.Snake[-1].right
        if first == last and self.Snake.count_digit(first) == 8:
            return True
        return False


# Start the game
Game()
