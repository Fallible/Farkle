import random

def randRoll():
    return random.randrange(1, 6)


def rollXDice(x):
    dieDict = {}
    for y in range(x):
        dieDict[y] = randRoll()
    return dieDict


# Build out my combo definitions
def isStraight(x):
   if(sorted(x.values()) == [1, 2, 3, 4, 5, 6]):
      print("winner")
      return(True)

def isSixOfAKind(x):
    for i in range(6):
        if(sorted(x.values()) == [i, i, i, i, i, i]):
            print(i)
            print("was the answer")

def isThreePair(x):
    




#def checkForScore(savedDice):
    #savedDice is a dictionary
    


goat = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}

for num in range(10000):
    qq = rollXDice(6)
    if(isStraight(qq)):
        print("got here")
        quit
    if(isSixOfAKind(qq)):
        print("and here")
        quit

# Testing below.  Build a dict, then use it.

goofball = {1: 1, 2: 3, 3: 2, 4: 4, 5: 5, 6: 6}
if(isStraight(goofball)):
    print("provided")

if(isSixOfAKind(goat)):
    print("got to goat")
