# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)

it_companies.update(['Sony', 'HP', 'Crowdstrike'])
print(it_companies)
it_companies.remove('Facebook')
print(it_companies)
it_companies.discard('Facebook')
print(it_companies)

# remove will remove the item, but will throw an error if the item is not present in the set when attempting to remove it
# dicard will remove the item, and will not throw an error if it is not present

C = A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(B.isdisjoint(A))

print(A.symmetric_difference(B))
print(B.symmetric_difference(A))

print(A)
A.update(B)
print(A)
B.update(A)


ages = set(age)
print(ages)
print(len(ages))
print(age)
print(len(age))

# a list is an ordered, changable array of multiple data types
# a string is a single sequence of characters, and is also immutable
# a tuple is an ordered, immutable sequence of objects
# a set is an unordered, mutable sequence of objects

sentence = 'I am a teacher and I love to inspire and teach people'
unique = set(sentence.split())
print(unique)
print(len(unique))