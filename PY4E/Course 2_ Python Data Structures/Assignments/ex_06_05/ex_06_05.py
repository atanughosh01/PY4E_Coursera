'''
6.5 Write code using find() and string slicing (see section 6.10)
to extract the number at the end of the line below. Convert the
extracted value to a floating point number and print it out.
'''

# ENTER this string as primary input = X-DSPAM-Confidence: 0.8475

text = input('Enter your string : ')                      # input string goes here
find_str = input('Enter which sub-string to find : ')     # self-explanatory
pos1 = text.find(find_str)                                # starting position of sub-string
pos2 = pos1 + len(find_str)                               # ending position of sub-string

if pos1 >= 0:                                             # if the sub-string is present (doesn't return -1)
    print('The sub-string', find_str, 'is present at position',
          pos1, 'and ending at position', pos2 - 1)
else:                                                     # condition if the sub-string is absent (returns -1)
    print('ERROR! The sub-string is not present in the original string.')
    quit()

new_text = text[pos1:pos2]                                # slicing the string between (int)pos1 & (int)pos2
try:
    num = float(new_text)
except:                                                   # catching exception if the string is not convertible to FLOAT type
    print('The sub-string is NOT convertible to float type')
    quit()

print('The converted float value is =', num)
