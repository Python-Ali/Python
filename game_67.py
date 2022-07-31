woman = ["scientist", "qeeun", "pirate", "giant rabbit"]
man = ["police officer", "artist", ", your granfather", "killer robot"]
place = ["in a Lay's factory.", "at the super market.", "in a spooky, bat-filled cave.", "on the beach."]
sW = ["scuba diving gear.", "fairy wings.", "a long glittering gown.", "jeans and a T-shirt."]
mW = ["a purple suit.", " beach shorts and a T-shirt.", "pyjamas and a dressing gown.", "shark costume."]
wS = ["Who are you?", "12,5 X 100 + 43?"]
mS = ["Don't count your chickens before they hatch.", "X = N x g = g = 3456,34 - N = 73847,738"]
X = ("The man droped a chips packet. Earth said, stop littering on me! Earth created an earthquake and they were swallowed up. The lesson is, do not litter.")
H = ("The woman droped a chips packet. Earth said, stop littering on me! Earth created an earthquake and they were swallowed up.  The lesson is, do not litter.")
D = ("The man made a fire to warm the two of them. The Earth said, this is what causes global warming and burns me! Earth created a rainstorm which caused the fire to go out and the two of them to get soaking wet.    Lesson is, do not make fires too often or in the open")
A = ("The woman made a fire to warm the two of them. The Earth said, this is what causes global warming and burns me! Earth created a rainstorm which caused the fire to go out and the two of them to get soaking wet.    Lesson is, do not make fires too often or in the open")
L = [(X), (H), (D), (A)]
import random
while True:
    print("A female", random.choice(woman), "met a male", random.choice(man), random.choice(place))
    print("She was wearing", random.choice(sW))
    print("He was wearing", random.choice(mW))
    print("She said,",random.choice(wS))
    print("He said,",random.choice(mS))
    print(random.choice(L))
    print()
    input("Press enter to play again.")
    print()
