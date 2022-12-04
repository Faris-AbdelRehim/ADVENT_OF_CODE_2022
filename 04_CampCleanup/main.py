#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Advent of Code Coding Calendar
    Day 4 - Camp Cleanup
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

def get_fully_overlapping_assignments(file):
    """
    FUNCTIONS RETURNS NUMBER OF FULLY OVERLAPPING ASSIGNMENTS
    """
    
    # Init pair counter
    overlap_counter = 0
    for line in file:
        
        # Replace newline char
        line = line.replace('\n', '')

        # Split to get each elve
        cleanup_assignments = line.split(',')
        
        # Specify Ranges
        first_range = range(int(cleanup_assignments[0].split('-')[0]),int(cleanup_assignments[0].split('-')[1])+1)
        second_range = range(int(cleanup_assignments[1].split('-')[0]),int(cleanup_assignments[1].split('-')[1])+1)        
        
        
        if set((first_range)).issubset(second_range) or set((second_range)).issubset(first_range):
            overlap_counter += 1    

    return overlap_counter

def get_overlapping_assignments(file):
    """
    FUNCTIONS RETURNS NUMBER OF FULLY OVERLAPPING ASSIGNMENTS
    """
    
    # Init pair counter
    overlap_counter = 0
    for line in file:
        
        # Replace newline char
        line = line.replace('\n', '')

        # Split to get each elve
        cleanup_assignments = line.split(',')
        
        # Specify Ranges (but as list)
        first_range = list(range(int(cleanup_assignments[0].split('-')[0]),int(cleanup_assignments[0].split('-')[1])+1))
        second_range = list(range(int(cleanup_assignments[1].split('-')[0]),int(cleanup_assignments[1].split('-')[1])+1))
        
        if set(first_range)&set(second_range):
            overlap_counter += 1    

    return overlap_counter

if __name__ == "__main__":
    # Specify input filename
    # filename = 'input_example.txt'
    filename = 'input_task.txt'    
    
    # Read File
    file = read_file(filename)
    
    ## Part one
    print('--- PART ONE ---') 
    # Get the number of fully overlapping assignments
    n_fully_overlaps = get_fully_overlapping_assignments(file)
    
    # Output Solution of part one
    print(str(n_fully_overlaps))    
    
    ## Part two
    print('--- PART TWO ---')     
    
    # Get the number of overlapping assignments
    n_overlaps = get_overlapping_assignments(file)    
    
    # Output Solution of part two
    print(str(n_overlaps))   