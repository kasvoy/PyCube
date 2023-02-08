import copy

"""
ALL SCRAMBLES' INITIAL ORIENTATION: WHITE TOP, GREEN FRONT

Scramble 1: 
L' D L2 U2 F2 L' D2 R2 F2 L B2 L F2 R B L2 F U L U2 F

Scramble 2:
F2 L B D' F' B L F' B2 D' R2 U' F2 R2 U' L2 U2 D' L2 U2 B'
"""

up1 =    [['o', 'w', 'y'], ['o', 'w', 'g'], ['g', 'b', 'r']]
left1 =  [['g', 'y', 'r'], ['o', 'o', 'b'], ['w', 'y', 'o']]
front1 = [['w', 'w', 'g'], ['y', 'g', 'r'], ['w', 'o', 'o']]
right1 = [['y', 'o', 'o'], ['g', 'r', 'w'], ['b', 'g', 'y']]
back1 =  [['b', 'r', 'y'], ['g', 'b', 'w'], ['r', 'b', 'r']]
down1 =  [['g', 'b', 'w'], ['r', 'y', 'y'], ['b', 'r', 'b']]

scramble1 = [up1, left1, front1, right1, back1, down1]

up2 =    [['o', 'g', 'g'], ['o', 'w', 'b'], ['r', 'w', 'y']]
left2 =  [['w', 'b', 'y'], ['y', 'o', 'g'], ['b', 'y', 'o']]
front2 = [['b', 'b', 'o'], ['w', 'g', 'w'], ['b', 'r', 'o']]
right2 = [['b', 'r', 'r'], ['o', 'r', 'w'], ['g', 'y', 'y']]
back2 =  [['w', 'r', 'g'], ['r', 'b', 'b'], ['g', 'g', 'w']]
down2 =  [['w', 'y', 'y'], ['o', 'y', 'g'], ['r', 'o', 'r']]

scramble2 = [up2, left2, front2, right2, back2, down2]
