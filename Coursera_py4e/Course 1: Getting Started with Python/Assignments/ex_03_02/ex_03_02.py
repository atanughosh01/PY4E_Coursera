'''
3.1 Write a program to prompt the user for hours and rate per hour
using input to compute gross pay. Pay the hourly rate for the hours
up to 40 and 1.5 times the hourly rate for all hours worked above 40
hours. Use 45 hours and a rate of 10.50 per hour to test the program
(the pay should be 498.75). You should use input to read a string and
float() to convert the string to a number. Do not worry about error
checking the user input - assume the user types numbers properly.
'''

# enter inputs (hours, rate per hour)
hrs = input("Enter Hours: ")
rate = input("Enter Rate Per Hour: ")

# error catching
try:
    # convert inputs into floating point values
    h = float(hrs)
    rph = float(rate)

except:
    # printing ERROR message if inputs taken are not numeric
    print("ERROR! Please enter numeric input(s)")
    quit()

# conditional statements to calculate gross pay
if h <= 40.0:
    # calculating regular pay
    gp = h * rph

else:
    # calculating over time pay
    regPay = h * rph
    overTimePay = (h - 40.0) * (rph * 0.5)
    gp = regPay + overTimePay

# displaying the final result
print('Gross Pay:', gp)
