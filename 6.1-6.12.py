#try it yoyrself 6.1
person_info = {
	"david" : "love kittens",
	"welder": "loves candy",
	"anndy" : "lover coding",
	}
p = person_info["david"]
print (f"david {p}")

#try it yourself 6.3
Fav_num = {
	"david" : 7,
	"alex"  : 1,
	"welder": 206

	}
v,b,c = Fav_num["david"], Fav_num["alex"], Fav_num["welder"]
print (f"david's favorite number is {v}\n" f"alex's favorite number is {b}\n" f"welder's favorite number is {c}\n")

#try it yoyrself 6.3

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }
op = glossary["string"]
oc = glossary["comment"]
ol = glossary["list"]
ol_1 = glossary["loop"]
od = glossary["dictionary"]



print (f"string: {op}")
print (f"comment: {oc}")
print (f"list: {ol}")
print (f"loop: {ol_1}")
print (f"dictionary: {od}\n")


#try it yourself 6.4
glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }
for key, value in glossary.items():
	print (f"{key}:{value}")

#try it yourself 6.4 

rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }
print("")
for name, country in rivers.items():
	print (f"{name.upper()} is in {country.upper()}")

print("\nThe following rivers are included in this data set:")
 
for name in rivers:
	print (name)	

print("The following countries are included in this data set:")

for country in rivers.values():
	print (country)

print ("")
#try it yourself 6.6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
pep = ["jen", "david", "jeff", "phil"]

for name in pep:
    if name in favorite_languages:
    	print (f"{name}, thank you for taking the poll")
    else:
    	print (f"{name}, please take our poll")\

print ("\n")

#try it yourself 6.7

people = []
person = {
    'first_name': 'eric',
    'last_name': 'matthes',
    'age': 43,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'ever',
    'last_name': 'matthes',
    'age': 5,
    'city': 'sitka',
    }
people.append(person)

person = {
    'first_name': 'willie',
    'last_name': 'matthes',
    'age': 8,
    'city': 'sitka',
    }
people.append(person)

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    print(name + ", of " + city + ", is " + age + " years old.")


#try it yourself 6.8
pets = []
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'KFC',
    'owner': 'yashap',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'bothy',
    'owner': 'david',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))


#try it yourself 6.9

favorite_places = {
    'david': ['london', 'ice land', 'canada'],
    'yashap': ['cage', 'toilet'],
    'william': ['heaven', 'familiy', 'any open space']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + " likes the following places:")
    for place in places:
        print("- " + place.title())

#try it yourself 6.10

favorite_numbers = {
    'dodo': [7, 17],
    'yashapo': [67, 68, 96],
    'willa': [6, 9],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))

#try it yourself 6.11

cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himilaya',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()
    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  The " + mountains + " mountains are nearby.")


input()


#try it yourself 6.12
#why not!!!

























	
	





















