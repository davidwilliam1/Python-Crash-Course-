#try it 7.1

car = input("what brand car are you looking for? : ")
print ("okay looking for "+ car)

#try it yourself 7.2

resturent = int(input("how many poeple want to eat? :"))
if resturent <= 8:
	print ("your seats are ready!")
else:
	print ("please wait a momment!")

#try it yourself 7.3

multiple_10 = int(input("type a number! :"))
if multiple_10 % 10 == 0:
	print ("the number is a multiple of 10")
else:
	print ("the number is not a multiple of 10")

#try it yourself 7.4

pizza = "please enter the toppings you want on your pizza :"
pizza += "type 'quit to exit'"
active = True 
while active:
	message = input(pizza)
	if message == 'quit':
		break
	else:
		print (f"adding {message} to your pizza\n")

#try it yourself 7.5 

prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    age = int(age)

    if age < 3:
        print("	 You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

    break

#7.6-7 pice of tihs!

#tyr it yourself 7.8
print ("")

sandwich_orders = ["chicken", "tuna", "fried"]
finished_sandwich = []

while sandwich_orders:
	orders = sandwich_orders.pop()
	print (f"making you a {orders.title()} sandwich")
	finished_sandwich.append(orders)

print("")
print (":okay finished making your sandwich orders...\n")

for sandwich in finished_sandwich:
	print (f":Here is your {sandwich} orders!")

#try it yourself 7.9 

sandwich_orders = ["chicken", "tuna", "fried", "pastrami", 
	"pastrami",
	"pastrami" ] 

finished_sandwiches = []

print ("Sorry, The delicatessen has ran-out of pastrami. ")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove("pastrami")

while sandwich_orders:
	orders = sandwich_orders.pop()
	print (f"making you a {orders.title()} sandwich")
	finished_sandwiches.append(orders)

print("")
print (":okay finished making your sandwich orders...\n")

for sandwich in finished_sandwiches:
	print (f":Here is your {sandwich} orders!")

#try it yourself 7.10

vacation = {}

poll_active = True

while poll_active:
	name = input("What is your name?: ")
	vacations = input("If you could vist one place in the world, what would it be? :")
	
	vacation[name] = vacations

	repeat = input ("Do you want to continue? (yes/no)")
	if repeat == 'no':
		 poll_active = False

print ("\n----poll-results----\n")
for name, vacation in vacation.items():
	print (f"{name.title()}'s favorite place is {vacation}")

input()

