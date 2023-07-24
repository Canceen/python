import random
souls = int(5000)

if souls <= 0:
    quit

print("Hello, welcome to the doom dice game") 
print("We will both roll 2 dice, I will roll mine first. ")

playing = input("Do you want to play?")

if playing.lower != "y":
    quit

print("You have", int(souls), "souls")    
soulsbet = input("How many souls do you wish to gamble? ")
if int(soulsbet) >> int(souls):
    print("You do not have enough souls")
else:
    souls = int(souls) - int(soulsbet)
    print("Very well")
print ("The captain picks up his dice.. and throws one out onto the deck!")

x1 = random.randint(1,6)
print("The Captain rolls a", int(x1),"!")
if x1 == 1:
    print("One half of the snakes eye!")

y1 = input("")        
    
    
    
    
    
    
    
    
    
x2 = random.randint(1,6)
print("The captain picks up the other die and rolls ")
print("And it'2",int(x2),"!")
if x2 == 1:
    print("Snake eyes for the captain!! You lose!")





#captainsroll1 = int(1,6) 
#captainsroll2 = int(1,6)

#print("The captain rolls")