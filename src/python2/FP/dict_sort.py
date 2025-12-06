students = [
{"name": "A", "marks": 50},
{"name": "B", "marks": 100},
{"name": "C", "marks": 40},
{"name": "D", "marks": 70},
{"name": "E", "marks": 60},
]
sort_data= sorted(students, key = lambda x:x['name'], reverse=True)
print(sort_data)