#!/usr/bin/python3
def multiple_returns(sentence):
    for i in range(len(sentence)):
        if i == 1:
            c = sentence[i]
        elif i <= 0:
            return "None"
        else:
            print("Length: {:d} -First character: {:d}".format(i, c))

