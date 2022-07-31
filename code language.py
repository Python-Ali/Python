alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
StrinEncry = input("Please enter a message to encrypt: ")
StrinEncry = StrinEncry.upper()
shiftAmount = int(input("Please enter a whole number from 1-25 to be your key."))
encrystring = ""
for currentCharacter in StrinEncry:
    position = alpha.find(currentCharacter)
    newPosition = position + shiftAmount
    encrystring = encrystring + alpha[newPosition]
print("Your encrypted message is", encrystring)
# This is a python program and it probably won't work for other languages.
