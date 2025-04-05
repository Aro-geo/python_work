# players = ['john', 'mike', 'sam','peter', 'larry']
# print(players[0:3])

# #Looping Through a Slice
# print("The first three items in the list are:")
# for player in players[:3]:
#     print(player.title())

#Copying a List
my_books = ['book1', 'book2', 'book3']
friend_books = my_books[:]
print(friend_books)
friend_books.append('book4')

print("My favorite books are:")
print(my_books)

print("My friend's favorite books are:")
print(friend_books)