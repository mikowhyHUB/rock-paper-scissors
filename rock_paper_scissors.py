from random import choice
'''
plan na apke:
1. stworzyc podstawowe opcje
2. dodac bajery
3. zrobić jak najbardziej profesjonalna
'''
# variables for counting and what are users options
user_count = 0
comp_count = 0


def user_selection(options):
    while True:  # while true for multiply selection
        user_choice = input('Rock/Paper/Scissors or Q for quit: ').lower()
        # making quit option and protect program from wrong input
        if user_choice == 'q':
            break
        if user_choice not in options:  # do zabezpieczenia przed errorami
            print('Wrong pick. Only rock, paper, scissors accepted.')
            continue
        return user_choice


def computer_selection(options):
    # using randint for computer choice
    comp_choice = choice(options)
    print('Your pick:', user_selection(options))
    print('Computer pick:', comp_choice)
    return comp_choice


def play():
    # counting won games
    if user_selection() == computer_selection():
        print('tie')
    elif user_selection() == 'rock' and computer_selection() == 'scissors':
        print('You won!')
        user_count += 1
    elif user_selection() == 'paper' and computer_selection() == 'rock':
        print('You won!')
        user_count += 1
    elif user_selection() == 'scisorrs' and computer_selection() == 'paper':
        print('You won!')
        user_count += 1
    else:
        print('You lose')
        comp_count += 1


# printing what scores are
print(f'You won {user_count} times. Computer won {comp_count} times.')
# dodać printa z ifelse np good luck next time


def main():
    print('''Welcome to the rock, paper, scissors game!
    The Rules are:
    1. Pick one of three options
    2. After your pick, you will get the results.
    3. If you want to quit and see scores, type "q"''')
    options_list = ['rock', 'paper', 'scissors']
    player_result = user_selection(options_list)
    computer_result = computer_selection(options_list)
    # play()


main()
