import numpy as np

def calculate_mean_age(birds, age):
    '''
    INPUT: birds, age -> 1D array
    OUTPUT: mean_age -> float variable
    '''
    
    birds = np.array(birds)
    age = np.array(age)
    
    ## STEP1. Create mask to get Crane birds from birds array
    mask = birds == 'Cranes'
    
    ## STEP2. Get the age of crane birds
    crane_ages = age[mask]
    
    ## STEP 3. Calculate mean age of crane birds
    mean_age = np.mean(crane_ages)
    
    ## STEP 4. Round off the mean age to 2 decimal points
    mean_age = np.round(mean_age, 2)
    
    return mean_age

birds = ['spoonbills',  'plovers',  'plovers',  'plovers',  'plovers',  'Cranes',  'plovers',  'plovers',  'Cranes',  'spoonbills']
age = [5.5, 6.0, 3.5, 1.5, 3.0, 4.0, 3.5, 2.0, 5.5, 6.0]

print(calculate_mean_age(birds, age))