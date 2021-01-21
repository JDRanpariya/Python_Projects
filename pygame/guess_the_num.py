import random

name = input('Enter your Name: ')
print(f"\nWelcome, {name} I've selected number between 1 and 20\n")
print("Let's see if you can guess it right\n")

num = random.randint(1, 20)

guess_count = 0

for i in range(1, 100):
    guess_count += 1
    guessed_num = int(input('\nguess the number: '))
    if guessed_num == num:
        print(f"congo! You guessed it right after {guess_count} times!\n")
        break
    elif guessed_num < num:
        print("You guessed lower than what I have selected\n")
    elif guessed_num > num:
        print("You have guessed higher than what I have selected\n")
