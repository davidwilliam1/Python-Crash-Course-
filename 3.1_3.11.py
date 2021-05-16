#3.1 list and modification

Friends = ["bob","josh","sam","mendla"]
print (f"{Friends[0]}\n{Friends[1]}\n{Friends[2]}\n{Friends[3]}\n")

#3.2 Greetigs 
print (f"You are a good friend, {Friends[0]}\n\
You are a good friend, {Friends[1]}\nYou are a good friend,\
{Friends[2]}\nYou are a good friend, {Friends[3]}\n")

#3.3 Make a list 
fav_transport = ["car", "plane", "bus", "trian"]
print (f"I would like to own a BMW {fav_transport[0]}")

#3.4  Guest list
Guests = ["mile", "alan","bob"]
print (f"I'd like to invite you to dinner, {Guests[0].title()}\nI'd like to invite you to dinner,\
 {Guests[1].title()}\nI'd like to invite you to dinner, {Guests[2].title()}\n")


#3.5 OH NO 
#spent an hour finding solution with this code:
#print (f"{Guests[0].title()} can't make it the party")
#Guests.remove("mile")
#Guests.insert(0,"gates")
#print (f"Instead, I'd like to invite you to dinner, {Guests[0].title()}\nI'd like to invite you to dinner,{Guests[1].title()}\nI'd like to invite you to dinner, {Guests[2].title()}")
# the solution was so simple -(just had to change the name manully)

#3.5 continued 

Guests = ["gates", "alan","bob"]

print (f"I'd like to invite you to dinner, {Guests[0].title()}\n\
I'd like to invite you to dinner,\
{Guests[1].title()}\nI'd like to invite you to dinner, {Guests[2].title()}\
\nSorry {Guests[0].title()}, can't make it to the party!\n")

#3.6 More Guests

print (f"{Guests[0]},we found a bigger table\n{Guests[1]},we found\
a bigger table\n{Guests[2]},we found a bigger table\n")

Guests.insert(0,"pob")
Guests.insert(2,"jell")
Guests.append("mike")

print (f"{Guests[0]}, I'd like to invite you to the party!\n{Guests[1]}, I'd like to invite you to the party!\n{Guests[2]},\
 I'd like to invite you to the party!\n{Guests[3]}, I'd like to invite you to the party!\n{Guests[4]}, I'd like to invite you to the party!\n{Guests[5]},\
  I'd like to invite you to the party!")

#3.7 Shrinking the list
print ("Sorry guys, I will invite only two people")
print (Guests)
pob = Guests.pop(0)
print (f"\n{pob}, Sorry the party is cancelled!")
Gates = Guests.pop(0)
print (f"{Gates}, Sorry the party is cancelled!")
jell = Guests.pop(0)
print (f"{jell}, Sorry the party is cancelled!")
alan = Guests.pop(0)
print (f"{alan}, Sorry the party is cancelled!")

print (f"\n{Guests[0].title()}, You are welcome to the secret party!")
print (f"{Guests[1].title()}, You are welcome to the secret party!")

del Guests[0:2]
print (Guests)

#3.8 Seeing the world (five places)

Places = ["paris","london","madrid","cape town","bangkok"]
print (Places)
print (sorted(Places))
print (Places)

Places.reverse()
print(Places)
Places.reverse()
print(Places)

Places.sort()
print(Places)
Places.sort(reverse=True)

#3.9 Dinner guest lenght/
print (len(Places))

#3.10 Using every function leanred in a code 

countries = ["South Korea", "China","Thailand","Canada","United States"]

print (countries[0])
print (countries[-1].title())

countries[0] = "Russia"
print (countries)

countries.append("Iceland")
print (countries)

countries.insert(0, "greenland")
print (countries)

del countries[2]
print (countries)

pop_method = countries.pop(-1)
print (countries)
print (pop_method)

countries.remove("Russia")
print (countries)

countries.sort()
print (countries)

countries.sort(reverse=True)
print (countries)

print (len(countries))

#3.11 indentaion Error

numbers = [1,2,3,4,5]
#print (numbers[5]) <---
print (numbers[4])

input ("\nThis was well complicated Code!")












