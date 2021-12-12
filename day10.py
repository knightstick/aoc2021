from statistics import median
from utils import read_day_lines


def first_illegal_character(line):
    char, _opens = __first_illegal_character__(line, [])
    return char


def incomplete_line(line):
    char, opens = __first_illegal_character__(line, [])
    return char == None and len(opens) > 0


def incomplete(lines):
    return filter(incomplete_line, lines)


def __first_illegal_character__(line, opens):
    if line == "":
        return None, opens
    char = line[0]
    last = opens[-1] if len(opens) > 0 else None

    match char:
        case ")":
            if last != "(":
                return char, opens
        case "]":
            if last != "[":
                return char, opens
        case "}":
            if last != "{":
                return char, opens
        case ">":
            if last != "<":
                return char, opens
        case "[" | "(" | "{" | "<":
            return __first_illegal_character__(line[1:], opens + [char])
        case other:
            raise RuntimeError(f"unknown bracket: {other}")

    return __first_illegal_character__(line[1:], opens[:-1])


def character_score(char):
    return {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
        None: 0
    }[char]


def error_score(line):
    return character_score(first_illegal_character(line))


def completion_string(line):
    _char, opens = __first_illegal_character__(line, [])
    return "".join(map(closer, reversed(opens)))


def completion_string_score(line):
    total = 0
    for char in completion_string(line):
        total *= 5
        total += point_value(char)

    return total


def point_value(char):
    return {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }[char]


def closer(opener):
    return {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }[opener]


def part1(lines):
    return sum(map(error_score, lines))


def part2(lines):
    return median(map(completion_string_score, incomplete(lines)))


if __name__ == '__main__':
    lines = read_day_lines(10)
    print(part1(lines), part2(lines))
