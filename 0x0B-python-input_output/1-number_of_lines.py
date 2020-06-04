#!/usr/bin/python3
"""Module 1-number_of_lines.py
returns the number of lines of a file
"""
def number_of_lines(filename=""):
    """Count the number of lines of 
    a file and return that number
    Args:
        - filename: name of the file
    """
    with open(filename, 'r') as f:
        for line in f:
            count += 1
    return count
