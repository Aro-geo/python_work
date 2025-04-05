# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# # Check for inquality
# requested = 'audi'
# if requested != 'subaru':
#     print(f"{requested.title()} is not in the list.")

#     #numeric comparisons
# answer = 18 
# if answer != 42:
#     print("That is not the correct answer.")

#   #Checking Whether a Value Is in a List
# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")  
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")

 #Checking Whether a Value Is Not in a List 
# banned_users = ['andrew', 'carolina', 'david']  
# user = 'marie'
# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")

# #if-else Statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

 #Using if-elif-else Chains
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 15
print(f"Your admission cost is ${price}.")
