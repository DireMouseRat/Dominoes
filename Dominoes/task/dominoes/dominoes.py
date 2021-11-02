import random


def domino_score(domino):
    return domino.score


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

    def appearance_count(self, number):
        count = 0
        for d in self:
            count += 1 if d.left is number else 0
            count += 1 if d.right is number else 0
        return count

    def pop_random(self):
        return self.pop(random.randrange(0, len(self)))

    def play(self, d):
        self.remove(d)
        return d


class Domino:
    def __init__(self, left=-1, right=0):
        self.left = left
        self.right = right
        self.double = left == right
        self.score = 0

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
                self.prep_player_turn()
                ready_to_start = True
            elif p_double > c_double:
                self.Snake.append(p_double)
                self.Player.remove(p_double)
                self.prep_computer_turn()
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
                self.start_player_turn()
            else:
                self.start_computer_turn()
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

    def start_player_turn(self):
        legal_move = False
        while not legal_move:
            move = self.get_player_move()
            index = abs(move) - 1
            # Positive, try to append to Snake
            if move > 0:
                if self.Snake[-1].right == self.Player[index].left:  # Snake right digit equals Domino left digit
                    self.Snake.append(self.Player.pop(index))  # Append to Snake
                    legal_move = True
                elif self.Snake[-1].right == self.Player[index].right:  # Snake right digit equals Domino right digit
                    self.Player[index].rotate()  # Rotate the domino
                    self.Snake.append(self.Player.pop(index))  # Append to Snake
                    legal_move = True
            # Negative, try to Prepend to Snake
            elif move < 0:
                if self.Snake[0].left == self.Player[index].left:  # Snake left digit equals Domino left digit
                    self.Player[index].rotate()  # Rotate the domino
                    self.Snake.insert(0, self.Player.pop(index))  # Prepend to the snake
                    legal_move = True
                elif self.Snake[0].left == self.Player[index].right:  # Snake left digit equals Domino right digit
                    self.Snake.insert(0, self.Player.pop(index))  # Prepend to the snake
                    legal_move = True
            # Take from Stock
            else:
                if len(self.Stock) > 0:
                    self.Player.append(self.Stock.pop_random())
                legal_move = True
            if not legal_move:
                print('Illegal move. Please try again.')
        self.prep_computer_turn()

    def get_player_move(self):
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

    def start_computer_turn(self):
        input()  # Press Enter to Continue...

        # AI scores each domino in its hand
        # Each key is a Number (0 - 6), and the value is the count of appearances of that Number
        key_appearances = dict()
        for i in range(0, 7):
            key_appearances[i] = self.Snake.appearance_count(i) + self.Computer.appearance_count(i)
        # A Domino's score is equal to its left Number count plus its right Number count
        for d in self.Computer:
            d.score = key_appearances[d.left] + key_appearances[d.right]
        # Sort the Computer hand by domino score with the highest value first
        self.Computer.sort(key=domino_score, reverse=True)

        starting_length = len(self.Computer)
        for d in self.Computer:
            # Try to append to Snake
            if self.Snake[-1].right == d.left:  # Snake right digit equals Domino left digit
                self.Snake.append(self.Computer.play(d))  # Append to Snake
                break
            elif self.Snake[-1].right == d.right:  # Snake right digit equals Domino right digit
                d.rotate()  # Rotate the domino
                self.Snake.append(self.Computer.play(d))  # Append to Snake
                break
            # Try to Prepend to Snake
            elif self.Snake[0].left == d.left:  # Snake left digit equals Domino left digit
                d.rotate()  # Rotate the domino
                self.Snake.insert(0, self.Computer.play(d))  # Prepend to the snake
                break
            elif self.Snake[0].left == d.right:  # Snake left digit equals Domino right digit
                self.Snake.insert(0, self.Computer.play(d))  # Prepend to the snake
                break
        # Take from Stock if a piece wasn't played
        if len(self.Computer) == starting_length:
            self.Computer.append(self.Stock.pop_random())
        self.prep_player_turn()

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

    def prep_player_turn(self):
        self.Status = "Status: It's your turn to make a move. Enter your command."
        self.Players_Turn = True

    def prep_computer_turn(self):
        self.Status = "Status: Computer is about to make a move. Press Enter to continue..."
        self.Players_Turn = False

    def print_snake(self):
        snake = str()
        if len(self.Snake) <= 6:
            snake = str(self.Snake)
        else:
            for domino in self.Snake[0:3]:
                snake += str(domino)
            snake += '...'
            for domino in self.Snake[-3:0]:
                snake += str(domino)
        print(snake)

    def draw_condition(self):
        first = self.Snake[0].left
        last = self.Snake[-1].right
        if first == last and self.Snake.appearance_count(first) == 8:
            return True
        return False


# Start the game
Game()
