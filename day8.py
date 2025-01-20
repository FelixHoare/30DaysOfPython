dog = {}
dog['name'] = 'Clover'
dog['age'] = 8
dog['colour'] = 'Red'
dog['breed'] = 'Fox Red Labrador'
dog['legs'] = 4

print(dog)

student = {
    'name': 'Felix',
    'last_name': 'Hoare',
    'gender': 'M',
    'age': 22,
    'isMarried': False,
    'skills': ['Python', 'Java', 'C', 'Flutter'],
    'country': 'Scotland',
    'city': 'Edinburgh',
    'address': 'Spottiswoode Road'
}

print(len(student))
print(type(student['skills']))

student['skills'].append('Drumming')
student['skills'].append('Sleeping')
print(student)

print(student.keys())
print(student.values())
studentList = student.items()
print(studentList)

del student['isMarried']
print(student)
del student