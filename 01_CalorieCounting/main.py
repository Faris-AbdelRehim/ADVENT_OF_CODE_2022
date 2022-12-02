#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Advent of Code Coding Calendar
    Day 1 - Calorie Counting
"""


def get_calories_per_elve(filename):
    """
    FUNCTION RETURNS LIST OF CALORIES CARRIED (SUM) BY EACH ELVE 
    """
    
    # Read calorie_list file
    with open(filename) as f:
        lines = f.readlines()  

    # Create empty list to assign sum of calories per elve
    calories_per_elve = []
    
    # Init current_calories (to sum up calories per elve)
    current_calories_sum = 0
    
    # Iterate over over calorie_list
    for line in lines:
        
        # Current line is not empty (add to current_calories_sum)
        if line != "\n" :
            current_calories_sum += int(line)
        
        # Current line is empty (append sum of calories to current elve and reset current_calories_sum)
        else:
            # Add calories to each elve
            calories_per_elve.append(current_calories_sum)
            
            # Reset the sum 
            current_calories_sum = 0    
    
    # Return the calories carried by each elve as list
    return calories_per_elve

def get_max_calories_and_elve(calories_per_elve):   
    """
    FUNCTION RETURNS MAX CALORIES AND THE ELVE WHO CARRIES IT
    """
    
    return max(calories_per_elve), calories_per_elve.index(max(calories_per_elve))

def get_top_three_calories(calories_per_elve): 
    """
    FUNCTION RETURNS THE SUM OF THE TOP THREE CALORIES 
    """    
    
    return sum(sorted(calories_per_elve)[-3:])
    
if __name__ == "__main__":
    # Specify calorie_list filename
    filename = 'calorie_list_task.txt'
    
    # Get calories_per_elve
    calories_per_elve = get_calories_per_elve(filename)
    
    # Get elve who carries most calories and how many calories 
    max_calories, elve_with_max_calories = get_max_calories_and_elve(calories_per_elve)
    
    # Output elve who carries most calories and how many he/she carries
    print('Elve ' + str(elve_with_max_calories) + ' carries ' + str(max_calories) + ' calories!')
    
    # Get top three calories in total
    top_three_calories_total = get_top_three_calories(calories_per_elve)
    
    # Output the top three calories in total
    print('Top three total:' + str(top_three_calories_total) + ' calories!')    