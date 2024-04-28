import mastermind_functions as mmf

# welcome & explanation
print('\nWelcome !'
      '\nPrepare to test your mind and unravel the secret sequence of colors.'
      '\nAre you up for the Mastermind challenge?'
      '\n\nI\'m CODEX, your friendly AI companion.')

while True:
    player_name = input('\nWhat is your name?\t')
    if len(player_name) > 1:
        player_name = player_name.upper()
        break
    else:
        print('\nInvalid input! Please enter your name.')

print('Hi ' + player_name + ', I\'m looking forward to cracking the code with you!')
print(
    '\nTo win the game, you have to guess the colors of 3-6 pegs within 12 tries. '
    'You can choose from the following colors:'
    '\n - yellow (Y)'
    '\n - orange (O)'
    '\n - red (R)'
    '\n - purple (P)'
    '\n - blue (B)'
    '\n - green (G)'
    '\n\nAfter each guess, I will provide hints:'
    '\n - an \'x\' for each peg with the correct color in the correct position'
    '\n - an \'o\' for each peg with the correct color in the wrong position')

print('\nLet\'s start !')

repeat = True
while repeat == True:
    while True:
        code_length = input(
            '\nPlease select the number of pegs for the secret color code (3 for easy, up to 6 for difficult):\t')
        if len(code_length) == 1 and int(code_length) in range(3, 7):
            code_length = int(code_length)
            break
        else:
            print('\nInvalid input! Please enter a number between 3 and 6.')

    # code generation
    code = mmf.generate_code(code_length)

    # playing the game
    mmf.play(code, code_length, player_name)

    # show highscore
    mmf.highscore(10, code_length)

    # repeat?
    repeat = mmf.repeat(player_name)
