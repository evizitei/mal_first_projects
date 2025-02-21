import random

player_wins = 0
comp_wins = 0

VALID_CHOICES = ['rock','paper','scissors']

player_win_conditions = {
    ('rock','scissors'): 'You win, I guessed scissors',
    ('paper','rock'): 'You win, I guessed rock',
    ('scissors','paper'): 'You win I guessed paper',
}
print(f'Rock Paper Scissors- best 3 out of 5!')  
while player_wins < 3 and comp_wins < 3:
    comp_guess = random.choice(VALID_CHOICES)
    player_choice = input ('rock, paper, scissors- shoot!').strip().lower()
    if player_choice not in VALID_CHOICES:
        print(f'Hey! guess rock, paper, or scissors')
    elif player_choice == comp_guess:
        print(f'We tied, I guessed {comp_guess}- neither of us gets a point')
    elif (player_choice,comp_guess) in player_win_conditions:
        print(f'You won, I guessed {comp_guess}')
        player_wins = player_wins + 1
    else:
        print (f'I won, I picked {comp_guess}')
        comp_wins = comp_wins + 1
    print(f'I have {comp_wins} point(s) you have {player_wins} point(s).')

if player_wins == 3:
    print('You won the game!')   
if comp_wins == 3:
    print('I won the game')    
print('Great game!')