from handout import *
from matplotlib import pyplot as plt
import numpy as np

VERY_SMALL = 0
SMALL = 1
PERFECT = 2
BIG = 3
VERY_BIG = 4

SHRINKING_FAST = 0
SHRINKING = 1
STABLE = 2
GROWING = 3
GROWING_FAST = 4

BREAK_HARD = 0
SLOW_DOWN = 1
NONE = 2
SPEED_UP = 3
FLOOR_IT = 4

distance = [
    lambda x: reverse_grade(x, 1, 2.5),
    lambda x: triangle(x, 1.5, 3, 4.5),
    lambda x: triangle(x, 3.5, 5, 6.5),
    lambda x: triangle(x, 5.5, 7, 8.5),
    lambda x: grade(x, 7.5, 9, 1)
]

delta = [
    lambda x: reverse_grade(x, -4, -2.5),
    lambda x: triangle(x, -3.5, -2, -0.5),
    lambda x: triangle(x, -1.5, 0, 1.5),
    lambda x: triangle(x, 0.5, 2, 3.5),
    lambda x: grade(x, 2.5, 4, 1)
]

actions = [
    lambda x, clip: reverse_grade(x, -8, -5, clip),
    lambda x, clip: triangle(x, -7, -4, -1, clip),
    lambda x, clip: triangle(x, -3, 0, 3, clip),
    lambda x, clip: triangle(x, 1, 4, 7, clip),
    lambda x, clip: grade(x, 5, 8, clip)
]

rules = [
    lambda a, b: distance[VERY_SMALL](a),
    lambda a, b: min([distance[SMALL](a), delta[STABLE](b)]),
    lambda a, b: min([distance[SMALL](a), delta[GROWING](b)]),
    lambda a, b: min([distance[PERFECT](a), delta[GROWING](b)]),
    lambda a, b: min([distance[VERY_BIG](a), max([1 - delta[GROWING](b), 1 - delta[GROWING_FAST](b)])])
]


def accumulation(x, a, b):
    return max(actions[i](x, rules[i](a, b)) for i in range(len(actions)))


def center_of_gravity(x_from, x_to, step, a, b):
    xfdx = sum([x * accumulation(x, a, b) * step for x in np.arange(x_from, x_to + step, step)])
    fdx = sum([accumulation(x, a, b) * step for x in np.arange(x_from, x_to + step, step)])
    return xfdx / fdx


def fuzz(dist, delt, visualize=False):
    if visualize:
        # Plot action
        act_x = np.arange(-10, 10.1, .1)
        act_bh, act_sl, act_n, act_su, act_fi = [[a(x, 1) for x in act_x] for a in actions]
        acc = [accumulation(x, dist, delt) for x in act_x]

        plt.figure("Action")
        plt.plot(act_x, act_bh, 'xkcd:dark sky blue')
        plt.plot(act_x, act_sl, 'r-')
        plt.plot(act_x, act_n, 'xkcd:apple green')
        plt.plot(act_x, act_su, 'xkcd:purple')
        plt.plot(act_x, act_fi, 'xkcd:baby blue')
        plt.plot(act_x, acc, 'xkcd:orange')
        plt.plot([center_of_gravity(-10, 10, .1, dist, delt)] * 2, [0, 1], 'k--')
        plt.legend(['BreakHard', 'SlowDown', 'None', 'SpeedUp', 'FloorIt', 'Accumulation', 'CenterOfGravity'],
                   loc='right', ncol=1)
        plt.show()

    return center_of_gravity(-10, 10, .1, dist, delt)

