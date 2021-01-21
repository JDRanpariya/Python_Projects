import random
import time


def start():
    intro_text = '''\n   You are in a land full of dragons. In front of you,
     you see two caves. In one cave, the dragon is friendly
     and will share his treasure with you. The other dragon
     is greedy and hungry, and will eat you on sight.'''
    print(intro_text)


def choose_cave():
    cave = ''
    print("Which cave will you go into ( 1 or 2 )")
    cave = int(input())
    return cave


def check_cave(chosen_cave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)
    # print(chosen_cave, friendlyCave)
    if chosen_cave == friendlyCave:
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!')


play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    start()
    cave_num = choose_cave()
    check_cave(cave_num)

    print("Do you want to Play Again? (yes or no) ")
    play_again = input()
