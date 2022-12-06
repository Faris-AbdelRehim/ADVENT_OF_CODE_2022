#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Advent of Code Coding Calendar
    Day 6 - Tuning Trouble
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

def get_start_marker(file, N):
    """
    FUNCTION RETURNS A SCALAR (start-of-packet marker)
    """
    
    recent_chars = []
    packet_marker_found = False
    packet_marker = 0
    
    while not packet_marker_found and packet_marker < len(file[0]):    
        # Get next char
        recent_chars.append(file[0][packet_marker])
        
        if len(recent_chars) > N:  
            # Remove first char
            recent_chars.pop(0)

            # Check, if recent_chars contains N unique elements
            if len(set(recent_chars)) == N:
                packet_marker_found = True
        else:
            # There were not yet 4 characters sent
            pass
        
        packet_marker += 1
        
    return packet_marker

if __name__ == "__main__":
    # Specify input filename
    # filename = 'input_example.txt'
    filename = 'input_task.txt'  
    
    # Read File
    file = read_file(filename)
    
    packet_marker = get_start_marker(file, 4)
    
    ## Part one
    print('--- PART ONE ---')     
    
    # Output Solution of part one
    print(packet_marker)    
    
    ## Part two
    print('--- PART TWO ---')       
    
    packet_marker = get_start_marker(file, 14)
    
    # Output Solution of part two
    print(packet_marker)     