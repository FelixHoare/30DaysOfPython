empty = []

list1 = ['labrador','dachshund','bernese','cavapoo','collie','golden retriever','husky','german shepherd']

print(len(list1))

print(list1[0])
print(list[4])
print(list1[-1])

mixed_data_types = ['Felix',22,189,'Unmarried','Edinburgh']

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[-1])
print(it_companies[3])

it_companies[0] = 'Crowdstrike'
print(it_companies)

it_companies.append('Mojang')
it_companies.insert(3,'Reddit')

it_companies[-1] = it_companies[-1].upper()
print(it_companies)

print('# '.join(it_companies))

print(it_companies.__contains__('Microsoft'))

it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)

print(it_companies[:3])
print(it_companies[-3:])
l = len(it_companies)
print(it_companies[l//2:l//2+1])

print(it_companies)

it_companies.remove('Reddit')
print(it_companies)

it_companies.remove('IBM')
print(it_companies)

it_companies.pop()
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

middle = front_end + back_end
print(middle)

full_stack = middle.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print(ages[0])
print(ages[-1])
ages.insert(0, ages[0])
ages.append(ages[-1])
print(ages)
print(ages[len(ages)//2])
total = 0
for x in ages:
    total += x
print(total)
average = total/len(ages)
print(average)
range = ages[-1]-ages[0]
print(range)
comp1 = abs(ages[0]-average)
print(comp1)
comp2 = abs(average-ages[-1])
print(comp2)


countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

print(len(countries))
print(countries[len(countries)//2])
countries_1 = countries[:len(countries)//2+1]
countries_2 = countries[len(countries)//2+1:]
print(len(countries_1))
print(len(countries_2))

countries_3 = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
one, two, three, *scandic = countries_3
print(one, two, three, scandic)