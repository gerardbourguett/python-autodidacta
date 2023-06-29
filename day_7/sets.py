# sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
more_it = ("Company 1", "Company 2", "Company 3", "Company 4")
it_companies.update(more_it)
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("Company 4")
print(it_companies)

# What is the difference between remove and discard // Explicado en 06_sets.py


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Join A and B
c = B.union(A)
print(c)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
ab = A.union(B)
ba = B.union(A)
print(ab, ba)

# What is the symmetric difference between A and B
print(A.symmetric_difference(B))

# Delete the sets completely
del A, B, c, age
