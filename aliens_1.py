aliens = 2
password = "ALIENS"
print("Quikly! Aliens are nvading the planet.")
print("You need to activate the global defence platform.")
print("Hope you know the password, for Earth's sake...")
print()
print("--------------------------------------------------")
print("     WELCOME TO THE GLOBAL DEFENCE NETWORK       ")
print("--------------------------------------------------")
geuss = input("Please enter the password: ").upper()
while geuss != password:
    print()
    print("INCORRECT PASSWORD")
    print()
    aliens = aliens * 2 * 2 * 4
    print("There are",aliens, "aliens now on Earth. Try again!")
    if aliens > 7400000000:        break
    print()
    print("Password hint: the things that are attacking us.")
    print()
    geuss = input("Quick! Please enter the password: ").upper()
if aliens < 7400000000:
    print("Nooooo! The aliens have outnumbered us. All is lost.")
else:
    print("Hooray! We won the fight and the world is saved!")
# This is a python program so it probably will not work for other languages
