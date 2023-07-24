import random

playerIn = True
dealerIn = True

#deck of cards / player dealer hand

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        "J", "Q", "K","A", "J", "Q", "K","A", "J", "Q", "K","A", "J", "Q", "K","A"]
playerhand = []
dealerhand = []

#deal the cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

#calculate the total of each hand

def total(turn):
    total = 0
    face = [ "K", "Q", "J"]
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total

#check for winner

def revealDealerHand():
    if len(dealerhand) == 2:
        return dealerhand[0]
    elif len(dealerhand) > 2:
        return dealerhand[0], dealerhand [1]

#game loop

for _ in range(2):
    dealCard(dealerhand)
    dealCard(playerhand)
    
while playerIn or dealerIn:
    print(f"Dealer has {revealDealerHand()} and X")
    print(f"You Have {playerhand} for a total of {total(playerhand)}")
    if playerIn:
        stayorhit = input("1: Stay\n 2: Hit\n")
    if total(dealerhand) > 17:
        dealerIn = False
    else:
        dealCard(dealerhand)
    if stayorhit == "1":
        playerIn = False
    else:
        dealCard(playerhand)
    if total(playerhand) >= 21:
        break
    elif total (dealerhand) >= 21:
        break
    
if total(playerhand) == 21:
    print (f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print ("BlackJack!")
elif total (dealerhand) == 21:
    print (f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print ("BlackJack! Dealer Wins!")
elif total(playerhand) > 21:
    print(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("You bust brokie!! Dealer Wins!")
elif total(dealerhand) > 21:
    print(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("The dealer bust!, You win!")
elif 21 - total(dealerhand) < 21 - total(playerhand):
    print(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("You bust brokie!! Dealer Wins!")
elif 21 - total(dealerhand) > 21 - total(playerhand):
    print(f"\nYou have {playerhand} for a total of {total(playerhand)} and the dealer has {dealerhand} for a total of {total(dealerhand)}")
    print("You Win!")
    
    

