from utils import read_day_lines, read_all
import re


BOARD_WIDTH = 5


def parse_board(string):
    num_rows = [re.findall(r"(\d+)", line.strip())
                for line in string.strip().split("\n")]

    board = []
    for num_row in num_rows:
        board.append([(num_row[j], False) for j in range(BOARD_WIDTH)])

    return board


def mark_number(board, number):
    for i in range(BOARD_WIDTH):
        for j in range(BOARD_WIDTH):
            if board[i][j][0] == number:
                board[i][j] = (number, True)
                # Assumes each board has each number only once
                return


def transpose(board):
    return [
        [board[j][i] for j in range(BOARD_WIDTH)]
        for i in range(BOARD_WIDTH)
    ]


def winner(board):
    for i in range(BOARD_WIDTH):
        if all([marked for num, marked in board[i] for i in range(BOARD_WIDTH)]):
            return True

    transposed = transpose(board)
    for i in range(BOARD_WIDTH):
        if all([marked for num, marked in transposed[i]]):
            return True

    return False


def unmarked_sum(board):
    sum = 0
    for i in range(BOARD_WIDTH):
        for num, marked in board[i]:
            if not marked:
                sum += int(num)

    return sum


def final_score(board, number):
    return unmarked_sum(board) * int(number)


def part1():
    [numbers_string, *board_strings] = read_all(4).split("\n\n")

    numbers = numbers_string.strip().split(",")
    boards = list(map(parse_board, board_strings))

    winning_board, number = None, None
    for number in numbers:
        for board in boards:
            mark_number(board, number)
        for board in boards:
            if winner(board):
                winning_board = board
                break
        if winning_board:
            break

    if winning_board:
        return final_score(winning_board, number)
    raise RuntimeError("No winners")


def part2():
    [numbers_string, *board_strings] = read_all(4).split("\n\n")

    numbers = numbers_string.strip().split(",")
    boards = list(map(parse_board, board_strings))

    remaining = boards
    winners = []
    number = None

    for number in numbers:
        for board in remaining:
            mark_number(board, number)

        new_remaining = []
        for board in remaining:
            if winner(board):
                winners.append(board)
            else:
                new_remaining.append(board)
        remaining = new_remaining
        if len(remaining) == 0:
            break

    return final_score(winners[-1], number)


if __name__ == '__main__':
    print(part1(), part2())
