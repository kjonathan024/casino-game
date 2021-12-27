import random

class Player:
    def __init__(self, name):
        self.name = name
        self.cash = 1000
        self.initial_cash = 1000
    
    def greeting(self):
        print(f"Hello {self.name}!")
        spacer(2)

    def __repr__(self):
        return f'You have {self.cash} dollars.'

def spacer(int=3):
    for i in range(int):
        print()

def blackjack():
    #will add logic soon
    #make sure to check that the bet is not over the amount of money they have
    print("this is blackjack")
    pass

def horses():
    #will add logic soon
    print("this is horses")
    pass

def dice():
    #will add logic soon
    dice_options = [1,2,3,4,5,6]
    spacer(5)
    print("Welcome to Dice!")
    spacer(1)
    game_type = ''
    #choose bet type (upper vs. lower, 1 out of 6)
    types = ['fifty','single']
    while game_type not in types:
        spacer(1)
        game_type = input("Would you like to do a fifty-fifty (type 'fifty) or a single-number game? (type 'single') ")
        spacer(1)
    #choose bet amount
    bet = 0
    while bet == 0 or bet > player.cash:
        bet = int(input("How much would you like to bet? "))
        spacer(1)
        if bet > player.cash:
            print(f"Invalid Bet Amount: You have {player.cash} dollars to bet.")
            spacer(1)    
    if game_type == types[0]:
        side = None
        while side != 0 and side != 1:
            spacer(1)
            side = int(input("Do you want to bet on the lower three numbers (type '0') or the upper three (type '1')? "))
            if side !=0 and side !=1:
                spacer(1)
                print(f"{side} is not a valid response.")
            elif side == 0:
                result = random.randint(1,6)

    else:
        pass

def win(player, bet, multiplier):
    setattr(player, 'cash', int(getattr(player,'cash'))+(bet*multiplier))

def lose(player, bet):
    setattr(player, 'cash', int(getattr(player,'cash'))-bet)
    

def gameSelect():
    list = ['blackjack', 'horses', 'dice']
    print("We have three games to choose from: blackjack, horses, and dice.")
    game = input("Which one would you like to play? ")
    if game.lower() in list:
        if game == list[0]:
            blackjack()
        elif game == list[1]:
            horses()
        else:
            dice()
    else:
        print("This is not a valid response.")
        spacer(1)
        gameSelect()

#Terminal Active (Main Game Portion)
print("Welcome to the casino game!")
spacer(2)
name = input("What is your name? ")
player = Player(name)
player.greeting()
while getattr(player, 'cash') > 0:
    gameSelect()
    break

print("Thanks for playing!")
print(f'Here\'s your P/L: {player.cash - player.initial_cash}')