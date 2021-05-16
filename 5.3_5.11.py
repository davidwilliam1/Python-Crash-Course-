#5.1 Conditional tests 
response = ["yes","no",]

print ("Is Yes in response, I think it's not")
print ('Yes' in response)   

# 5.2 
if 'hi' not in response:
	print ("\nTrue, 'hi' is not in response")

if 'Yes' in response:
	print ("True")

if 'Yes'.lower() in response:
	print ("True")

if (2 >= 2):
	print ("2 is equal to 2 :(2>=2)")
if (2 <= 2):
	print ("2 is equal to 2 :(2<=2)")	
if (2<3):
	print ("3 is grater then 2 :(2<3)") 
if (2>3):
	pass
else : 
	print ("2 is less then 3 :(2>3)") 


if (2<=2 and 3>=3) == (2<3 and 3<4): 	
	""" True """
	print ("The statments match")
else : 
	print ("The statments don't match")

if (2>3 or 4<2 ) == (7>5 and 5<9): 
	""" False """
	print ("The statments match")
else :
	print ("The statments don't match")

# Testing whether an item is in the list
alphabets = ["a","b","c"]
if "a" in alphabets:
	print ("Letter 'a' is in alphabets")
else : pass

if 'd' not in alphabets:
	print ("Letter 'd' is not in the alphabets\n")
else : pass


# try it yourself 5.3

alien_color = "green"
if alien_color == "green":
	print ('You have earned 5 points!\n')

alien_color = "green"
if alien_color != "green":
	""" The test is purposefuly made to fail"""
	print ('You have earned 5 points!\n')

# try it yourself 5.4

alien_color = "red"
if alien_color == "green":
	print ('You have earned 5 points!\n')
if alien_color != "green":
	print ("you have earned 10 points!\n")


#try it yourself 5.5
alien_color_1 = "yellow"

if alien_color_1 == "green":
	points = 5
elif alien_color_1 == "yellow":
    points = 10
else:
	points = 15
print (f"you have earned {points} points\n")

#try it yourself 5.6
age = 17

if age < 2:
	human = "baby"
elif age < 4:
	human = "toddler"
elif age < 13:
	human = "kid"
elif age < 20:
	human = "teen"
elif age < 65:
	human = "adult"
else:
	human = "elder"

print (f"The person is {human}\n") 

#try it yourself 5.7

favorite_fruit = ["bananas", "apple", "mango"]

if 'kiwi' in favorite_fruit:
	print ("So you really like banana, huh!")
if 'appler' in favorite_fruit:
	print ("So you really like apples, huh!")
if 'mango' in favorite_fruit:
	print ("So you really like mangos, huh!")
if 'bananas' in favorite_fruit:
	print ("So you really like bananas, huh!\n")

#try it yourself 5.8 

users = ["david", "bob", "kiki", "william","jenny" ,"admin"]

for user in users:
	if user == "admin": 
		print ("Hello admin, would you like see the status report!\n")
	else:
		print (f"hello {user.title()}, how are you?")


#try it yourself 5.9 

usernames = []

if usernames:
	 for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see today?")
        else: 
        	print("Hello {username}, how are you?")
else:
print ("We need to find Users")
#try it yourself 5.10


current_users = ["dad", "mad", "gad", "lad", "bad," "sad"]
new_users = ["dAd", "had" ,"tad", "Gad"]

current_users_lower = [usersl.lower() for usersl in current_users]

for usersl in new_users:
	if usersl.lower() in current_users:
		print ("sorry "+usersl+" this name is taken")

	else:
		print ("nice name ,"+ usersl)


#try it yourself 5.11

numbers = list(range(1,10))

for number in numbers:
	if number == 1:
		print ("\n1st")
	elif number == 2:
		print ("2nd")
	elif number == 3:
		print ("3rd")
	else:
		print (str(number)+"th")




































