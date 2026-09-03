''' Puzzle Game '''

import random

def guessing_word():
    words = ['apple', 'mango', 'banana','orange']

    Choice =  random.choice(words)
    char = list(Choice)

    print(f'First letter: {char[0]} \n Last latter: {char[-1]} \n Total char = {len(Choice)}')

    attempts = 3

    while attempts > 0:
        Fruits_name = input('Enter the fruit name:').lower()

        if Fruits_name == Choice:
            print(' Puzzle completed...Congrets!')
            return

        hint = ''
        for i in range(len(char)):
            if Fruits_name[i] == char[i]:
                hint += Fruits_name[i]
            else:
                hint += '-'
        print("Hint:", hint)
                
        attempts -=1

        if attempts >0 :
            print('Plz try again. ')
        else:
            print("Puzzle not completed. Game Over ! ")





guessing_word()
