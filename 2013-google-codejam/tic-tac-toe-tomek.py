"""When parsing game field, create two binary representations,
one for X (every X or T is 1, all else is 0),
and one for O. Also mark the fact that empty cells '.' are present.
"""
import sys


patterns = (
    # rows
    0b1111000000000000,
    0b0000111100000000,
    0b0000000011110000,
    0b0000000000001111,
    # columns
    0b1000100010001000,
    0b0100010001000100,
    0b0010001000100010,
    0b0001000100010001,
    # diagonals
    0b1000010000100001,
    0b0001001001001000,
)


def parse_case(text):
    code_x = 0
    code_o = 0
    has_dot = False
    for i, ch in enumerate(text):
        if ch == 'X':
            code_x |= 1 << i
        elif ch == 'O':
            code_o |= 1 << i
        elif ch == 'T':
            code_x |= 1 << i
            code_o |= 1 << i
        elif ch == '.':
            has_dot = True
    return code_x, code_o, has_dot


def test_win(code):
    for p in patterns:
        if code & p == p:
            return True
    return False


def main():
    n = int(sys.stdin.readline().strip())
    for i in xrange(1, n + 1):
        text = "".join([sys.stdin.readline().strip() for _ in xrange(5)])
        code_x, code_o, has_dot = parse_case(text)

        outcome = "ERROR"
        if test_win(code_x):
            outcome = "X won"
        elif test_win(code_o):
            outcome = "O won"
        elif has_dot:
            outcome = "Game has not completed"
        else:
            outcome = "Draw"

        print "Case #{0}: {1}".format(i, outcome)

if __name__ == '__main__':
    main()
