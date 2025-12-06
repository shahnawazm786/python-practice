def decorate(function):
    def wrapper(students_data):
        # write your code below this comment
        for student in students:
            scores = student["scores"]
            avg_marks = sum(scores.values()) / len(scores)
            print(f'{student["name"]}: {round(avg_marks, 2)}')
        
        # Call original function to get mean grace marks
        # write your code above this comment
        return function(students_data)
    return wrapper


@decorate
def return_mean_grace(students):
    # write your code below this comment
    mean_grace = sum(s["grace_marks"] for s in students) / len(students)
    
    # Return rounded to 2 decimals
    return round(mean_grace, 2)

# Sample Test
students = [
    {"name": "Alice", "scores": {"math": 88, "science": 90, "english": 85}, "grace_marks": 10},
    {"name": "Bob", "scores": {"math": 72, "science": 68, "english": 74}, "grace_marks": 11},
    {"name": "Charlie", "scores": {"math": 95, "science": 92, "english": 91}, "grace_marks": 9},
    {"name": "David", "scores": {"math": 60, "science": 75, "english": 70}, "grace_marks": 10},
    {"name": "Eve", "scores": {"math": 82, "science": 78, "english": 88}, "grace_marks": 11}
]

print(return_mean_grace(students))