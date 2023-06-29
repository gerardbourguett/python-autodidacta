# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.  # noqa: E501
thirty = "Thirty"
days = "Days"
of = "Of"
python = "Python"

print(thirty, days, of, python)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
coding = "Coding"
val_for = "For"
all = "All"

print(f"{coding} {val_for} {all}")

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Print the variable company using print().
print(company)

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.  # noqa: E501
print(company.capitalize()) # Coding for all
print(company.title()) # Coding For All
print(company.swapcase()) # cODING fOR aLL

# Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# Check if Coding For All string contains a word Coding using the method index, find or other methods.  # noqa: E501
print(company.find("Coding")) # 0 = Si se encontró

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "coding"))

# Change Python for Everyone to Python for All using the replace method or other methods.  # noqa: E501
everyone = "Python for All"
print(everyone.replace("Python", "Everyone"))

# Split the string 'Coding For All' using space as the separator (split()) .
company = "Coding For All"
print(company.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.  # noqa: E501
rrss = "Facebook, Google, Microsoft, Apple, Oracle, Amazon"
print(rrss.split(","))

# What is the character at index 0 in the string Coding For All.
print(company[0])

# What is the last index of the string Coding For All.
print(company[-1])

# What character is at index 10 in "Coding For All" string.
print(company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = "Python for Everyone"
acronym = ''.join(word[0] for word in name.split())

print(acronym)

# Create an acronym or an abbreviation for the name 'Coding For All'.
name_two = "Coding for All"
acronym_two = ''.join(word[0] for word in name_two.split())

print(acronym_two)

# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))

# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.#   # noqa: E501
people = "Coding For All People"

print(company.rfind("l"))

