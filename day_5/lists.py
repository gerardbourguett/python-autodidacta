# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
items_list = [1,2,3,4,5]

# Find the length of your list
print("3: %d items" % len(items_list))

# Get the first item, the middle item and the last item of the list
middle_items = len(items_list) // 2
print("4: {}, {}, {}".format(items_list[0], items_list[middle_items], items_list[-1]))

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)  # noqa: E501
mixed_data_types = ["Gerard", 1.65, "alone :(", "Falsa 123"]

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.  # noqa: E501
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print("5: %d companies in list" % len(it_companies))

# Print the first, middle and last company
middle_company = len(it_companies) // 2
print(f"6: Primera: {it_companies[0]} Medios: {it_companies[middle_company]} Finale: {it_companies[-1]}")

# Print the list after modifying one of the companies
it_companies[2] = "Netflix"
print("7: ",it_companies)

# Add an IT company to it_companies
it_companies.append("Microsoft")
print("8: ",it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(middle_company, "A company")
print("9: ", it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
upperC = it_companies[3].upper()
it_companies[3] = upperC
print("10: ",it_companies)

# Join the it_companies with a string '#;  '
result = " ".join(["#" + company for company in it_companies])
print("11: ", result)

# Check if a certain company exists in the it_companies list.
print("12: ", it_companies.index("Google"))

# Sort the list using sort() method
it_companies.sort()
print("13: ", it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print("14: ", it_companies)

# Slice out the first 3 companies from the list
print(f"15: {it_companies[0]} {it_companies[1]} {it_companies[2]}")

# Slice out the last 3 companies from the list
print(f"16: {it_companies[-1]} {it_companies[-2]} {it_companies[-3]}")

# Slice out the middle IT company or companies from the list
middle_company = len(it_companies) // 2
print(f"16: {it_companies[middle_company]}")

# Remove the first IT company from the list
it_companies.remove("A COMPANY")
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(middle_company)
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()

# Destroy the IT companies list
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.  # noqa: E501
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print(full_stack)

