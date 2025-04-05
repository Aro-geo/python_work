bicycles = ['trek', 'cannondale', 'redline', 'specialized']

#To access an element in a list, write the name of the list followed by the index of the item
#enclosed in square brackets.
print(bicycles[0].title()) # first element
print(bicycles[1].title()) # second element
print(bicycles[-1].title()) # last element

#Using Individual Values from a List
message = f" My first bicycle was a {bicycles[0].title()}."
print(message)

#Modifying Elements in a List
bicycles[0] = "mountain"
print(bicycles)

#Adding Elements to a List
#1.Appending Elements to the End of a List
bicycles.append("mountain")
print(bicycles)

#2.Inserting Elements into a List
bicycles.insert(0, "mountain")
print(bicycles)

#Removing Elements from a List
#1.Removing an Item Using the del Statement
del bicycles[0]
print(bicycles) # code del remove the first item "mountain" from the list.
#You can remove an item from any position in a list using the del statement if you know its index.
del bicycles[-1]
print(bicycles)
#2.Removing an Item Using the pop() Method
popped_bicycle = bicycles.pop()
print(bicycles)
print(popped_bicycle)
#The pop() method removes the last item in a list, but it lets you work
#with that item after removing it

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
last_owned = bicycles.pop()
print(f"The last bicycle i owned was {last_owned.title()}.")
#we can use the pop() method to print a statement
#about the last bicycle we bought:

#Popping Items from any Position in a List
first_owned = bicycles.pop(0)
print(f"The first bicycle i owned was {first_owned.title()}.")

print(bicycles) 
#Remember that each time you use pop(), the item you work with is no
#longer stored in the list.

#3.Removing an Item by Value
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'mountain']
print(bicycles)
bicycles.remove("mountain")
print(bicycles)

#You can also use the remove() method to work with a value that’s being
#removed from a list.
bicycles = ['trek', 'cannondale', 'redline', 'specialized', 'mountain'] 
print(bicycles)
too_expensive = "mountain"
bicycles.remove(too_expensive)
print(bicycles)
print(f"\n A {too_expensive.title()} bicycle is too expensive for me.")
#The remove() method deletes only the first occurrence of the value you specify