import random
from shutil import move
import sys

WIDTH = 40
HEIGHT = 20
NUM_ROBOTS = 10
NUM_TELEPORTS = 2
NUM_DEAD_ROBOTS = 2
NUM_WALLS = 100
EMPTY_SPACE = ' '
PLAYER = '@'
ROBOT = 'R'
DEAD_ROBOT = 'X'

WALL = chr(9617)


def main():
    print('''Hungry Robots, by Al Sweigart al@inventwithpython.com

    You are trapped in a maze with hungry robots! You don't know why robots
    need to eat, but you don't want to find out. The robots are badly
    programmed and will move directly toward you, even if blocked by walls.
    You must trick the robots into crashing into each other (or dead robots)
    without being caught. You have a personal teleporter device, but it only
    has enough battery for {} trips. Keep in mind, you and robots can slip
    through the corners of two diagonal walls!
    '''.format(NUM_TELEPORTS))
    input('Press Enter to begin...')

    board = get_new_board()
    robots = add_robots(board)
    player_position = get_random_empty_space(board, robots)
    while True:
        display_board(board, robots, player_position)

        if len(robots) == 0:
            print('All the robots have crashed into each other and you')
            print('lived to tell the tale! Good job!')
            sys.exit()

        player_position = ask_for_player_move(board, robots, player_position)


def get_new_board():
    board = {'teleports': NUM_TELEPORTS}

    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = EMPTY_SPACE

    for x in range(WIDTH):
        board[(x, 0)] = WALL
        board[(x, HEIGHT-1)] = WALL
    for y in range(HEIGHT):
        board[(0, y)] = WALL
        board[(WIDTH-1, y)] = WALL

    for i in range(NUM_WALLS):
        x, y = get_random_empty_space(board, [])
        board[(x, y)] = WALL
    for i in range(NUM_WALLS):
        x, y = get_random_empty_space(board, [])
        board[(x, y)] = DEAD_ROBOT
    return board


def get_random_empty_space(board, robots):
    while True:
        random_x = random.randint(1, WIDTH-2)
        random_y = random.randint(1, HEIGHT-2)
        if is_empty(random_x, random_y, board, robots):
            break
    return (random_x, random_y)


def is_empty(x, y, board, robots):
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots


def add_robots(board):
    robots = []
    for i in range(NUM_ROBOTS):
        x, y = get_random_empty_space(board, robots)
        robots.append((x, y))
    return robots


def display_board(board, robots, player_position):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if board[(x, y)] == WALL:
                print(WALL, end='')
            elif board[(x, y)] == DEAD_ROBOT:
                print(DEAD_ROBOT, end='')
            elif (x, y) in player_position:
                print(PLAYER, end='')
            elif (x, y) in robots:
                print(ROBOT, end='')
            else:
                print(EMPTY_SPACE, end='')
        print()


def ask_for_player_move(board, robots, player_position):
    player_x, player_y = player_position

    q = 'Q' if is_empty(player_x-1, player_y-1, board, robots) else ' '
    w = 'W' if is_empty(player_x-0, player_y-1, board, robots) else ' '
    e = 'E' if is_empty(player_x+1, player_y-1, board, robots) else ' '
    d = 'D' if is_empty(player_x+1, player_y+0, board, robots) else ' '
    c = 'C' if is_empty(player_x+1, player_y+1, board, robots) else ' '
    x = 'X' if is_empty(player_x+1, player_y+1, board, robots) else ' '
    z = 'Z' if is_empty(player_x-1, player_y+1, board, robots) else ' '
    a = 'A' if is_empty(player_x-1, player_y+0, board, robots) else ' '
    all_moves = (q+w+e+d+c+x+z+a+'S')

    while True:
        print('Teleports remaining: {}'.format(board['teleports']))
        print('                    ({}) ({}) ({})'.format(q, w, e))
        print('                    ({}) (S) ({})'.format(a, d))
        print('Enter move or QUIT: ({}) ({}) ({})'.format(z, x, c))

        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif move == 'T' and board['teleports'] > 0:
            board['teleports'] -= 1
            return get_random_empty_space(board, robots)
        elif move != '' and move in all_moves:
            return {
                'Q': (player_x-1, player_y-1),
                'W': (player_x+0, player_y-1),
                'E': (player_x+1, player_y-1),
                'D': (player_x+1, player_y+0),
                'C': (player_x+1, player_y+1),
                'X': (player_x+0, player_y+1),
                'Z': (player_x-1, player_y+1),
                'A': (player_x-1, player_y+0),
                'S': (player_x, player_y)
            }[move]
