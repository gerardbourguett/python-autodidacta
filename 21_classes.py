### Classes ###

class PersonEmpty:
    pass

print(PersonEmpty) # <class '__main__.Person'>
print(PersonEmpty()) # <__main__.PersonEmpty object at 0x000001C7693B7F90>    

class MyClass:
    pass

p = MyClass() #
print(p) # <__main__.MyClass object at 0x00000193DEFB6ED0>

# Class constructor

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = f"{name} {surname}"

person = Person("Gerard", "Bourguett")
print(person.name) # Gerard
print(f"{person.full_name}") # Gerard Bourguett

class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'  # noqa: E501

p = Person('Gerard', 'Bourguett', 30, 'Chile', "Valdivia")
print(p.person_info()) # Gerard Bourguett is 30 years old. He lives in Valdivia, Chile      # noqa: E501

# p1 = Person()
# print(p1.person_info()) # TypeError: Person.__init__() missing 5 required positional arguments: 'firstname', 'lastname', 'age', 'country', and 'city'   # noqa: E501
p2 = Person('John', 'Doe', 30, 'Chile', "Valdivia")
print(p2.person_info()) # John Doe is 30 years old. He lives in Valdivia, Chile

class Person:
    def __init__(self, firstname='Gerard', lastname='Bourguett', age=30, country='Chile', city='Valdivia'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'
    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()
print(p1.person_info()) # Gerard Bourguett is 30 years old. He lives in Valdivia, Chile    
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info()) # John Doe is 30 years old. He lives in Noman city, Nomanland      
print(p1.skills) # ['HTML', 'CSS', 'JavaScript']
print(p2.skills) # []
        
# Inheritance

class Student(Person):
    pass

s1 = Student('Juan', 'Martinez', 35, 'Chile', 'Graneros')
s2 = Student('Camilo', 'Perez', 34, 'Chile', 'Puente Alto')
print(s1.person_info()) # Juan Martinez is 35 years old. He lives in Graneros, Chile       
s1.add_skill('Javascript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills) # ['Javascript', 'React', 'Python']

print(s2.person_info()) # Camilo Perez is 34 years old. He lives in Puente Alto, Chile     
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills) # ['Organizing', 'Marketing', 'Digital Marketing']

# Overriding parent method

class Student(Person):
        def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):  # noqa: E501
            self.gender = gender
            super().__init__(firstname, lastname, age, country, city)
        def person_info(self):
            gender = 'He' if self.gender == 'male' else 'She'
            return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'  # noqa: E501

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info()) # Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.     
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills) # ['JavaScript', 'React', 'Python']

print(s2.person_info()) # Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland. 
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills) # ['Organizing', 'Marketing', 'Digital Marketing']
