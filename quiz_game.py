print("Welcome to my quiz :)")

score = 0

playing = input("Do you want to play? ")

if playing != "yes":
    
    quit()

print("Very well! Let's play :3")

answer = input("How many brain cells do orange cats have? ")
if answer.lower() == "one":
    print("Correct!")
    score +=1     
else:
    print("Incorrect!")
    
answer = input("Are cats a liquid? ")
if answer.lower() == "yes":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("Are you a liquid? D: ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Meow? ")
if answer.lower() == "meow":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!" )
print("That means you got " +str((score /4) * 100) + "%")
    