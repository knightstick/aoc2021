from utils import read_all
import re


def parse_input(input):
    [(x1, x2, y1, y2)] = re.findall(
        r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", input)
    return int(x1), int(x2), int(y1), int(y2)


def step(location, velocity):
    x, y = location
    dx, dy = velocity
    x += dx
    y += dy
    if dx != 0:
        ddx = -1 if dx >= 0 else 1
    else:
        ddx = 0
    dx += ddx
    dy -= 1

    return (x, y), (dx, dy)


def sumk(k):
    return (k*(k+1)) / 2


def find_min_dx(x):
    for i in range(x):
        if sumk(i) > x:
            return i


def fly(initial_velocity, target_area):
    (ta_x1, ta_x2, ta_y1, ta_y2) = target_area
    probe = (0, 0)
    velocity = initial_velocity
    height = 0

    while True:
        probe, velocity = step(probe, velocity)
        px, py = probe
        dx, dy = velocity

        if py > height:
            height = py

        if px >= ta_x1 and px <= ta_x2 and py >= ta_y1 and py <= ta_y2:
            return ("hit", initial_velocity, height)

        if px > ta_x2 and py > ta_y2:
            return ("overshot", initial_velocity)

        if px >= ta_x1 and py > ta_y2 and (py + dy) < (2 * ta_y1):
            return("icarus", initial_velocity)

        if py < ta_y1:
            return("too low", initial_velocity)


if __name__ == '__main__':
    input = read_all(17).strip()
    target_area = parse_input(input)
    (ta_x1, ta_x2, ta_y1, ta_y2) = target_area

    min_dx = find_min_dx(ta_x1)
    max_dx = ta_x2 + 1
    min_dy = ta_y1

    velocs = {}
    for dx0 in range(min_dx, max_dx):
        dy0 = min_dy
        while True:
            match fly((dx0, dy0), target_area):
                case ("icarus", _):
                    break
                case ("overshot", _):
                    break
                case ("too low", _):
                    pass
                case ("hit", veloc, height):
                    velocs[veloc] = height
                case other:
                    raise NotImplementedError(f"{other}")
            dy0 += 1

    print(max(velocs.values()), len(velocs))
