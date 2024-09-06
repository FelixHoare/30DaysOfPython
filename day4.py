string1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
string2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[:6])

print(company.__contains__('Coding'))
print(company.find('Coding'))
company.replace('Coding', 'Python')
print(company)
company.replace('All', 'Everyone')
print(company)

company = 'Coding For All'
print(company.split(' '))

companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(companies.split(','))

print(company[0])
print(company[-1])
print(company[10])

acr1 = 'P4E'
acr2 = 'C4A'

print(company.index('C'))
print(company.index('F'))
string3 = 'Coding For All People'
print(string3.rfind('l'))

sentence = 'You cannot end a sentence with because because because is a conjunction'

print(sentence.find('because'))
print(sentence.index('because'))

print(sentence.rfind('because'))
print(sentence.rindex('because'))

print(sentence[31:54])

print(company.startswith('Coding'))
print(company.endswith('Coding'))

trailing = '   Coding   '
print(trailing.strip())

print('thirty_days_of_python'.isidentifier())

list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list1))

print('I am enjoying this challnge.\nI jsut wonder what is next.')

print('Name\tAge\t\tCountry\t\tCity\nFelix\t22\t\tScotland\tEdinburgh')

radius = 10
area = 3.14 * radius**2
print(f'The area of a circule with radius {radius} is {area} meters square')
print('The area of a circile with radius %d is %.1f meters square' % (radius, area))

