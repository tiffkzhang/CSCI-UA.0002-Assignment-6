import random
import string

def add_letters(word, integer):
    encoded_word = ''
    for char in word:
        encoded_word = encoded_word + char
        for i in range(integer):
            encoded_word = encoded_word + random.choice(string.ascii_letters)
    
    return(encoded_word)


def remove_letters(word, integer):
    unscrambled = ''
    for i in range(0, len(word), integer + 1):
        unscrambled = unscrambled + word[i]
    
    return(unscrambled)

def shift_characters(word, integer):
    shifted_word = ''
    for char in word:
        shifted_word += chr((ord(char) + integer)%256)
    
    return(shifted_word)

def main():

    while True:
        
        choice = input('(e)ncode, (d)ecode or (q)uit: ')
        if choice == 'q':
            break

        number = int(input('Enter a number between 1 and 5: '))
        while number > 5 or number < 1:
             number = int(input('Enter a number between 1 and 5: '))
        
        if choice == 'e':
            phrase = input('Enter a phrase to encode: ')
            new_phrase = shift_characters(add_letters(phrase, number), number)
            print('Your encoded word is:', new_phrase)
       
        elif choice == 'd':
            phrase = input('Enter a phrase to decode: ')
            new_phrase = shift_characters(remove_letters(phrase, number), - number)
            print('Your decoded word is:', new_phrase)
        

main()