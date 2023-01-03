import random


def play():
    userMove = input('Rock, Paper or Scissors:\n')
    computerMove = random.choice(['Rock','Paper','Scissors'])

    while computerMove == userMove:
        print('tie')
        userMove = input('Choose again:\nRock, Paper or Scissors:\n')
        computerMove = random.choice(['Rock', 'Paper', 'Scissors'])

    if (computerMove == 'Rock' and userMove == 'Paper') or (computerMove == 'Paper' and userMove == 'Scissors') or (computerMove == 'Scissors' and userMove =='Rock'):
        print (f'You Win!\nYou chose {userMove} and the computer chose {computerMove}')
    elif (computerMove == 'Rock' and userMove == 'Scissors') or (computerMove == 'Paper' and userMove == 'Rock') or (computerMove == 'Scissors' and userMove =='Paper'):
        print(f'You Lose!\nYou chose {userMove} and the computer chose {computerMove}')
    else:
        print ('Please type either "Rock", "Paper", or "Scissors"')


play()