import random
import collections


def rand_roll():
    return random.randrange(1, 6)


def roll_x_dice(x):
    die_dict = {}
    for y in range(x):
        die_dict[y] = rand_roll()
    return die_dict


# Build out my combo definitions
# Return value of combo.
def is_straight(x, y):
    if sorted(x.values()) == [1, 2, 3, 4, 5, 6]:
        return null, 1500 + y


def is_three_pair(x):
    result_list = [0] * 6
    three_pair = [0, 0, 0, 2, 2, 2]
    for i in list(x.values()):
        result_list[(list(x.values())[i]) - 1] += 1
    if result_list.__contains__(6):
        return 1500
    if result_list.__contains__(4) and result_list.__contains__(2):
        return 1500
    if sorted(result_list) == three_pair:
        return 1500
    else:
        return -1


def is_ace(x)


'''
# Commenting this function out.  I don't think 6 of a kind is special
# outside of normal procedural rules.
def is_six_of_kind(x):
    for i in range(6):
        if sorted(x.values()) == [i, i, i, i, i, i]:
            return i * 100 * 
'''
"""
for num in range(10000):
    qq = rollXDice(6)
    if(is_straight(qq)):
        print("got here")
#        break
    if(is_six_of_kind(qq)):
        print("and here")
#        break
    if(is_three_pair(qq)):
        print("Confirmed.  Three Pair.")

"""

# Testing below.  Build a dict, then use it.

goofball = {1: 1, 2: 3, 3: 2, 4: 4, 5: 5, 6: 6}
# if(is_straight(goofball)):
#    print("provided")

goat = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1}
# if(is_six_of_kind(goat)):
#    print("got to goat")

yAak = {1: 1, 2: 1, 3: 2, 4: 3, 5: 2, 6: 3}

print(is_three_pair(yAak))


print(type(list(yAak.values())) is list)
# if(is_three_pair(yAak)):
#    print("Is Three Pair")
