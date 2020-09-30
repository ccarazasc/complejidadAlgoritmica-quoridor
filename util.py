from math import cos, sin, pi

from djikstra import dijkstra_algorithm
from bfs import bfs_algorithm
from dfs import dfs_algorithm


def rotate(x, y, theta, c):
    x, y = x - c[0], y - c[1]

    _x = round(x * cos(theta * pi / 180) - y * sin(theta * pi / 180))
    _y = round(x * sin(theta * pi / 180) + y * cos(theta * pi / 180))

    x, y = c[0] + _x, c[1] + _y

    return x, y


def get_player_movement_algorithm(n_player):
    algorithms = {
        1: dijkstra_algorithm,
        2: dijkstra_algorithm,
        3: dijkstra_algorithm,
        4: dijkstra_algorithm
    }
    return algorithms[n_player]


def get_position_from_player_number(player, board):
    if 0 < player.n_player < 5:
        rotations = player.n_player - 1
        board_center = board.m // 2, board.n // 2
        _x, _y = rotate(player.x, player.y, 90 * rotations, board_center)
        return _x, _y
