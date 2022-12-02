#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Advent of Code Coding Calendar
    Day <day> - <topic>
"""


def read_file(filename):
    """
    FUNCTION RETURNS CONTENT OF FILE
    """
    
    # Read file
    with open(filename) as f:
        lines = f.readlines()      
    
    # Comments
    return lines

if __name__ == "__main__":
    # Specify input filename
    filename = '<filename>.txt'
    
    # Read File
    file = read_file(filename)
    
    # Output Solution
    print('...')    