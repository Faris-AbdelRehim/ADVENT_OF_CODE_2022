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
    filename = 'input_example.txt'
    # filename = 'input_task.txt'  
    
    # Read File
    file = read_file(filename)
    
    ## Part one
    print('--- PART ONE ---')     
    
    # Output Solution of part one
    print('...')    
    
    ## Part two
    print('--- PART TWO ---')       
    
    # Output Solution of part two
    print('...')     