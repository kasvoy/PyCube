import subprocess
from model import Cube
from rotator import execute_scramble

def main():

    subprocess.run("clear", shell = True)

    cube = Cube()

    execute_scramble("U' R U' B2 L2 R2 U2 R2 F R2 F R2 D2 B R' U2 F' D B2 F2 U", cube)

    print(cube)
    
if __name__ == "__main__":
    main()
