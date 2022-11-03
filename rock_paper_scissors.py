from random import choice
'''
plan na apke:
1. stworzyc podstawowe opcje
2. dodac bajery
3. zrobić jak najbardziej profesjonalna
'''
# make variables for counting and what are users options
user_count = 0
comp_count = 0
options = ['rock', 'paper', 'scissors']
print('\nWelcome to the rock, paper, scissors game!\nThe Rules are:\n1. Pick one of three options\n2. After your pick, you will get the results.\n3. If you want to quit and see scores, type "q"')
print('--------------------------------------------')

# adding while true for mulitple options
while True:
    user_choice = input('Rock/Paper/Scissors or Q for quit: ').lower()
    # making quit option and protect program from wrong input
    if user_choice == 'q':
        break
    if user_choice not in options:
        print('Wrong pick. Only rock, paper, scissors accepted.')
        continue
    # using randint for computer choice
    comp_choice = choice(options)
    print('Your pick:', user_choice)
    print('Computer pick:', comp_choice)
    # counting won games
    if user_choice == comp_choice:
        print('tie')
    elif user_choice == 'rock' and comp_choice == 'scissors':
        print('You won!')
        user_count += 1
    elif user_choice == 'paper' and comp_choice == 'rock':
        print('You won!')
        user_count += 1
    elif user_choice == 'scisorrs' and comp_choice == 'paper':
        print('You won!')
        user_count += 1
    else:
        print('You lose')
        comp_count += 1
# printing what scores are
print(f'You won {user_count} times. Computer won {comp_count} times.')
# dodać printa z ifelse np good luck next time
