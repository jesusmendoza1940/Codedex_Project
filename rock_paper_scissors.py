import random

print("===================")
print("Rock Paper Scissors")
print('===================')

while True:
    print('1) ✊')
    print('2) ✋')
    print('3) ✌️')
    print('4) 🦎')
    print('5) 🖖')
    choice = int(input('Pick a number: '))
    rand_num = random.randint(1,5)
    print(f'You chose: {choice}')
    print(f'CPU chose: {rand_num}')
    if choice == 3 and rand_num == 2: #Scissors cut Paper.
        print('The player won!')
    elif choice == 2 and rand_num == 1: #Paper covers Rock.
        print('The player won!')
    elif choice == 1 and rand_num == 4: # Rock crushes Lizard.
        print('The player won!')
    elif choice == 4 and rand_num == 5: #Lizard poisons Spock.
        print('The player won!')
    elif choice == 5 and rand_num == 3: #Spock smashes Scissors.
        print('The player won!')
    elif choice == 3 and rand_num == 4: #Scissors beat Lizard.
        print('The player won!')
    elif choice == 4 and rand_num == 2:#Lizard eats Paper.
        print('The player won!')
    elif choice == 2 and rand_num == 5:#Paper disproves Spock.
        print('The player won!')
    elif choice == 5 and rand_num == 1: #Spock vaporizes Rock.
        print('The player won!')
    elif choice == 1 and rand_num == 3: #Rock breaks Scissors.
        print('The player won!')
    elif choice == rand_num:
        print("It's a tie!")
    else:
        print('The CPU won!')
    play = input('\nPlay Again? (Y/N): ')
    if play == 'Y' or play == 'y':
        print('\n')
    elif play == 'N' or play == 'n':
        print('Thanks for playing\n')
        break
    else:
        print('Wrong choice so we playing again\n')




