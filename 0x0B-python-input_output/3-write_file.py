#!/usr/bin/python3
"""Module 2-read_lines.
Reads a certain number of lines from a file.
"""
def write_file(filename="", text=""):
    """Writes text in filename.

    Args:
      - filename: name of the file
      - text: the text that gonna be added to the file

      Retuns: number of characters written
    """

    with open(filename, 'w+') as f:
        return f.write(text)

