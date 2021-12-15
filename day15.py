from utils import read_day_lines
from itertools import cycle
import sys
from datetime import datetime


def increment_risk(risk, step):
    new_risk = risk + step
    while new_risk > 9:
        new_risk -= 9
    return new_risk


def get_neighbours(point, height):
    x, y = point
    neighbours = []
    if x-1 >= 0:
        neighbours.append((x-1, y))
    if x+1 < height:
        neighbours.append((x+1, y))
    if y-1 >= 0:
        neighbours.append((x, y-1))
    if y+1 < height:
        neighbours.append((x, y+1))
    return neighbours


def down_right_path(grid):
    width = len(grid[0])
    height = len(grid)

    memo = [[0 for i in range(width)] for j in range(height)]

    # First column is just sum to get there
    for i in range(1, height):
        memo[0][i] = grid[0][i] + memo[0][i-1]

    # First row is just sum to get there
    for i in range(1, width):
        memo[i][0] = grid[i][0] + memo[i-1][0]

    for x in range(1, width):
        for y in range(1, height):
            memo[x][y] = grid[x][y] + min(memo[x-1][y], memo[x][y-1])

    return memo[width-1][height-1]


def dijkstra_i_think(grid):
    height = len(grid)
    risks = [[sys.maxsize for digit in row] for row in grid]
    risks[0][0] = 0
    visited = set()

    least_risk_node = None
    steps = 0
    checkin = datetime.now()
    while least_risk_node != (height - 1, height - 1):
        if steps % 1000 == 0:
            new_checkin = datetime.now()
            delta = new_checkin - checkin
            print("Visited", len(visited))
            print("Delta", delta)
            checkin = new_checkin

        steps += 1

        # Find the least risky next node
        least_risk_node = None
        least_risk = sys.maxsize
        for x in range(height):
            for y in range(height):
                if not (x, y) in visited and risks[x][y] < least_risk:
                    least_risk = risks[x][y]
                    least_risk_node = (x, y)

        # Visit it
        visited.add(least_risk_node)

        # For all the neighbours, calculate the risk
        neighbours = get_neighbours(least_risk_node, height)
        for neighbour in neighbours:
            if not neighbour in visited:
                x, y = neighbour
                if risks[x][y] == sys.maxsize:
                    risks[x][y] = least_risk + grid[x][y]

    x, y = least_risk_node
    return risks[x][y]


if __name__ == '__main__':
    lines = read_day_lines(15)
    grid = [[int(digit) for digit in list(line)] for line in lines]

    width = len(grid[0])
    height = len(grid)
    new_grid = [[0 for i in range(5 * width)] for j in range(5 * height)]

    for i in range(5):
        for j in range(5):
            for x in range(width):
                for y in range(height):
                    new_grid[x + (i * width)][y + (j * height)
                                              ] = increment_risk(grid[x][y], i + j)

    print(down_right_path(grid))
    print(dijkstra_i_think(new_grid))
