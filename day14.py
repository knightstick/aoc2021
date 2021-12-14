from collections import defaultdict
from collections import Counter

from utils import read_all


def split_pair(pair, rules):
    first, last = list(pair)
    next = rules[pair]
    return f"{first}{next}", f"{next}{last}"


if __name__ == '__main__':
    input = read_all(14)
    template, rulestr = input.strip().split("\n\n")
    rules = {}
    for line in rulestr.split("\n"):
        first, second = line.split(" -> ")
        rules[first] = second

    pairs = ["".join(template[i:i+2]) for i in range(len(template)-1)]
    counter = defaultdict(int)
    for pair in pairs:
        counter[pair] += 1

    for i in range(40):
        next_counter = defaultdict(int)
        for key, count in counter.items():
            first_pair, second_pair = split_pair(key, rules)
            next_counter[first_pair] += count
            next_counter[second_pair] += count
        counter = next_counter

    totals = defaultdict(int)
    for key, count in next_counter.items():
        first, second = list(key)
        totals[first] += count
    totals[template[-1]] += 1

    print(max(totals.values()) - min(totals.values()))
