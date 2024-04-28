class Try:
    def __init__(self, try_number: int):
        self.try_number = str(try_number)
        self.indent = '\t\t\t>>>   '

    def peg_input(self, code_length: int) -> list:
        error = (f'\tInvalid input! Please enter {code_length} valid colors (Y, O, R, P, B, G).\n')
        if self.try_number == '1':
            print('\n' + self.indent + self.try_number + '. try:   _' + ' _' * (code_length - 1))
        while True:
            pegs = str(input(self.indent + self.try_number + '. try:   ')).replace(' ', '').upper()
            if len(pegs) != code_length or any(element not in ('Y', 'O', 'R', 'P', 'B', 'G') for element in pegs):
                print(error)
            else:
                return list(pegs)

    def peg_output(self, peg_input, code):
        print(self.indent + self.try_number + '. try:   ' + ' '.join(peg_input))
        out = []
        input_false = []
        code_false = []
        for i in range(len(code)):
            if code[i] == peg_input[i]:
                out.append('x')
            else:
                input_false.append(peg_input[i])
                code_false.append(code[i])
        input_false.sort()
        code_false.sort()
        while len(input_false) > 0 and len(code_false) > 0:
            if code_false[0] == input_false[0]:
                out.append('o')
                code_false.remove(code_false[0])
                input_false.remove(input_false[0])
            elif code_false[0] > input_false[0]:
                input_false.remove(input_false[0])
            elif code_false[0] < input_false[0]:
                code_false.remove(code_false[0])
        if len(out) == 0:
            out.append('-')
        print(('\t' * 9) + (' ' * (3 - len(out))) + ''.join(out))
        if self.try_number == '1':
            if out == ['-']:
                print(f'\t\tHint: Your code contains no correct color.\n')
            else:
                count_x = out.count('x')
                count_o = out.count('o')
                if count_x == 1 and count_o == 0:
                    print(
                        f'\t\tHint: Your code contains {count_x} peg with the correct color in the correct position.\n')
                elif count_x > 1 and count_o == 0:
                    print(
                        f'\t\tHint: Your code contains {count_x} pegs with the correct color in the correct position.\n')
                elif count_x == 0 and count_o == 1:
                    print(f'\t\tHint: Your code contains {count_o} peg with the correct color in the wrong position.\n')
                elif count_x == 0 and count_o > 1:
                    print(
                        f'\t\tHint: Your code contains {count_o} pegs with the correct color in the wrong position.\n')
                elif count_x == 1 and count_o == 1:
                    print(f'\t\tHint: Your code contains {count_x} peg with the correct color in the correct position'
                          f' and {count_o} peg with the correct color in the wrong position.\n')
                elif count_x > 1 and count_o > 1:
                    print(f'\t\tHint: Your code contains {count_x} pegs with the correct color in the correct position'
                          f' and {count_o} pegs with the correct color in the wrong position.\n')
        if self.try_number == '11':
            print(f'\t\tHint: You have only one try left !\n')
        return out
