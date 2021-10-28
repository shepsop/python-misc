#rock paper scissors game


import random

while True:
        
    options = ['rock','paper','scissors']

    computer = random.choice(options)

    player = None

    while player not in options:
        player = input('choose rock, paper or scissors  ').lower()

    print('computer has ' + computer)

    print('player has ' + player)

    if computer == player:
        print('It is a tie!')
    elif computer == 'rock':
        if player == 'scissors':
            print('computer has ' + computer)
            print('player has ' + player)
            print('computer wins')
        if player == 'paper':
            print('computer has ' + computer)
            print('player has ' + player)
            print('player  wins')
    elif computer == 'paper':
        if player == 'scissors':
            print('computer has ' + computer)
            print('player has ' + player)
            print('player wins')
        if player == 'rock':
            print('computer has ' + computer)
            print('player has ' + player)
            print('computer  wins')
    elif computer == 'scissors':
        if player == 'paper':
            print('computer has ' + computer)
            print('player has ' + player)
            print('player wins')
        if player == 'rock':
            print('computer has ' + computer)
            print('player has ' + player)
            print('computer  wins')
    play_again = input('do you want to play again?  yes/no ').lower()

    if play_again != 'yes':
        break

print('thanks for playing!')
           