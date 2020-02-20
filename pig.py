from random import randint

class Game:
    def __init__(self):
        self.computer = Computer("Computer")
        self.player = Player("Player")
        self.die = Die()

    def choose_starting_player(self):
        rng = randint(1, 10)
        if rng < 6:
            print("Computer goes first.")
            self.computer.round()

        else:
            print("Player goes first.")
            self.player.round()

class Die:
    def __init__(self):
        self.value = randint(1, 6)

    def __str__(self):
        return f"{self.value}"

class Computer:
    def __init__(self, name):
        self.name = name 
        self.round_score = 0
        self.computer_score = 0


    def __str__(self):
        return f"{self.name}"

    def round(self):
        if self.round_score < 20:
            roll = Die().value
            print(f"Computer rolls {roll}")
            if roll != 1:
                self.round_score += roll
                print(f"Round score is {self.round_score}")
                self.round()
            else:
                print("Pig!") 
                self.round_score = 0
                self.computer_score += self.round_score
                print(f"Computer's total score is {self.computer_score}")
                print("Computer holds")
                self.computer_score += self.round_score
                print(f"Computer's total score is {self.computer_score}")
        else: 
            print("Computer holds")
            self.computer_score += self.round_score
            print(f"Computer's total score is {self.computer_score}")


class Player:
    def __init__(self, name):
        self.name = name 
        self.round_score = 0
        self.player_score = 0

    def __str__(self):
        return f"{self.name}"

    def round(self):
        choice = input("Do you want to (r)oll or (h)old? ")
        while choice != 'h':
            roll = Die().value
            print(f"You rolled {roll}")
            self.round_score += roll
            print(f"Your score for this round is {self.round_score}")
            choice = input("Do you want to (r)oll or (h)old? ")
        if choice == "h": 
            self.player_score += self.round_score
            print(f"Your total score is {self.player_score}")


game = Game()
game.choose_starting_player()