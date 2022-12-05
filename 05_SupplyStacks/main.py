#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Advent of Code Coding Calendar
    Day 5 - Supply Snacks
"""

class Done(Exception): pass
    
def read_file(filename):
    """
    FUNCTION RETURNS CONTENT OF FILE
    """
    
    # Read file
    with open(filename) as f:
        lines = f.readlines()      
    
    # Comments
    return lines

def get_init_status(file):
    
    ## Get number of stacks
    stack_ids = 0
    for line in file:
        try:
            if line[1] == '1':
                stack_ids = [int(s) for s in line.split() if s.isdigit()]
        except:
            pass
    
    n_stacks = len(stack_ids)
    stacks = [[] for i in range(0, n_stacks)] 
    rearrangements = []
    
    ## Get Initial status of stacks
    # Status of loop (if 1, add to stacks)
    get_stacks = 1
    for line in file:
        
        line = line.replace('\n','')
        
        if line == '':
            # Stop, if line is empty
            get_stacks = 0

        else:
            if get_stacks == 1:
                if line[1] != '1':
                    for iStack in range(1,n_stacks+1):
                        idx = 1+(iStack-1)*4
                        stacks[iStack-1].append(line[idx])
            else:
                # Get Arrangements
                rearrangements.append(line)
    
    return stacks, stack_ids, rearrangements


def move_create(source, destination, stacks):
    crate_to_move = ' '
    
    try:
        for idx, crate in enumerate(stacks[source-1]):
            if crate != ' ':
                crate_to_move = crate
                stacks[source-1][idx] = ' '
                raise Done
    except Done:
        pass
    
    try:
        for idx, crate in enumerate(stacks[destination-1]):      
            if idx < len(stacks[destination-1])-1:
                if stacks[destination-1][idx] != ' ':   
                    stacks[destination-1].insert(0, crate_to_move)
                    raise Done
                else:
                    if stacks[destination-1][idx+1] != ' ':
                        stacks[destination-1][idx] = crate_to_move
                        raise Done
            else:
                stacks[destination-1][idx] = crate_to_move
                raise Done

    except Done:
        pass
    return stacks

def perform_arrangements_single(stacks_init, rearrangements):
    stacks = stacks_init
    for rearrangement in rearrangements:
        # Parse rearrangement line
        number_of_crates_to_move = [int(s) for s in rearrangement.split() if s.isdigit()][0]
        source = [int(s) for s in rearrangement.split() if s.isdigit()][1]
        destination = [int(s) for s in rearrangement.split() if s.isdigit()][2]
        
        for i in range(0,number_of_crates_to_move):
            stacks = move_create(source, destination, stacks) 
    return stacks

def move_crates(source, destination, number_of_crates_to_move, stacks):
    crates_to_move = []
    
    crate_counter = 0
    for idx, crate in enumerate(stacks[source-1]):
        if crate_counter < number_of_crates_to_move:
            if crate == ' ':
                #stacks[source-1].pop(idx)
                pass
            else:
                stacks[source-1][idx] = ' '
                crates_to_move.append(crate)
                crate_counter += 1
                

    if crates_to_move != []:
        try:
            for idx, crate in enumerate(stacks[destination-1]):   
                if len(stacks[destination-1])!= 1:   
                    if idx < len(stacks[destination-1])-1:
                        if stacks[destination-1][idx] != ' ':  
                            stacks[destination-1] = crates_to_move + stacks[destination-1]
                            raise Done
                        else:
                            if stacks[destination-1][idx+1] != ' ':
                                stacks[destination-1] = crates_to_move + stacks[destination-1][idx+1:]
                                raise Done
                    else:
                        stacks[destination-1] = crates_to_move
                        raise Done
                else:   
                    stacks[destination-1] = crates_to_move + stacks[destination-1][idx:]
                

        except Done:
            pass
        
    return stacks

def perform_arrangements_multiple(stacks_init, rearrangements):
    stacks = stacks_init
    
    for rearrangement in rearrangements:
        # Count stack vals
        sum = 0
        for stack in stacks:
            for crate in stack:
                if crate != ' ':
                    sum += 1
        
        # Parse rearrangement line
        number_of_crates_to_move = [int(s) for s in rearrangement.split() if s.isdigit()][0]
        source = [int(s) for s in rearrangement.split() if s.isdigit()][1]
        destination = [int(s) for s in rearrangement.split() if s.isdigit()][2]
        
        stacks = move_crates(source, destination, number_of_crates_to_move, stacks)
    return stacks

def get_top_creates(stacks):
    top_crates = []
    for stack in stacks:
        try:
            for crate in stack:
                if crate != ' ':
                    top_crates.append(crate)
                    raise Done

        except Done:
            pass
        
    return ''.join(top_crates)

if __name__ == "__main__":
    # Specify input filename
    # filename = 'input_example.txt'
    filename = 'input_task.txt'
    
    # Read File
    file = read_file(filename)

    ## Part one
    print('--- PART ONE ---') 
        
    # Get init status of stacks
    stacks_init, stack_ids, rearrangements = get_init_status(file)
    
    # Get list of rearrangements commands
    stacks_final = perform_arrangements_single(stacks_init, rearrangements)
    
    # Get each top crate
    top_crates = get_top_creates(stacks_final)
    
    
    # Output Solution of part one
    print(top_crates)    
    
    ## Part two
    print('--- PART TWO ---')       
    
    # Get init status of stacks
    stacks_init, stack_ids, rearrangements = get_init_status(file)

    # Get list of rearrangements commands
    stacks_final = perform_arrangements_multiple(stacks_init, rearrangements)
    
    # Get each top crate
    top_crates = get_top_creates(stacks_final)    
    
    # Output Solution of part two
    print(top_crates)     