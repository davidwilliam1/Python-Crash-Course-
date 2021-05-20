import modules 

#try it yourself 8.1
def display_message():
	"""what i learned in chap#8"""
	print ("Function are good for warping a block of code!")

display_message()

#try it yourself 8.2

def fav_book(favbook):
	"""prints the favorite book"""
	print (f"So your favorite book is {favbook.title()}")

fav_book("Lice in wonderland")

#try it yourself 8.3

def make_shirt(size, text): 
	"""prints the size and the text on a customizable t-shirt """
	print (f"\nThe size of your t-shirt is {size}\nThe text on the t-shirt will be '{text}'")

make_shirt(43, "i love dogs")

#try it yourself 8.4

def make_shirt(size=50, text='i love python'): 
	print (f"\nThe size of your t-shirt is {size}\nThe text on the t-shirt will be '{text}'")


make_shirt()
make_shirt(size=30, text="i love you")

#try it yourself 8.5 

def describe_city(city, country="finland"):
	print (f"{city.title()} is in {country.title()}")

describe_city("Helsinki")
describe_city("espoo")

#try it yourself 8.6

def city_country(city, country):   
	city_country = (f'"{city}, {country}"')
	return city_country.title()

city = city_country("espoo", "finland")
print (city)

#try it yourself 8.7

def make_album(artist_1, album_1, tracks =None):
	album_dic = {'art_name': artist_1, 'album_name': album_1}
	if tracks:
		album_dic["tracks"] = tracks
	return album_dic 

al_1,al_2,al_3  = make_album("ed shren", "2018 X"), make_album("taylor fast", "idk"), make_album("david", "the loom" , 3)
print (al_1,'\n', al_2,'\n', al_3)

#try it yourself 8.8

def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
    	'artist': artist.title(), 'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "


print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)

print("\nThanks for responding!")


#try it yourself 8.9 

def show_message(messages):
    for message in messages:
        print(message)
        

message = ["hello there", "hi there", "good morning, there", "i love you there"]
show_message(message)


#try it yourself 8.10

def sent_mess(messages, sents):
	while message:
		sent1 =message.pop()
		sent.append(sent1)

message = ["hello there", "hi there", "good morning, there", "i love you there"]
sent = []

print (message)
print (sent)
#after the function takes place
sent_mess(message, sent)
print (message)
print (sent)


#try it yourself 8.11

def sent_mess(messages, sents):
	while message:
		sent1 =message.pop()
		sent.append(sent1)

message = ["hello there", "hi there", "good morning, there", "i love you there"]
sent = []
messages0 = message[:]
sent_mess(messages0, sent)

print (messages0)
print (sent)
print (message)
 
#try it yourself 8.12 
def sandwiches(*toppings):
	print (toppings)

sandwiches("apple", "banana")
sandwiches("egg")
sandwiches("egg", "tomato","leaves")

#try it yourself 8.13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile("joe", "amam", location="nutland ")
print(my_profile)

#try it yourself 8.14
""" 
cars function is used fo 8.15 
def cars(manufacture, model,**features):
	car_info={}
	car_info["manufacture"]=manufacture
	car_info["model.num"]=model
	for key, value in features.items():
		car_info[key]=value
	return car_info

Ford = cars("Ford","focus",tiremodel="A78")
print (Ford) 
"""
# 8.15 

instence = modules.cars("audi","a4")
print (v)

# 8.16 
""" All importing methods have been tested thoroughly

import modules
from modules import cars 
from modules import cars as c
import modules as m
from modules import *

"""
















