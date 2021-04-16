"""
3.3 Write a program to prompt for a score between 0.0 and 1.0.
If the score is out of range, print an error.
If the score is between 0.0 & 1.0, print a grade using the following table:
Score   Grade
>= 0.9   A
>= 0.8   B
>= 0.7   C
>= 0.6   D
< 0.6    F
If the user enters a value out of range, print a suitable error message and
exit. For the test, enter a score of 0.85.
"""

# Taking score input
s = input('Enter a score between 0.0 & 1.0: ')

# catching ERROR if input is non-numeric
try:
    score = float(s)

except:
    print('ERROR! Please enter numeric value')
    print('Exiting Program....')
    quit()

# checking if input numerical value is within specified range
if score <= 0.0:
    print('ERROR! Input score is out of range')
    print('Exiting Program....')

elif score >= 1.0:
    print('ERROR! Input score is out of range')
    print('Exiting Program....')

else:
    print('Input score is within range')

    # assigning grades for given input score
    if score >= 0.9:
        print('Acquired grade is A')

    elif score >= 0.8:
        print('Acquired grade is B')

    elif score >= 0.7:
        print('Acquired grade is C')

    elif score >= 0.6:
        print('Acquired grade is D')

    elif score < 0.6:
        print('Acquired grade is E')
