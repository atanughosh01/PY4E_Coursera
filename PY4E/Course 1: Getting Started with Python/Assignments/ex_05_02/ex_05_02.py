'''5.2 Write a program that repeatedly prompts a user for integer numbers
until the user enters 'done'. Once 'done' is entered, print out the largest
and smallest of the numbers. If the user enters anything other than a valid
number catch it with a try/except and put out an appropriate message and
ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.'''

# assigning NULL value to variables
largest = None
smallest = None
while True:
    # taking input from user
    num = input("Enter a number: ")
    if num == "done":
        break

        # catching exception
    try:
        # convert inputs into floating point values
        fnum = float(num)
    except:
        # printing ERROR message for non-numeric inputs
        print('Invalid input')

    else:
        # This block will execute if no exception is caught
        if smallest is None:  # first number
            smallest = fnum
        elif fnum < smallest:
            smallest = fnum
        elif largest is None:  # first number
            largest = fnum
        elif fnum > largest:
            largest = fnum

print("Maximum is", int(largest))
print("Minimum is", int(smallest))
