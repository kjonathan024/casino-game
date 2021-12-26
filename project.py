class Player:
    def __init__(self, name):
        self.name = name
        self.cash = 1000
    
    def greeting(self):
        print(f"Hello {name}!")
        spacer(2)

    def __repr__(self):
        return f'You have {cash} dollars.'

def spacer(int=3):
    for i in range(int):
        print()

def blackjack():
    #will add logic soon
    #make sure to check that the bet is not over the amount of money they have
    pass

def horses():
    #will add logic soon
    pass

def dice():
    #will add logic soon
    pass

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