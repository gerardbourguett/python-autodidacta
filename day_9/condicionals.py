#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:  # noqa: E501

# age = int(input('Enter your age): '))

age = int(30)

if age >= 18:  # noqa: F821
    print("You are old enough to drive")
else:
    print(f"You need {18 - age} more years to learn to drive.")  # noqa: F821

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:  # noqa: E501

# my_age = int(input("Enter your age"))
# your_age = int(input("Enter your age"))

my_age, your_age = int(30), int(25)

if my_age > your_age:
    print(f"My age is greater than your age for {my_age - your_age} years")
elif my_age < your_age:
    print(f"Your age is greater than my age for {your_age - my_age} years")
else:
    print("My age and your age are equal")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:  # noqa: E501

one = int(3)
two = int(4)

if one > two:
    print(f"{one} is greater than {two}")
elif one < two:
    print(f"{one} is smaller than {two}")
else:
    print(f"{one} is equal to {two}")

### Exercises: Level 2

# Write a code which gives grade to students according to theirs scores:

note = int(45)

if note >= 90 and note <= 100:
    print("A")
elif note >= 70 and note <= 89:
    print("B")
elif note >= 60 and note <=69:
    print("C")
elif note >= 50 and note <=59:
    print("D")
else:
    print("F")


fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')  # noqa: E501

# inp = str(input("Ingrese o valide una fruta: "))

inp = "Caballito"

if inp in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(inp)
    print(fruits)

# Here we have a person dictionary. Feel free to modify it!

person = {
    'first_name': 'Gerard',
    'last_name': 'Bourguett',
    'age': 30,
    'country': 'Chile',
    'is_married': False,
    'skills': ['Javascript', 'HTML', 'Node', 'Python'],
    'address': {
        'street': 'Calle Falsa 123',
        'zipcode': '02210'
    }
}

#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.  # noqa: E501

if "skills" in person:
    skills = person["skills"]
    middle_skill = len(skills) // 2
    print('Skills: ', skills[middle_skill])
else:
    print("No hay :(")

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.  # noqa: E501

if "skills" in person:
    skills = person["skills"]
    if "Python" in skills:
        print('Si tiene el esquil')
    else:
        print("No hay :(")
else:
    print("Nel")

#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!  # noqa: E501

if "skills" in person:
    skills = person['skills']
    if "javaScript" in skills and "React" in skills and len(skills) == 2:
        print("He is a front end developer")
    elif "Node" in skills and "Python" in skills and "MongoDB" in skills:
        print("He is a backend developer")
    elif "Node" in skills and "React" in skills and "MongoDB" in skills:
        print("He is a full-stack developer")
    else:
        print("Unknown title")
else:
    print("Unknown title")
    

#  * If the person is married and if he lives in Chile, print the information in the following format: Asabeneh Yetayeh lives in Chile. He is married.  # noqa: E501

if person['country'] == "Chile" and person["is_married"] == True:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")  # noqa: E501
else:
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is not married")  # noqa: E501


