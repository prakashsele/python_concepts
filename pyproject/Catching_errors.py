'''

Try except block (Except catching errors)
'''



try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Dont do this again")
except ValueError:
    print("no prob")