'''
Create a text file called “hello.txt” and add the following text inside of it:
Python
Java
Javascript
C/C++/C#
PHP
Node.js
Write a short program to read and display the text file
'''
def read(filename):
    with open(filename,'r') as f:
        return f.readlines()


print(read('hello.txt'))

def append(filename,data):
     with open(filename, 'a') as f:
         for line in data:
             f.write(line+'\n')

append('hello.txt',['Go', 'Kotlin', 'Swift'])

print(read('hello.txt'))

def every_other_line(filename,data):
    with open(filename,'r') as f:
        for line in data[::2]:
            print(line)

every_other_line('hello.txt',read('hello.txt'))


alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def generate_sentence(letter):
    pozitie=alfabet.index(letter)+1
    if pozitie in [1,21]:
        terminatie='st'
    elif pozitie in [2,22]:
        terminatie='nd'
    elif pozitie in [3,23]:
        terminatie='rd'
    else:
        terminatie='th'
    return f'My name is letter {letter}.\nI am the {pozitie}{terminatie} letter of the alphabet.\n'

for letter in alfabet:
    filename = f'{letter}.txt'
    sentence = generate_sentence(letter)
    with open(filename, 'w') as file:
        file.write(sentence)
