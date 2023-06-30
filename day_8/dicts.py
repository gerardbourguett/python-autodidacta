# Create an empty dictionary called dog
dog = dict()

# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'Dog',
    'color': '#FFFFFF',
    'breed': 'German Shepherd',
    'legs': 'Long',
    'age': 6
}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary  # noqa: E501
student = {
    'first_name': 'Joe',
    'last_name': 'Doe',
    'gender': 'Female',
    'age': 32,
    'marital_status': 'Married',
    'skills': ["Python", "Java", "Javascript", "PHP"],
    'country': 'United States',
    'city': 'New York',
    'address': {
        'street': 'George Street',
        'zipcode': '02210'
    }
}
# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
skills = list(student.get('skills'))
print(skills)
print(type(skills))

# Modify the skills values by adding one or two skills
student['skills'].append("HTML")
student['skills'].append("CSS")
print(student.get('skills'))

# Get the dictionary keys as a list
keys = student.keys()
print(keys)

# Get the dictionary values as a list
values = student.values()
print(values)

# Change the dictionary to a list of tuples using items() method
tuples = dog.items()
print(tuples)
print(type(tuples))

# Delete one of the items in the dictionary
del dog['legs']
print(dog)

# Delete one of the dictionaries
# copiando
dog_copy = dog.copy()
del dog