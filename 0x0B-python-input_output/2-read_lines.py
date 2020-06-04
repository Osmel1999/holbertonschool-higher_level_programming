#!/usr/bin/python3
"""Module 2-read_lines.py
read (n) lines of a text file
and prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """Read from filename (n) lines 
    and prints to stdout
    
    Args:
       - filename: name of the file
       - nb_lines: number of lines to read
    """

    with open(filename) as f:
        i = 0
        count = 0
        for line in f:
            count += 1
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= count:
            read_text = f.read()
            print(read_text, end="")
        else:
            for line in f:
                print(read_text, end='')
                i += 1
                if i == nb_lines:
                    break
