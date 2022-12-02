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

def calc_points_1(file):
    """
    A,X - ROCK
    B,Y - PAPER
    C,Z - SCISSORS        
    
    A > Z (Rock defeats Scissors)
    C > Y (Scissors defeats Paper)
    B > X (Paper defeats Rock)    
    
    """
    
    points_sum = 0
    
    for line in file:
        
        ## Points for symbol 
        if line [2] =='X':
            points_sum += 1
        elif line [2] =='Y':
            points_sum += 2
        elif line [2] =='Z':
            points_sum += 3
        else:
            # Undefined symbol
            pass

        ## Points for win/draw/loss

        if line [0] =='A' and line [2] =='Z':
            # A > Z (Rock defeats Scissors)
            # Lost
            points_sum += 0
            
        elif line [0] =='C' and line [2] =='Y':
            # C > Y (Scissors defeats Paper)             
            # Lost
            points_sum += 0               
        
        elif line [0] =='B' and line [2] =='X':
            # B > X (Paper defeats Rock)
            # Lost
            points_sum += 0              
            
        elif line [2] =='X' and line [0] =='C':
            # X > C (Rock defeats Scissors)            
            # Won
            points_sum += 6
            
        elif line [2] =='Z' and line [0] =='B':
            # C > Y (Scissors defeats Paper)
            # Won
            points_sum += 6            
        
        elif line [2] =='Y' and line [0] =='A':
            # Y > A (Paper defeats Rock)               
            # Won
            points_sum += 6     
            
        else:
            # Draw
            points_sum += 3                                    
        
        #print(points_sum)
        
    return points_sum

def calc_points_2(file):
    """
    A,X - ROCK
    B,Y - PAPER
    C,Z - SCISSORS        
    
    A > Z (Rock defeats Scissors)
    B > X (Paper defeats Rock)        
    C > Y (Scissors defeats Paper)

    
    """
    
    points_sum = 0
    
    for line in file:
        
        ## Points for win/draw/lose 
        if line [2] =='X':
            # lose
            points_sum += 0
            
            if line [0] =='A':
                # Chose Scissors
                points_sum += 3
            elif line [0] =='B':
                # Chose Rock
                points_sum += 1                
            elif line [0] =='C':   
                # Chose Paper
                points_sum += 2                
            else:
                pass             

        elif line [2] =='Y':
            # draw
            points_sum += 3
            # lose
            points_sum += 0
            
            if line [0] =='A':
                # Chose Rock
                points_sum += 1
            elif line [0] =='B':
                # Chose Paper
                points_sum += 2                
            elif line [0] =='C':   
                # Chose Scissors
                points_sum += 3                
            else:
                pass                  
            
        elif line [2] =='Z':
            # win
            points_sum += 6
            
            if line [0] =='A':
                # Chose Paper
                points_sum += 2
            elif line [0] =='B':
                # Chose Scissors
                points_sum += 3                
            elif line [0] =='C':   
                # Chose Rock
                points_sum += 1                
            else:
                pass              
        else:
            # Undefined
            pass

        ## Points for symbols


        
        #print(points_sum)
        
    return points_sum


if __name__ == "__main__":
    # Specify input filename
    #filename = 'strategy_guide_example.txt'
    filename = 'strategy_guide_task.txt'    
    
    # Func
    file = read_file(filename)
    
    points = calc_points_1(file)
    
    # Output Solution
    print('Part 1 - ' + str(points))     
    
    points = calc_points_2(file)    
    # Output Solution
    print('Part 2 - ' + str(points))    