from random import randint

'''
Class ver:
1.  stowrzyć klasę player, konstruktor init, w nim dwie zmienne instance(nie parametry do konstruktora) choice none , score 0. 
2. stworzyć metodę get_input z parametrem choice, i zabezpiecz ją od złych enterów:
- stwórz for loopa by zlupowal options i ifa by sprawidzc czy zgadza się z options. jeeli się zagadza, dodaj do zmiennje 1(1 oznacza, ze jest ok)
- if poza petla mówiący, ze jak będzie 0 to wyprintować info. Zmienic tez konstruktor run na false. zwrócic run. 
-drugi if jezeli jest 1 to print ze wszystko ok i przyznac choice do choice i zwrocic run(ktory jest noramlnei true)
3. stworz metode by  zwracala wybor i niech zwraca choice
4. stworz metode sprawdajaca o parametrze wyboru komputera i na razie pass
5. stworz metode zwracajaca wynik i niech zwraca wynik
6. stworz obiekt run który jest standardowo true oraz while loop z runem. 
- stworz zmienna run i tam uzyj clasy i metody get input. w jako parametry daj input i run
7. zdefiniuj obiekt przed run = true. inaczej nie bedzie 6 dzialac
8. stworz if i jezeli run bedzie true to wtedy robimy komputer choice z options i randint
- wydrukuj wybor komputera
- stworz kto wygral - klasa. wybór(wybór komputera)
- poza petla print by zwrocilo wynik
9. dodaj do metody sprawdzania petle if ktora mowi ze gdy wybor jest inny niz ten podany jako zmienna choice, wtedy nastepna petla i podajemy warunki wygranej i dodajemy punkt do self.score
'''
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
