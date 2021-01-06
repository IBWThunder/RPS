import random
import time
# THIS IS A ROCK PAPER SCISSORS GAME.
print("Winning Rules of the Rock paper scissor game as follows: \n" + "Rock vs paper->paper wins \n" +  "Rock vs scissor->Rock wins \n" + "paper vs scissor->scissor wins \n")
while True:
    print('Enter choice \n 1. Rock \n 2. Paper \n 3. Scissors')
    time.sleep(1)
    print('Your choice is based on the number from 1 to 3.')
    choice = int(input('Player turn: '))
    while choice > 3 or choice < 1:
        print('Error, there is no such a choice. Please choose a number from 1 to 3.')
    if choice == 1:
        choice_name = 'Rock'   
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print('Player choice is: ' + choice_name)
    print("Now it's the computer's turn...")
    comp_choice = random.randint(1,3)
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
    if comp_choice == 1:
        bot_choice_name = 'Rock'
    elif comp_choice == 2:
        bot_choice_name = 'Paper'
    else:
        bot_choice_name = 'Scissors'
    if ((choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1)):
        print('Paper wins =>', end = "")
        result = 'Paper'
    elif ((choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1)):
        print('Rock wins => ', end = "")
        result = 'Rock'
    else:
        print('Scissors wins => ', end = "")
        result = 'Scissors'
    if result == choice_name:
        print('Player wins!')
    else:
        print('Bot wins!')
    print('Do you wish to play again? (Y/N)')
    answer = input()
    if answer == 'n' or answer == 'N':
        break
    print('Thanks for playing.') 