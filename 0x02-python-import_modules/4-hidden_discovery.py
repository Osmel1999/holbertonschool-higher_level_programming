#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    t = dir()
    for i in range(0, len(t)):
        if t[i][0:2] != "__":
            print("{}".format(t[i]))
