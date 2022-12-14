#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Advent of Code Coding Calendar
    Day 2 - Rock Paper Scissors
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

def calc_part_1(file):
    """
    FUNCTION RETURNS THE SCORE OF PART 1
    
    A,Z - Lose against ROCK -> SCISSORS
    B,X - Lose against PAPER -> ROCK
    C,Y - Lose against SCISSORS -> PAPER 
    C,X - Win against SCISSORS -> ROCK
    B,Z - Win against PAPER -> SCISSORS
    A,Y - Win against ROCK -> PAPER
    A,X - Draw against ROCK -> ROCK
    B,Y - Draw against PAPER -> PAPER
    C,Z - Draw against SCISSORS -> SCISSORS 
    """
    
    # Init point sum
    points_sum = 0

    # Each Round
    for line in file:
        
        # Check if round is valid
        if line[0] == 'A' or line[0] == 'B' or line[0] == 'C' \
            and line[2] == 'X' or line[2] == 'Y' or line[2] == 'Z' :   
            # Valid round
            points_sum += {
                # Lose # SCISSORS
                ('A','Z'):0+3,
                # Lose # PAPER                
                ('C','Y'):0+2,
                # Lose # ROCK                
                ('B','X'):0+1,
                # Win # ROCK
                ('C','X'):6+1,
                # Win # SCISSORS                
                ('B','Z'):6+3,
                # Win # PAPER                
                ('A','Y'):6+2,  
                # Draw # ROCK
                ('A','X'):3+1,
                # Draw # PAPER                
                ('B','Y'):3+2,
                # Draw # SCISSORS                
                ('C','Z'):3+3,                                                
                }[line[0],line[2]]
        else:
            # Invalid round
            print("Invalid Round: " + line[0] + ' vs. ' + line[2] + '!')
            pass

    return points_sum

def calc_part_2(file):
    """
    FUNCTION RETURNS THE SCORE OF PART 1    
    
    A,X - Lose against ROCK -> Choose SCISSORS
    B,X - Lose against PAPER -> Choose ROCK
    C,X - Lose against SCISSORS -> Choose PAPER 
    A,Z - Win against ROCK -> Choose PAPER
    B,Z - Win against PAPER -> Choose SCISSORS
    C,Z - Win against SCISSORS -> Choose ROCK
    A,X - Draw against ROCK -> Choose ROCK
    B,Y - Draw against PAPER -> Choose PAPER
    C,Z - Draw against SCISSORS -> Choose SCISSORS          
    """
    
    # Init point sum    
    points_sum = 0

    # Each Round
    for line in file:
        
        # Check if round is valid
        if line[0] == 'A' or line[0] == 'B' or line[0] == 'C' \
            and line[2] == 'X' or line[2] == 'Y' or line[2] == 'Z' :  
            ## Points for win/draw/loss
            points_sum += {
                # Lose # Choose SCISSORS
                ('X','A'):0+3,
                # Lose # Choose ROCK
                ('X','B'):0+1,
                # Lose # Choose PAPER
                ('X','C'):0+2,   
                # Win # Choose PAPER
                ('Z','A'):6+2,
                # Win # Choose SCISSORS
                ('Z','B'):6+3,
                # Win # Choose ROCK
                ('Z','C'):6+1,   
                # Draw # Choose ROCK
                ('Y','A'):3+1,
                # Draw # Choose PAPER
                ('Y','B'):3+2,
                # Draw # Choose SCISSORS
                ('Y','C'):3+3,                                                    
                }[line[2],line[0]]      
        else:
            # Invalid round
            print("Invalid Round: " + line[0] + ' vs. ' + line[2] + '!')
            pass

    return points_sum


if __name__ == "__main__":
    # Specify input filename
    #filename = 'strategy_guide_example.txt'
    filename = 'strategy_guide_task.txt'    
    
    # Func
    file = read_file(filename)
    
    # Get points of first part
    points = calc_part_1(file)
    
    # Output Solution
    print('Part 1 - ' + str(points))     
    
    # Get points of second part    
    points = calc_part_2(file)
        
    # Output Solution
    print('Part 2 - ' + str(points))    
    
    """
    # Part 1 - 11767
    # Part 2 - 13886        
    """