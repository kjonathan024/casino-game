import random

class Player:
    #maybe add the leveling
    def __init__(self, name):
        self.name = name
        self.cash = 1000
        self.initial_cash = 1000
    
    def greeting(self):
        print(f"Hello {self.name}!")
        spacer(2)

    def __repr__(self):
        return f'You have {self.cash} dollars.'

class Horse:
    def __init__(self,speed,luck):
        self.speed = speed
        self.luck = luck
    def __repr__(self):
        return f'Horse with speed {self.speed} and luck {self.luck}%'        

def spacer(int=3):
    for i in range(int):
        print()

def bet(player):
    bet = 0
    while bet == 0 or bet > player.cash:
        try:
            bet = int(input("How much would you like to bet? "))
            spacer(1)
            if bet > player.cash:
                print(f"Invalid Bet Amount: You have {player.cash} dollars to bet.")
                spacer(1)
        except ValueError:
            print(f"Invalid Bet Amount: You have {player.cash} dollars to bet.")
            spacer(1)
            continue
    return bet

def win(player, bet, multiplier):
    print(f"You won {bet*multiplier} dollars!")
    setattr(player, 'cash', int(getattr(player,'cash'))+(bet*multiplier))

def lose(player, bet):
    print(f"You lost {bet} dollars.")
    setattr(player, 'cash', int(getattr(player,'cash'))-bet)

def blackjack():
    #will add logic soon
    #make sure to check that the bet is not over the amount of money they have
    print("this is blackjack")
    pass

def horses():
    #will add logic soon
    #gameplan: generate random horse objects and list their characteristics to the players. Have speed be the determinant and add luck factor to each horse
    spacer(5)
    print("Welcome to Horses!")
    spacer(1)
    #store horse objects in a List?
    horse_catalog = []
    for i in range(4):
        horse_catalog.append(Horse(random.randint(1,40),random.randint(0,50)))
    horse_catalog.sort(key = lambda Horse:  -Horse.speed) 
    print(horse_catalog)
    

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
    #choose bet amount using bet() function
    bet_amount = bet(player)  
    #50/50
    if game_type == types[0]:
        side = None
        while side != 0 and side != 1:
            spacer(1)
            side = int(input("Do you want to bet on the lower three numbers (type '0') or the upper three (type '1')? "))
            if side !=0 and side !=1:
                spacer(1)
                print(f"{side} is not a valid response.")
            else:
                result = random.randint(0,1)
                print(f"Here's the Roll! upper" if result ==1 else f"Here's the Roll! lower")
                if side == result:
                    win(player,bet_amount, 2)
                else:
                    lose(player,bet_amount)
    #single number
    else:
        spacer(1)
        choice = None
        while choice not in [1,2,3,4,5,6]:
            choice = int(input("Which number would you like to bet on? Choose any number from 1 to 6: "))
            if choice not in [1,2,3,4,5,6]:
                spacer(1)
                print(f"{choice} is not a valid response.")
            else:
                result = random.randint(1,6)
                spacer(1)
                print(f"Here's the Roll! {result}")
                if choice == result:
                    win(player,bet_amount, 5)
                else:
                    lose(player,bet_amount)
        

def gameSelect():
    list = ['blackjack', 'horses', 'dice', 'exit']
    print("We have three games to choose from: blackjack, horses, and dice.")
    print("## You may also type 'exit' if you wish to leave. ##")
    game = input("Which one would you like to play? ")
    if game.lower() in list:
        if game == list[0]:
            blackjack()
        elif game == list[1]:
            horses()
        elif game == list[2]:
            dice()
        else:
            return False
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
gameState = True
while getattr(player, 'cash') > 0 and gameState:
    gameState = gameSelect()
    

print("Thanks for playing!")
print(f'Here\'s your P/L: {player.cash - player.initial_cash}')