import random

player_wins = 0
comp_wins = 0

VALID_CHOICES = ['rock','paper','scissors']
WIN_TUPLES = [
    ('rock','scissors'),
    ('paper','rock'),
    ('scissors','paper')
]

def player_points(player_choice: str,comp_choice: str)->int:
    if player_choice == comp_choice:
        return 0
    elif (player_choice,comp_choice) in WIN_TUPLES:
        return 1
    elif (comp_choice,player_choice) in WIN_TUPLES:
        return -1
    else:
        raise ValueError(f'Invalid choices: {player_choice} and {comp_choice}')

print(f'Rock Paper Scissors- best 3 out of 5!')  
while player_wins < 3 and comp_wins < 3:
    comp_guess = random.choice(VALID_CHOICES)
    player_choice = input ('rock, paper, scissors- shoot!').strip().lower()
    try:
        result = player_points(player_choice,comp_guess)
        if result == 0:
            print(f'We tied, I guessed {comp_guess}- neither of us gets a point')
        elif result == 1:
            print(f'You won, I guessed {comp_guess}')
            player_wins = player_wins + 1
        else:
            print(f'I won, I picked {comp_guess}')
            comp_wins = comp_wins + 1
    except ValueError as e:
        print(f'Hey! guess rock, paper, or scissors! not {player_choice}')
    print(f'I have {comp_wins} point(s) you have {player_wins} point(s).')

if player_wins == 3:
    print('You won the game!')   
if comp_wins == 3:
    print('I won the game')    
print('Great game!')