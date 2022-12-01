def get_calories_per_elve(filename):
    """
    FUNCTION RETURNS LIST OF CALORIES CARRIED BY EACH ELVE
    """
    # Read calorie_list file
    with open(filename) as f:
        lines = f.readlines()  

    # Create empty list -> calories_per_elve
    calories_per_elve = []
    
    # Init current_calories (to sum up calories per elve)
    current_calories_sum = 0
    
    # Iterate over over calorie_list -> iLine
    for line in lines:
        
        # Get current line and save as calories
        current_calories = line 
        
        # Current line is not empty (add to current_calories_sum)
        if current_calories != "\n" :
            current_calories_sum += int(current_calories)
        
        # Current line is not empty (add to current_calories_sum)
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
    FUNCTION RETURNS TOP THREE CALORIES IN TOTAL
    """    
    
    # Store complete calories list  
    temp_list_calories = calories_per_elve
    
    # Init top three calorie values list
    top_three_calories_total_list = []
    
    # Init current maximum 
    current_maximum = 0

    while len(top_three_calories_total_list) <3:
        
        # Get current maximum in list
        current_maximum = max(temp_list_calories)
        
        top_three_calories_total_list.append(current_maximum)
        
        # Get number of occurrences of maximum in list (in case there are more than one)
        n_occurrences = temp_list_calories.count(current_maximum)
        
        for iOccurrences in range(0,n_occurrences-1):
            # Append maximum for number of occurrences
            top_three_calories_total_list.append(current_maximum)               
        
        # Remove current maximum from list  
        temp_list_calories.remove(current_maximum)
        
        # Does top_three_calories_total_list containt 3 or more values? If yes, cut the remaining elements
        if len(top_three_calories_total_list) >= 3:
            top_three_calories_total_list = top_three_calories_total_list[0:3]

    return sum(top_three_calories_total_list)
    
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