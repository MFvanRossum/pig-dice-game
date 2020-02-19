from random import randint

class Game:
    def __init__(self):
        self.computer = Computer("Computer")
        self.player = Player("Player")
        self.die = Die()

    def choose_starting_player(self):
        rng = randint(1, 10)
        print(f"{rng}")
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
        self.roll_die = Die()


    def __str__(self):
        return f"{self.name}"

    def round(self):
        self.roll_die.value
        print(f"Computer rolls {self.roll_die.value}")
        if self.roll_die.value != 1:
            if self.round_score < 20:
                self.round_score += self.roll_die.value
                print(f"Round score is {self.round_score}")
                self.roll_die.value
                print(f"Computer rolls {self.roll_die.value}")
            else: 
                # self.hold
                print("Computer holds")
                self.round_score += self.computer_score
                print(f"Computer's total score is {self.computer_score}")
        else: 
            print("Pig!")
            self.round_score = 0
            self.round_score += self.computer_score
            print(f"Computer's total score is {self.computer_score")


class Player:
    def __init__(self, name):
        self.name = name 
        self.round_score = 0
        self.player_score = 0
        self.roll_die = Die()

    def __str__(self):
        return f"{self.name}"

    def round(self):
        choice = input("Do you want to (r)oll or (h)old? ")
        while choice != 'h':
            self.roll_die.value
            print(f"You rolled {self.roll_die.value}")
            self.round_score += self.roll_die.value
            print(f"Your score for this round is {self.round_score}")
            choice = input("Do you want to (r)oll or (h)old? ")
            if choice == "h": 
                self.round_score += self.player_score
                print(f"Your total score is {self.player_score}")


game = Game()
game.choose_starting_player()