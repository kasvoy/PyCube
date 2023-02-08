def execute_scramble(scramble_string, cube):

    for symbol in scramble_string.split():
        rotate_on_symbol(symbol, cube)
    
def rotate_on_symbol(symbol, cube):

    if symbol == "R":
        cube.rotate_R()
    elif symbol == "R'":
        cube.rotate_Rprime()     
    elif symbol == "L":
        cube.rotate_L()
    elif symbol == "L'":
        cube.rotate_Lprime()
    elif symbol == "U":
        cube.rotate_U()
    elif symbol == "U'":
        cube.rotate_Uprime()
    elif symbol == "D":
        cube.rotate_D()
    elif symbol == "D'":
        cube.rotate_Dprime()
    elif symbol == "F":
        cube.rotate_F()
    elif symbol == "F'":
        cube.rotate_Fprime()
    elif symbol == "B":
        cube.rotate_B()
    elif symbol == "B'":
        cube.rotate_Bprime()
    elif symbol == "R2":
        cube.rotate_R2()
    elif symbol == "L2":
        cube.rotate_L2()
    elif symbol == "F2":
        cube.rotate_F2()
    elif symbol == "U2":
        cube.rotate_U2()
    elif symbol == "D2":
        cube.rotate_D2()
    elif symbol == "B2":
        cube.rotate_B2()