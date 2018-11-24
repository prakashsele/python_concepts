

friends = ["Ram", "Jim", "Om", "James", "Ravi"]
friends[1] = "James"  # to change the particular name
print(friends[2:])   # to print after 2nd index
print(friends[2])
print(friends[2:4])   # to print from one index to another index

lucky_numbers = [1, 2, 3, 4, 5, 6, 0, 97, -9]

#  List functions

friends.extend(lucky_numbers)  # to extend any other variables
friends.append("creed")  # to append any other variables after the list
friends.insert(7, "creed")  # to insert any other variables in particular index  list
friends.remove("creed")  # to delete any other variables in particular index  list
# friends.clear()  # to delete everything

print(friends.count("creed"))
# print(friends.index("mike"))

print(friends)


lucky_numbers.sort()
lucky_numbers.reverse()
lucky_numbers.sort()

print(lucky_numbers)

friends2 = friends.copy()
print(friends2)