"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import string
import time
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        # no moves stored to memory when a new object is created
        self.my_move = ''
        self.their_move = ''

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        # keeps track of every move made
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            human_move = input('Rock, Paper or Scissors?: \n'.lower())
            if human_move.lower() in moves:
                return human_move
                break
            else:
                print_pause('Invalid. Please try again\n')


class ReflectPlayer(Player):
    '''Subclass of the Player class, remembers what move the opponent
    played last round, and plays that move this round
    (In other words, if user plays 'paper' on the first round,
    a ReflectPlayer will play 'paper' on the second round.)
    In the first round it will return a random move.
    '''
    def move(self):
        if self.their_move == '':
            return random.choice(moves)
        elif self.their_move == 'rock':
            return 'rock'
        elif self.their_move == 'paper':
            return 'paper'
        else:
            return 'scissors'


class CyclePlayer(Player):
    '''Remembers what move it played last round, and cycles through
    the different moves (If it played 'rock' this round, it should play
    'paper' in the next round.) In the first round it will return
    a random move.
    '''
    def move(self):
        if self.my_move == '':
            return random.choice(moves)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        else:
            return 'rock'


def beats(one, two):
    return (
            (one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock')
           )


def print_pause(printmessage):
    print(printmessage)
    time.sleep(1)


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        # Setting initial player scores to 0.
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        # Get move of each player
        move1 = self.p1.move()
        move2 = self.p2.move()
        # print_pause each player's move
        print_pause(f"Player 1: {move1} // Player 2: {move2}")
        # determine which player move won
        if move1 == move2:
            print_pause("Tie!")
        elif beats(move1, move2):
            print_pause("Player 1 wins!")
            self.p1_score += 1
        else:
            print_pause("Player 2 wins!")
            self.p2_score += 1
        # print_pause player scores
        print_pause(f'\nScores: \nPlayer 1: {self.p1_score}'
                    f'\nPlayer 2: {self.p2_score}\n')
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print_pause("\nGame start!")
        for round in range(3):
            print_pause(f"\n**Round {round}**")
            self.play_round()
        print_pause("Game over!")
        # prompts at the end of every game session
        print_pause(f'\nFinal Score: \nPlayer 1: {self.p1_score}'
                    f'\nPlayer 2: {self.p2_score}\n')
        if self.p1_score > self.p2_score:
            print_pause('* PLAYER ONE WINS *')
        elif self.p1_score < self.p2_score:
            print_pause('* PLAYER TWO WINS *')
        else:
            print_pause('* TIE GAME *')
        self.restart_game()

    def restart_game(self):
        # ask if the user wants to play again
        while True:
            restart = input('Would you like to play again? '
                            'Enter Yes or No.\n')
            if restart.lower() == 'yes':
                self.p1_score = 0
                self.p2_score = 0
                self.play_game()
                break
            elif restart.lower() == 'no':
                print_pause('Goodbye and thanks for playing!')
                break
            else:
                print_pause('Invalid. Please try again\n')


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
