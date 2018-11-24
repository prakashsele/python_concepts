
# Python read command

'''
r - read
w - write - overwrite an existing file
a - append - cant modify but can add info
r+ - read and write
'''

emplist = open("data.txt", "r")
# print(emplist.readable())
# print(emplist.read())
# print(emplist.readline())
print(emplist.readlines())  # keeps every thing in an array.

emplist.close()

