#!/usr/bin/env python3

def ubbi_dubbi(word):
    output = []
    for letter in word:
        if letter in 'aeiou':
            output.append(f'ub{letter}')
        else:
            output.append(letter)
    return ''.join(output)

def add_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text)

filename = "output.txt"
text = "Hola mundo\n"

# Convert the word "python" to Ubbi Dubbi
ubbi_dubbi_word = ubbi_dubbi('python')

# Add the Ubbi Dubbi word to the file
add_to_file(filename, ubbi_dubbi_word)

# Print the Ubbi Dubbi word
print(ubbi_dubbi_word)
