import random
def roulette_game():
    Money= 5000
    while True:
        print('your balance is: {Money}')
        bet = int(input('How much do you want to bet? '))
        print('')
        if bet > Money:
            print ('You dont have enough money fam, wtf?')
            continue
        number = int(input('Which number do you want to bet on?'))
        if number <0 or number > 36:
            print("Invalid number bro")
            continue
        Money -= bet
        spin_number = random.randint(0,36)
        print('')
        if spin_number == number:
            print("You Won!")
            Money += bet*36
        else:
            print('You lost, the number was {spin_number}')
        if Money <= 0:
            print("You ran out of coins, beat it!")
            break
        play_again = input('Do you want to play again (y/n)')
        if play_again.lower == "n": 
            break
        print ('Thanks for playing :)')