import random
import collections


def randRoll():
    return random.randrange(1, 6)


def rollXDice(x):
    die_dict = {}
    for y in range(x):
        die_dict[y] = randRoll()
    return die_dict


# Build out my combo definitions
def isStraight(x):
    if sorted(x.values()) == [1, 2, 3, 4, 5, 6]:
        return True


def isSixOfAKind(x):
    for i in range(6):
        if sorted(x.values()) == [i, i, i, i, i, i]:
            return True


def isThreePair(x):
    result_list = [0] * 6
    for i in list(x.values()):
        result_list[(list(x.values())[i]) - 1] += 1
    if result_list.__contains__(6):
        return True
    if result_list.__contains__(4) && result_list.__contains__(2):
        return True
    print(result_list)


"""
for num in range(10000):
    qq = rollXDice(6)
    if(isStraight(qq)):
        print("got here")
#        break
    if(isSixOfAKind(qq)):
        print("and here")
#        break
    if(isThreePair(qq)):
        print("Confirmed.  Three Pair.")

"""

# Testing below.  Build a dict, then use it.

goofball = {1: 1, 2: 3, 3: 2, 4: 4, 5: 5, 6: 6}
# if(isStraight(goofball)):
#    print("provided")

goat = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
# if(isSixOfAKind(goat)):
#    print("got to goat")

yAak = {1: 1, 2: 1, 3: 2, 4: 3, 5: 2, 6: 3}

if isThreePair(yAak):
    print("Three Pair Confirmed")

print(type(list(yAak.values())) is list)
# if(isThreePair(yAak)):
#    print("Is Three Pair")
