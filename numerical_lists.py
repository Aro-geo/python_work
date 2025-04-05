#Using the range() Function
for value in range(1, 5):
    print(value) # range(5) would return the numbersfrom 0 through 4.

#Using range() to Make a List of Numbers
numbers = list(range(1, 6)) # range(1, 6) would return the numbers from 1 through 5.
print(numbers) 
#Using range() to Make a List of Even Numbers
even_numbers = list(range(2, 11, 2)) # range(2, 11, 2) would return the even numbers from 2 to 10.
print(even_numbers)
squares = [] # Creating an empty list to store squares
for value in range(1, 11): # Looping through numbers 1 to 10
    square = value ** 2 # Squaring each number
    squares.append(square) # Appending the square to the list
print(squares) # Printing the list of squares

#simple statistics
#Minimum and Maximum Values
numbers = [1, 2, 3, 4, 5]
print(min(numbers)) 
print(max(numbers)) 
sum_numbers = sum(numbers) # Sum of all numbers in the list
print(sum_numbers)
