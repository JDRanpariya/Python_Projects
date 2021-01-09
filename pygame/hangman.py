from hangman_pics import pics
import random
from nltk.corpus import words
import nltk
import re

nltk.data.path.append('/home/jdranpariya/projects/python')

secret_words = words.words()
secret_word = secret_words[random.randint(0, len(secret_words)-1)]

print('\n' + '_'*len(secret_word) + '\n' + f'guess {len(secret_word)} long word \
     .. or you will be hanged')

guessed = False
guess_count = 7
guessed_word = '_'*len(secret_word)

while (guess_count >= 0):
    print(pics[7 - guess_count])
    if guess_count == 0:
        print("Better luck next time you are hanged")
        break

    guessed_letter = input('\nguess letter: ')

    if guessed_letter in secret_word and (guessed_letter not in guessed_word):
        indexs_of_letter = re.finditer(guessed_letter, secret_word)
        for index in [index.start() for index in indexs_of_letter]:
            print(index)
            guessed_word = guessed_word[:index] + guessed_letter + guessed_word[index+1:]
        print('\nYou guessed it write')
    elif guessed_letter in secret_word and guessed_letter in guessed_word:
        print('\nyou already guessed it..')
    else:
        guess_count -= 1
        print('\nTry again')

    print(guessed_word)
    if guessed_word == secret_word:
        guessed = True
        print("Congo! You Win")
        break
