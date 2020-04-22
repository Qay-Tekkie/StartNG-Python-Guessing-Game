import random

secret_number = 8

trial = 0
guess_limit = 0
# user is able to guess numbers against the number you set
print('Guess a number')
while True:
    try:
        guess_number = int(input(''))
        break
    except ValueError:
        print('You must enter a number')
if guess_number == secret_number:
    print('You got it right!')
else:
    if guess_number != secret_number:
        print('''That was wrong. The game has 3 levels
                    >Easy
                    >Medium
                    >Hard''')
        levels = input('Set your level: ')
            
        # if user enters a wrong number,user should be told there are 3 levels
        if levels.lower() == 'easy':
            # at easy,there are 6 guesses and chances between 1-10
            guesses_left = 5
            secret_number = 4
            guess_limit = 6
            number = random.randint(1,10)
            while trial < guess_limit:
                print('Guess a number between 1 and 10')
                while True:
                    try:
                        guess_number = int(input(''))
                        break
                    except ValueError:
                        print('You must enter a number')
                if guess_number ==secret_number:
                    print('You got it right!')

                    break
                else:
                    print('That was wrong!')
                    print('you have ' + str(guesses_left) + ' guesses left' )
                    trial+=1
                    guesses_left -=1
            else:
                print('game over')
                
        elif levels.lower() == 'medium':
            # at medium,there are 4 guesses and chances between 1-20
            guesses_left = 3
            secret_number = 15
            guess_limit = 4
            number = random.randint(1,20)
            while trial < guess_limit:
                print('Guess a number between 1 and 20')
                while True:
                    try:
                        guess_number = int(input(''))
                        break
                    except ValueError:
                        print('You must enter a number')
                if guess_number == secret_number:
                    print('You got it right!')

                    break
                else:
                    print('That was wrong!')
                    print('you have ' + str(guesses_left) + ' guesses left') 
                    trial+=1
                    guesses_left -=1
            else:
                print('game over') 
        elif levels.lower() == 'hard':
            # at hard, there 3 guesses and chances between 1-50
            guesses_left = 2
            secret_number = 45
            guess_limit = 3
            number = random.randint(1,50)
            while trial < guess_limit:
                print('Guess a number between 1 and 50')
                while True:
                    try:
                       guess_number = int(input('')) 
                       break
                    except ValueError:
                        print('You must enter a number')
                if guess_number ==secret_number:
                    print('You got it right!')
                    break
                else:
                    print('That was wrong!')
                    print('you have ' + str(guesses_left) + ' guesses left')
                    trial+=1
                    guesses_left -=1
            else:
                print('game over')
        else:
            print('Wrong input. Select a level')
          