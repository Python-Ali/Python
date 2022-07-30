import random
number = random.randint(1,20)
geuss = int(input("I'm thinking of a number from 1 to 20. What is it?"))
while geuss != number:
    if geuss < number:
        print("Your number was too low...")
    if geuss > number:
        print("Your number was too high...")
    geuss = int(input("Please try again..."))
print("Congratulations! Correct answer!")
