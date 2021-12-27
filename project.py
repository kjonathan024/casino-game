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

class Horse:
    def __init__(self,speed,luck):
        self.speed = speed
        self.luck = luck
        self.name = "Horse"

    def __repr__(self):
        return f'Speed: {self.speed} Luck: {self.luck}%'

    def lucky(self):
        if self.luck != 0:
            luck = None
            luck = self.luck <= random.randint(1,100)
            if luck:
                spacer(1)
                print(f'{self.name} is feeling lucky!')
            return luck


def spacer(int=3):
    for i in range(int):
        print()

def horseAlgorithm(horse_list, choice, bet, mults):
    luckies = []
    for horse in horse_list:
        if len(luckies) == 0 and horse.lucky():
            luckies.append(horse)
    if len(luckies) == 0:
        return horse_list[choice] == horse_list[0]
        #aka choice == 0 (wrote more wordy version for easier readability)
    
    else:
       return horse_list[choice] == luckies[0] 
        

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
    spacer(5)

def lose(player, bet):
    print(f"You lost {bet} dollars.")
    setattr(player, 'cash', int(getattr(player,'cash'))-bet)
    spacer(5)

def blackjack():
    #will add logic soon
    spacer(5)
    print("Welcome to Blackjack!")
    spacer(1)
    card_list = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
    count_list = []
    count = 0
    bet_amount = bet(player)
    print("Let's begin the game...")
    spacer(1)
    dealer_count = 0
    dealer_count_list = []
    dealer_count += hitCard(dealer_count,dealer_count_list,1,None)
    count = hitCard(count,count_list,2)
    turnOver = False
    while isNotOver(count) and not turnOver:
        choice = ''
        spacer(1)
        print(count_list)
        while choice not in ("hit","stand"):
            choice = input(f"The dealer is showing a {dealer_count_list}\nYour total is {count}: would you like to hit (type 'hit') or stand (type 'stand')? ")
            if choice not in ("hit","stand"):
                print("Invalid option.")
                spacer(1)
            if choice == "hit":
                count = hitCard(count,count_list)
            else:
                spacer(1)
                print("You've chosen to stand, good luck!")
                spacer(1)
                turnOver = True
    if isNotOver(count):
        dealer_count = hitCard(dealer_count,dealer_count_list,1,"Dealer")
        while isNotOver(dealer_count) and dealer_count < 17:
            dealer_count = hitCard(dealer_count,dealer_count_list,1,"Dealer")

        print(f'Dealer Cards: {dealer_count_list}')
        print(f'The dealer has {dealer_count}.')
        if dealer_count > count and isNotOver(dealer_count):
            lose(player, bet_amount)
        elif dealer_count == count:
            print("Push")
        else:
            win(player,bet_amount,2)

    else:
        print("Busted!")
        lose(player,bet_amount)
    
def isNotOver(count):
    if count > 21:
        spacer(1)
        return False
    else:
        return True

#I think I need to write a function to count up the cards from the list and just use that to change the Ace value while showing
#No difference to the user

def cardCount(count_list):
    card_list = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
    total = 0
    ace_counter = 0
    for item in count_list:
        if item in {10, 'Jack', 'Queen', 'King'}:
            total += 10
        elif item == 'Ace':
            ace_counter += 1
        else:
            total += item
    while ace_counter > 0:
        if total + ace_counter*11 > 21:
            total +=1
        else:
            total += 11
        ace_counter -=1
    return total

def hitCard(count, count_list, times=1, name = "You"):
    #fix logic for if we have an existing ace that needs to become a one. 
    #Currently, if we have an ace, we just subtract 10 if it would go over 21, but this is flawed logic.
    card_list = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
    for i in range(times):
        hit = random.choice(card_list)
        count_list.append(hit)
        if name != None:
            print(f'{name} got a {hit}')
    return cardCount(count_list)

def horses():
    spacer(5)
    print("Welcome to Horses!")
    spacer(1)
    #store horse objects in a List?
    horse_catalog = []
    names = ["Flash", "Spike", "Sleepster", "Lucy"]
    multipliers = [2,3,6,10]
    for i in range(4):
        horse_catalog.append(Horse(random.randint(1,40),random.randint(0,40)))
    horse_catalog.sort(key = lambda Horse:  -Horse.speed)
    print("Here are our horse options today:")
    for i in range(len(horse_catalog)):
        horse_catalog[i].name = names[i]
        print(f'{horse_catalog[i].name}: {horse_catalog[i]} + Bet Multiplier: {multipliers[i]}')
    spacer(2)
    bet_amount = bet(player)
    choice = ""
    while choice not in names:
        choice = str(input("Which horse would you like to place a bet on? ")).title()
        if choice not in names:
            print("Invalid Horse, try again.")
            spacer(1)
    spacer(1)
    print(f"You have chosen {choice}, good choice!")
    print(f'Let\'s find out if {choice} is today\'s winner!')
    choice_num = names.index(choice)
    if horseAlgorithm(horse_catalog, choice_num, bet_amount, multipliers):
        print(f"{choice} was the winner!")
        spacer(1)
        win(player, bet_amount, multipliers[choice_num])
    else: 
        print(f"{choice} was not the winner.")
        spacer(1)
        lose(player, bet_amount)
    

def dice():
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
    spacer(1)
    print("## You may also type 'exit' if you wish to leave. ##")
    spacer(2)
    game = input("Which one would you like to play? ")
    if game.lower() in list:
        if game == list[0]:
            blackjack()
            return True
        elif game == list[1]:
            horses()
            return True
        elif game == list[2]:
            dice()
            return True
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
    
spacer()
print("Thanks for playing!")
print(f'Here\'s your P/L: {player.cash - player.initial_cash}')