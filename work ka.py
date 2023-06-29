import random
def let_user_pick(options):
    print("Please choose:")

options = ["play with computer", "play with another player"]
print('choose 1 play with another player')
print('choose 2 play with computer')
player = 1
computer = 2
rock = 1
paper = 2
scissors = 3
d = 0
user_1 = 0
user_2 = 0
bot = 0
user = int(input('choose. 1 or 2 ='))
if user == 1:
    print ('welcome to rock paper scissors game')
    print ('read first')
    print ('type 1 for rock')
    print('type 2 for paper')
    print('type 3 for scissors')
    user_1 = int(input('player1 choose only one number'))
    user_2 = int(input('player2 choose only one number'))
    if user_1 == user_2:
        print('on one win')
    elif user_1 == 1 and user_2 == 2:
        print('player2 win')
    elif user_1 == 1 and user_2 == 3:
        print('player1 win')
    elif user_1 == 2 and user_2 == 1:
        print('player1 win')
    elif user_1 == 2 and user_2 == 3:
        print('player2 win')
    elif user_1 == 3 and user_2 == 2:
        print('player1 win')
    elif user_1 == 3 and user_2 == 1:
        print('player2 win')
elif user == 2:
    print('welcome to rock paper scissors game(play with bot)')
    print('read first')
    print('type 1 for rock')
    print('type 2 for paper')
    print('type 3 for scissors')
    bot = random.randint(1,3)
    user = int(input('choose 1, 2 or 3 ='))
    if user == bot:
        print('no one win')
    elif user == 1 and bot == 2:
        print('you loss')
    elif user == 1 and bot == 3:
        print('you win')
    elif user == 2 and bot == 1:
        print('you win')
    elif user == 2 and bot == 3:
        print('you loss')
    elif user == 3 and bot == 1:
        print('you loss')
    elif user == 3 and bot == 2:
        print('you win')

