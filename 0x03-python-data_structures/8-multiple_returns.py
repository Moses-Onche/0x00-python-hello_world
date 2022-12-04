#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        max = [0, None]
        return max
    else:
        max = [len(sentence), sentence[0]]
        return max
"""    invalid = my_list is None or len(my_list) == 0
       if invalid:
        return "None"
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return max """
