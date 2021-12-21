import itertools


class DeterministicDice:
    def __init__(self, iter):
        self.iter = iter
        self.rolls = 0

    def take(self, n):
        self.rolls += n
        return list(itertools.islice(self.iter, None, n))


if __name__ == '__main__':
    players = [
        {"space": 8, "score": 0},
        {"space": 5, "score": 0},
    ]

    dd = DeterministicDice(itertools.cycle(range(1, 101)))
    rolls = 0
    i = 0
    while True:
        roll = dd.take(3)
        player = i % 2
        players[player]["space"] = (players[player]["space"] + sum(roll)) % 10
        players[player]["score"] += 10 if players[player]["space"] == 0 else players[player]["space"]
        if players[player]["score"] >= 1000:
            break
        i += 1

    losing_score = min(map(lambda player: player["score"], players))
    print(losing_score * dd.rolls)
