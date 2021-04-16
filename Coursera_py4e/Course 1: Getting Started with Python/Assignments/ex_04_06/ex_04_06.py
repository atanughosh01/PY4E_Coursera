'''4.6 Write a program to prompt the user for hours and rate per hour
using input to compute gross pay. Pay should be the normal rate for
hours up to 40 and time-and-a-half for the hourly rate for all hours
worked above 40 hours. Put the logic to do the computation of pay in
a function called computePay() and use the function to do the
computation. The function should return a value. Use 45 hours and a
rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the
string to a number. Do not worry about error checking the user input
unless you want to - you can assume the user types numbers properly.
Do not name your variable sum or use the sum() function.'''


# definition the function
def computepay(x, y):
    return x * y

# taking inputs from user
hrs = input("Enter Hours: ")
rate = input("Enter Rate Per Hours: ")

# catching exception
try:
    # convert inputs into floating point values
    h = float(hrs)
    r = float(rate)
except:
    # printing ERROR message if inputs are non-numeric
    print("ERROR! Please enter numeric value")
    quit()

# conditional statements to calculate gross pay
if h <= 40.0:
    # calculating regular pay
    p = computepay(h, r)
else:
    # calculating over time pay
    regPay = computepay(h, r)
    overTimePay = computepay((h - 40.0), (r * 0.5))
    p = regPay + overTimePay

# displaying the final result
print('Gross Pay:', p)
