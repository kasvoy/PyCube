import copy

class Cube:
    def __init__(self):

        self.up_face =    [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
        self.down_face =  [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
        self.front_face = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
        self.back_face =  [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
        self.left_face =  [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
        self.right_face = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
    
        self.set_state()

        """
        indexing the color of a sticker --> cube[face][row][column]
        index:
                0 - UP
                1 - LEFT
                2 - FRONT
                3 - RIGHT
                4 - BACK
                5 - DOWN
        """


    def set_state(self):
        self.state = [self.up_face, self.left_face, self.front_face, self.right_face, self.back_face, self.down_face]
    
    def get_state_copy(self):
        return copy.deepcopy(self.state)

    def rotate_R(self):
        state = self.get_state_copy()
        
        for i in range(3):
            self.up_face[i][2] = state[2][i][2]
            self.back_face[i][2] = state[0][i][2]
            self.down_face[i][2] = state[4][i][2]
            self.front_face[i][2] = state[5][i][2]

        self.set_state()
    
    def rotate_Rprime(self):

        state = self.get_state_copy()

        for i in range(3):
            self.up_face[i][2] = state[4][i][2]
            self.back_face[i][2] = state[5][i][2]
            self.down_face[i][2] = state[2][i][2]
            self.front_face[i][2] = state[0][i][2]
        
        self.set_state()


    def __str__(self):
        up_str = (f"UP FACE:    {self.up_face}\n")
        left_str = (f"LEFT FACE:  {self.left_face}\n")
        front_str = (f"FRONT FACE: {self.front_face}\n")
        right_str = (f"RIGHT FACE: {self.right_face}\n")
        back_str = (f"BACK FACE:  {self.back_face}\n")
        down_str = (f"DOWN FACE:  {self.down_face}\n")

        printout = up_str + left_str + front_str + right_str + back_str + down_str

        return printout


cube = Cube()

cube.rotate_Rprime()
cube.rotate_R()
print(cube)

        