import subprocess
from model import Cube
import scrambles

"""
Scramble 1: 
L' D L2 U2 F2 L' D2 R2 F2 L B2 L F2 R B L2 F U L U2 F

Scramble 2:
F2 L B D' F' B L F' B2 D' R2 U' F2 R2 U' L2 U2 D' L2 U2 B'
"""

#changes state of cube
def execute_scramble1(cube):
    cube.rotate_Lprime()
    cube.rotate_D()
    cube.rotate_L2()
    cube.rotate_U2()
    cube.rotate_F2()
    cube.rotate_Lprime()
    cube.rotate_D2()
    cube.rotate_R2()
    cube.rotate_F2()
    cube.rotate_L()
    cube.rotate_B2()
    cube.rotate_L()
    cube.rotate_F2()
    cube.rotate_R()
    cube.rotate_B()
    cube.rotate_L2()
    cube.rotate_F()
    cube.rotate_U()
    cube.rotate_L()
    cube.rotate_U2()
    cube.rotate_F()



def execute_scramble2(cube):
    cube.rotate_F2()
    cube.rotate_L()
    cube.rotate_B()
    cube.rotate_Dprime()
    cube.rotate_Fprime()
    cube.rotate_B()
    cube.rotate_L()
    cube.rotate_Fprime()
    cube.rotate_B2()
    cube.rotate_Dprime()
    cube.rotate_R2()
    cube.rotate_Uprime()
    cube.rotate_F2()
    cube.rotate_R2()
    cube.rotate_Uprime()
    cube.rotate_L2()
    cube.rotate_U2()
    cube.rotate_Dprime()
    cube.rotate_L2()
    cube.rotate_U2()
    cube.rotate_Bprime()



def main():

    subprocess.run("clear", shell = True)

    cube = Cube()
    print("inital:")
    print(cube,"\n")





    execute_scramble1(cube)
    print(cube)
if __name__ == "__main__":
    main()
