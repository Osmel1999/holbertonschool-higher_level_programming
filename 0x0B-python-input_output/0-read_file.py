#!/usr/bin/python3
""" Module 0-read_file.
Reads from a file and prints
"""

def read_file(filename=""):
    with open(filename, 'r') as f:
        read_data = f.read()
        print(read_data, end="")
