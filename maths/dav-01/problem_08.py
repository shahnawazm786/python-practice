import numpy as np
def ratio(marks_arr):
    distinction = marks_arr[marks_arr >= 80]        # masking
    first_div = marks_arr[(marks_arr >= 60) & (marks_arr < 80)]  # masking
    
    distinction_count = len(distinction)
    first_div_count = len(first_div)
    
    ratio = distinction_count / first_div_count
    
    return round(ratio, 2)