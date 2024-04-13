import random
from replit import clear

def add_player_cards():
    player_score = 0
    for i in range(len(player_cards)):
        if(player_cards[i] == "K" or player_cards[i] == "Q" or player_cards[i] == "J"):
            player_score += 10
        elif(player_cards[i] == "A"):
            value = int(input("What you value do you want A be 1 or 11 : "))
            player_score += value
        else:
            player_score += player_cards[i]
    return player_score

def add_computer_cards():
    computer_score = 0
    for i in range(len(computer_cards)):
        if(computer_cards[i] == "K" or computer_cards[i] == "Q" or computer_cards[i] == "J"):
            computer_score += 10
        elif(computer_cards[i] == "A"):
            value = [1,11]
            computer_score += value[random.randint(0,1)]
        else:
            computer_score += computer_cards[i]
    return computer_score

play = "Y"
player_amount = 2000

while(play == "Y"):
    clear()
    cards = [2,3,4,5,6,7,8,9,10,"K","Q","J","A"]

    player_cards = []
    computer_cards = []

    while(len(player_cards) < 2):
        player_cards.append(cards[random.randint(0,12)])

    computer_cards.append(cards[random.randint(0,12)])


    print(f"Amount you have : ${player_amount}")
    bet = int(input("Place your bet : $ "))

    while(bet > player_amount):
        bet = int(input("Place a bet less than the amount you have : $"))

    player_amount = player_amount - bet
    print(f"Amount Left : ${player_amount}")
    print(f"Bet : ${bet}")

    print(f"Your cards : {player_cards}")
    print(f"Computer cards : {computer_cards}")

    computer_score = add_computer_cards()
    player_score = add_player_cards()

    place_bet = input("Do you want to draw another card Y or N : ").upper()

    if(place_bet == "Y"):
        player_cards.append(cards[random.randint(0,12)])
        computer_cards.append(cards[random.randint(0,12)])
        computer_score = add_computer_cards()
        player_score = add_player_cards()
        
        if(computer_score < 17):
            computer_cards.append(cards[random.randint(0,12)])
            computer_score = add_computer_cards()

        if(player_score > 21 or player_score < computer_score):
            print(f"Your cards : {player_cards}\nComputer cards : {computer_cards}\nComputer Score : {computer_score} and Player Score : {player_score}\nPlayer Lose")
            print(f"Amount Left : ${player_amount}")
            play = input("Do you want to play again ? Y or N : ").upper()
        elif(player_score == computer_score):
            print(f"Your cards : {player_cards}\nComputer cards : {computer_cards}\nComputer Score : {computer_score} and Player Score : {player_score}\nGame Draw")
            player_amount += bet
            print(f"Amount Left : ${player_amount}")
            play = input("Do you want to play again ? Y or N : ").upper()
        else:
            print(f"Your cards : {player_cards}\nComputer cards : {computer_cards}\nComputer Score : {computer_score} and Player Score : {player_score}\nPlayer Won")
            player_amount = player_amount + (bet * 2)
            print(f"Amount Left : ${player_amount}")
            play = input("Do you want to play again ? Y or N : ").upper()

    elif(place_bet == "N"):
        computer_cards.append(cards[random.randint(0,12)])
        computer_score = add_computer_cards()

        if(player_score < computer_score):
            print(f"Your cards : {player_cards}\nComputer cards : {computer_cards}\nComputer Score : {computer_score} and Player Score : {player_score}\nPlayer Lose")
            print(f"Amount Left : ${player_amount}")
            play = input("Do you want to play again ? Y or N : ").upper()
        elif(player_score == computer_score):
            print(f"Your cards : {player_cards}\nComputer cards : {computer_cards}\nComputer Score : {computer_score} and Player Score : {player_score}\nGame Draw")
            player_amount += bet
            print(f"Amount Left : ${player_amount}")
            play = input("Do you want to play again ? Y or N : ").upper()
        else:
            print(f"Your cards : {player_cards}\nComputer cards : {computer_cards}\nComputer Score : {computer_score} and Player Score : {player_score}\nPlayer Won")
            player_amount = player_amount + (bet * 2)
            print(f"Amount Left : ${player_amount}")
            play = input("Do you want to play again ? Y or N : ").upper()
        
print(f"You have ${player_amount}")