empty = tuple()
sisters = ('Poppy', 'Briony', 'Sorrel')
brothers = ('Dan', 'Harry')
siblings = sisters + brothers
print(sisters)
print(brothers)
print(siblings)

nSiblings = len(siblings)
print(nSiblings)

parents = ('Liz', 'Toddy')
family_members = parents + siblings
print(parents)
print(family_members)


unpackedSiblings = family_members[2:]
print(unpackedSiblings)
unpackedParents = family_members[:2]
print(unpackedParents)

fruits = ('mango', 'pineapple', 'kiwi')
vegetables = ('broccoli', 'peas', 'spinach')
animal_products = ('beef', 'chicken', 'bacon')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

print(len(food_stuff_lt))
print(food_stuff_tp[4:5])
print(food_stuff_lt[4:5])

print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print(nordic_countries)
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)