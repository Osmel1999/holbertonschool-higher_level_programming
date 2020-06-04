#!/usr/bin/python3
"""Module 1-number_of_lines.py
returns the number of lines of a file
"""
def number_of_lines(filename=""):
    """Count the number of lines of 
    a file and return that number
    Args:
        - filename: name of the file

    Returns:
        - number of lines
    """

    count = 0

    with open(filename) as f:
        text = f.readlines()
        for line in text:
            count += 1
    return count
