import random
import collections


def rand_roll():
    return random.randrange(1, 6)


def roll_x_dice(x):
    die_dict = {}
    for y in range(x):
        roll_value = rand_roll()
        die_dict[roll_value] += 1
    return die_dict


def check_combos(score, die_dict):
    current_best = score, die_dict
    if list(die_dict.values()) == [0, 0, 0, 0, 0, 0]:
        return score
    if current_best(score) < is_straight(score, die_dict):
        current_best
    is_three_pair(score, die_dict)
    #is_ace(score, die_dict)
    #is_five(score, die_dict)
    #is_no_score()


#def list_index(die_dict, index):
#    ret_list[6]
#    for value in list(die_dict.values()):
#        if value is not 0:
#            ret_list[value - 1] += 1
#    #ret_list[index] = 0  # I have no idea what I was trying to do with this...
#    return ret_list


# Build out my combo definitions
# Return value of combo.
def is_straight(score, die_dict):
    if sorted(die_dict.values()) == [1, 1, 1, 1, 1, 1]:
        return 1500 + score, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


def is_three_pair(score, die_dict):
    three_pair = [0, 0, 0, 2, 2, 2]
    empty_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    if 6 in die_dict.values():
        return 1500 + score, empty_dict
    elif 4 in die_dict.values() and 2 in die_dict.values():
        return 1500 + score, empty_dict
    elif sorted(list(die_dict.values())) == three_pair:
        return 1500 + score, empty_dict
    else:
        return score, die_dict


def is_set(score, die_list):
    if die_list.__contains__(3):
        return check_combos((die_list.index(3)+1)*100 + score, list_index(die_list, die_list.index(3)))
    if result_list.__contains__(4):
        return check_combos((die_list.index(4)+1)*100*2 + score, list_index(die_list, die_list.index(4)))
    if result_list.__contains__(5):
        return check_combos((die_list.index(5)+1)*100*3 + score, list_index(die_list, die_list.index(5)))
    if result_list.__contains__(6):
        return (die_list.index(6)+1)*100*4 + score, list_index(die_list, die_list.index(6))


#def is_ace(score, die_list):
#    if '1' in die_list.values():
#        return check_combos()


#def is_five(score, die_list):



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


'''
Might need this for sending selected dice into processor
    for i in list(die_list.values()):
        result_list[(list(die_list.values())[i]) - 1] += 1
'''
# Testing below.  Build a dict, then use it.

goofball = {1: 1, 2: 3, 3: 2, 4: 4, 5: 5, 6: 6}
# if(is_straight(goofball)):
#    print("provided")

goat = {1: 2, 2: 2, 3: 2, 4: 0, 5: 0, 6: 0}
# if(is_six_of_kind(goat)):
#    print("got to goat")

yAak = {1: 2, 2: 2, 3: 2, 4: 0, 5: 0, 6: 0}

print(check_combos(0, yAak))

print(is_three_pair(0, yAak))
#print(sorted(yAak.values()))


#print(type(list(yAak.values())) is list)
# if(is_three_pair(yAak)):
#    print("Is Three Pair")
