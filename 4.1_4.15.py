#4.1  Favorite Pizza 

Fav_pizza = ["hawaiian","pepperoni","cheese"]

for pizza in Fav_pizza:
	print(pizza)

print ("\n")

for pizza in Fav_pizza:
	print (f"I really love {pizza.title()} pizza")

print ("I love all of the Pizzas\n")

#4.2
Fav_animal = ["Chicken", "Panguin","duck"]
for animal in Fav_animal:
	print (f"{animal.title()} would make a great pet")

print ("All of the birds mentioned above can't fly!\n")
 
#4.3  1-20
num_20 = list(range(1,21))
for number in num_20:
	print (number)

#4.4 counting to a millon
# Takes too much time and processing powering!
#millon = []
#for number_0 in list(range(0,1000001)):
	#millon.append(number_0)
#print (millon)

#4.5 Won't work without 4.4
#print (max(millon))
#print (min(millon))
#print (sum(millon))

#4.6 odd numbers 
odd_num = []
for i in range(0,21):
	if i%2!=0:
		odd_num.append(i)

print(f"\n{odd_num}")

#4.7 multiple of three (reduced from 30 --> 10)
three = [value * 3 for value in range(0,11)]
print (three)

#4.8 cube number
cube = [value**3 for value in range(0,11)]
print (f"{cube}\n")
 
#4.9 Did it the first time (To smart! lol)

# 4.10 

print (f"The first three elements of the list Three are: {three[:3]}")
print (f"The middle elements of the list are, {three[4:7]}")
print (f"The last three elements of the list are, {three[8:]}\n")

#4.11 copy past pizza 
  
my_friend_pizza = Fav_pizza[:]
Fav_pizza.append("Mushroom")
my_friend_pizza.append("Chicken")

print (Fav_pizza)
print (my_friend_pizza)

#4.12 More loops 
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print (f"\n")

for i in my_foods:
	print (i)

print(f"\n")
for i in friend_foods:
	print (i) 

print (f"\n")

#4.13 Buffet Tuples 
Buffet = ("Chicken curry","radish","Rice","Roti","Kabeb")
for i in Buffet:
	print (i)

print (f"\n")

#Buffet.append("Coke")
Buffet = ("Chicken curry","Som-tum","Rice","Roti","T-ki")
for i in Buffet:
	print (i)

Buffet = ("Chicken curry","Som-tum","Rice","Roti","Noodle Soup")

print ("\nWe have updated our menu:")

for i in Buffet:
	print (f"- {i}")

#4.14 PEP 8 style guide
#4.15 Code review rewite code according to PEP 8 (Done)

input ("\nA very well effort and well planned!")