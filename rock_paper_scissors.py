from random import randint

options = ['rock', 'paper', 'scissors']


class Main:
    def __init__(self):
        self.choice = 'None'
        self.score = 0

    def get_input(self, choice, run):
        x = 0
        for i in range(3):
            if choice == options[i]:
                x = 1
        if x == 0:
            print('Wrong input')
            run = False
            return run
        if x == 1:
            self.choice = choice
            return run

    def return_choice(self):
        return self.choice

    def checking(self, computer_choice):
        if self.choice != 'None':
            if self.choice == 'rock' and computer_choice == 'scissors':
                self.score += 1
            elif self.choice == 'rock' and computer_choice == 'paper':
                self.score -= 1
            if self.choice == 'paper' and computer_choice == 'rock':
                self.score += 1
            elif self.choice == 'paper' and computer_choice == 'scissors':
                self.score -= 1
            if self.choice == 'scissors' and computer_choice == 'rock':
                self.score -= 1
            elif self.choice == 'scissors' and computer_choice == 'paper':
                self.score += 1

    def return_score(self):
        return self.score


player = Main()
run = True
while run:
    run = player.get_input(input('Enter your choice: '), run)
    if run == True:
        computer_choice = options[randint(0, 2)]
        print('the computer choice is:', computer_choice)
        player.checking(computer_choice)
    print(player.return_score())
