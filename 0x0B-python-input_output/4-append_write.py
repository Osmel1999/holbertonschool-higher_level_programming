#!/usr/bin/python3
"""Module 4-append_write.py.
append text at the end of the file.
"""


def append_write(filename="", text=""):
    """Append text in filename.

    Args:
        - filename: name of the file
        - text: text to append
    Returns: the number of characters added
    """

    with open(filename, 'a+') as f:
        return f.write(text)
