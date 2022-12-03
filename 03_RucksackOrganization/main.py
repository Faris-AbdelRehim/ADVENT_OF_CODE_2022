#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Advent of Code Coding Calendar
    Day 3 - Rucksack Organization
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

def get_priority_value(priority):
    """
    FUNCTION RETURNS PRORITY VALUE (BASED ON RULES) TAKES CHAR RETURNS NUMBER
    """
    return {
            ('a'):1,
            ('b'):2,            
            ('c'):3,
            ('d'):4,
            ('e'):5,
            ('f'):6,
            ('g'):7,                        
            ('h'):8,
            ('i'):9, 
            ('j'):10,
            ('k'):11, 
            ('l'):12,
            ('m'):13,   
            ('n'):14,   
            ('o'):15,   
            ('p'):16,   
            ('q'):17,   
            ('r'):18,   
            ('s'):19,  
            ('t'):20,   
            ('u'):21,   
            ('v'):22,   
            ('w'):23,
            ('x'):24,
            ('y'):25,
            ('z'):26, 
            ('A'):27,
            ('B'):28,            
            ('C'):29,
            ('D'):30,
            ('E'):31,
            ('F'):32,
            ('G'):33,                        
            ('H'):34,
            ('I'):35, 
            ('J'):36,
            ('K'):37, 
            ('L'):38,
            ('M'):39,   
            ('N'):40,   
            ('O'):41,   
            ('P'):42,   
            ('Q'):43,   
            ('R'):44,   
            ('S'):45,  
            ('T'):46,   
            ('U'):47,   
            ('V'):48,   
            ('W'):49,
            ('X'):50,
            ('Y'):51,
            ('Z'):52,                                                                           
        }[priority]  

def calc_part_1(file):   
    """
    FUNCTIN RETURNS SUM OF PRIORITIES 
    """
    priorities_sum = 0
    
    for line in file:
        first_half = line[:len(line)//2]
        second_half = line[len(line)//2:]
        
        print(list(set(first_half)&set(second_half)))
        
        priority = list(set(first_half)&set(second_half))[0]
        
        priorities_sum += get_priority_value(priority)     

    return priorities_sum

def calc_part_2(file):  
    """
    FUNCTIN RETURNS SUM GROUP BADGES
    """    
    member_counter = 0
    priorities_sum = 0
    current_items = []
    items_total = []
    for line in file:
        
        current_items.append(line.replace('\n',''))        
        member_counter += 1
                
        if member_counter == 3:
            print(current_items)
            prio_a = set(current_items[0])&set(current_items[1])
            priority = list(prio_a&set(current_items[2]))[0]
            
            # get badge
            items_total.append(priority)
            
            priorities_sum += get_priority_value(priority)  
            
            # Reset member_counter
            member_counter = 0
            
            current_items = []
            
    return priorities_sum
    
if __name__ == "__main__":
    # Specify input filename
    # filename = 'input_example.txt'
    filename = 'input_task_1.txt'    
    
    # Read File
    file = read_file(filename)
    
    ## Part one
    print('--- PART ONE ---') 
    
    # Find same characters in compartments
    rucksack_item_priorities_sum = calc_part_1(file)
    
    # Output Solution   
    print(rucksack_item_priorities_sum)  
    

    ## Part two
    print('--- PART TWO ---')       
    # Find same characters in compartments
    priorities_sum = calc_part_2(file)

    print(priorities_sum)  