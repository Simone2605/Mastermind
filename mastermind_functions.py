import datetime as dt
import mastermind_classes as mmc
import csv


def generate_code(length: int) -> list:
    from random import choice
    code = []
    for _ in range(length):
        code.append(choice('YORPBG'))
    return code


def play(code: list, code_length: int, player_name: str):
    try_count = 0
    start_time = dt.datetime.now()
    for x in range(1, 13):
        try_x = mmc.Try(x).peg_input(code_length)
        hint_x = mmc.Try(x).peg_output(try_x, code)
        try_count += 1
        if ''.join(hint_x) == 'x' * code_length:
            end_time = dt.datetime.now()
            time = (end_time - start_time).total_seconds().__round__(3)
            if try_count == 1:
                print(
                    f'\nCongratulations ! You solved the color code within only {try_count} try and {time} seconds. Excellent guess !')
            elif try_count > 1 and try_count <= 6:
                print(
                    f'\nCongratulations ! You solved the color code within {try_count} tries and {time} seconds. Good job !')
            elif try_count > 6 and try_count <= 12:
                print(
                    f'\nCongratulations ! You solved the color code within {try_count} tries and {time} seconds. Well done !')
            csv.writer(open(f'mastermind_highscore_{code_length}.csv', 'a', newline='\n')).writerow(
                [player_name, try_count, time])
            break
        elif x == 12 and ''.join(hint_x) != 'x' * code_length:
            print('\nGame over !')


def highscore(top_n: int, code_length: int):
    try:
        highscore = csv.reader(open(f'mastermind_highscore_{code_length}.csv', 'r'))
        top_ten = sorted(highscore, key=lambda row: (int(row[1]), float(row[2])))[:10]
        print('\n\n\t\t\t\t --- HIGHSCORE ---\n')
        place = 0
        for list in top_ten:
            place += 1
            print(f'\t\t\t{place}. {list[0]}:  {list[1]} tries  in  {list[2]} seconds')
    except:
        pass


def repeat(name: str) -> bool:
    repeat = input(f'\nDo you like to play again, {name}?\t').upper()
    if repeat == 'Y' or repeat == 'YES':
        return True
    else:
        return False
