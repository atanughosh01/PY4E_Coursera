""" Use this line of text as input:
Whether you want to find a more fulfilling career, build something you're proud of, or expand your understanding of the world, we are here to help make it happen.
"""
counts = dict()
line = input('Enter a line of text: ')

words = line.split()

print('Words:', words)
print('Counting.....')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Word Counts are:', counts)