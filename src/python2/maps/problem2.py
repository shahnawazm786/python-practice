students=[
            {"name":"Arham","marks":70,"grade":"A"},
            {"name":"Subhan","marks":73,"grade":"A"},
            {"name":"Sanjay","marks":50,"grade":"C"},
            {"name":"Ram","marks":45,"grade":"D"},
            {"name":"Kalam","marks":75,"grade":"A+"},
            {"name":"Salam","marks":80,"grade":"A++"}
]
list_of_grade=map(lambda student:student['grade'],students)
print(list(list_of_grade))
