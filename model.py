import copy


UP_FACE =    [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
LEFT_FACE =  [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
FRONT_FACE = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
RIGHT_FACE = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
BACK_FACE =  [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]
DOWN_FACE =  [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]

INITIAL = [UP_FACE, LEFT_FACE, FRONT_FACE, RIGHT_FACE, BACK_FACE, DOWN_FACE]


class Cube:
    def __init__(self, scramble = INITIAL):

        self.up_face    = scramble[0]
        self.left_face  = scramble[1]
        self.front_face = scramble[2]
        self.right_face = scramble[3]
        self.back_face  = scramble[4]
        self.down_face  = scramble[5]
        
        self.set_state()

        """
        Initial orientation ---> WHITE UP, GREEN FRONT

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
    
    def reset(self):
        self.up_face = INITIAL[0]
        self.left_face = INITIAL[1]
        self.front_face = INITIAL[2]
        self.right_face = INITIAL[3]
        self.back_face = INITIAL[4]
        self.down_face = INITIAL[5]

        self.set_state()

    def get_state_copy(self):
        return copy.deepcopy(self.state)

    def rotate_R_Lprime(self, col_no):

        """
        For R: col_no = 2
        For L prime: col_no = 0 
        """

        state = self.get_state_copy()
        
        first_column_backface_reversed = list(reversed([row[0] for row in state[4]]))
        third_column_backface_reversed = list(reversed([row[2] for row in state[4]]))

        first_column_frontface_reversed = list(reversed([row[0] for row in state[0]]))
        third_column_frontface_reversed = list(reversed([row[2] for row in state[0]]))

        for i in range(3):
            self.up_face[i][col_no] = state[2][i][col_no]       
            self.front_face[i][col_no] = state[5][i][col_no]

            if col_no == 2:
                self.down_face[i][col_no] = first_column_backface_reversed[i]
                self.back_face[i][0] = third_column_frontface_reversed[i]
            else:
                self.down_face[i][col_no] = third_column_backface_reversed[i]
                self.back_face[i][2] = first_column_frontface_reversed[i]
        
        if col_no == 2:
            self.right_face = rotate_face_clockwise(self.right_face)
        else:
            self.left_face = rotate_face_anticlockwise(self.left_face)

        self.set_state()
    
    def rotate_Rprime_L(self, col_no):
        """
        For Rprime: col_no = 2
        For L: col_no = 0 
        """

        state = self.get_state_copy()

        first_column_backface_reversed = list(reversed([row[0] for row in state[4]]))
        third_column_backface_reversed = list(reversed([row[2] for row in state[4]]))  

        first_column_downface_reversed = list(reversed([row[0] for row in state[5]]))
        third_column_downface_reversed = list(reversed([row[2] for row in state[5]]))              

        for i in range(3):
            
            self.down_face[i][col_no] = state[2][i][col_no]
            self.front_face[i][col_no] = state[0][i][col_no]
        
            if col_no == 2:
                self.back_face[i][0] = third_column_downface_reversed[i]
                self.up_face[i][col_no] = first_column_backface_reversed[i]
            else:
                self.back_face[i][2] = first_column_downface_reversed[i]
                self.up_face[i][col_no] = third_column_backface_reversed[i]
        
        if col_no == 2:
            self.right_face = rotate_face_anticlockwise(self.right_face)
        else:
            self.left_face = rotate_face_clockwise(self.left_face)


        self.set_state()


    def rotate_U_Dprime(self, row_no):
        """
        For U: row_no = 0
        FOr D': row_no = 2 
        """
    
        state = self.get_state_copy()

        for i in range(3): 
            self.front_face[row_no][i] = state[3][row_no][i]
            self.left_face[row_no][i] = state[2][row_no][i]
            self.back_face[row_no][i] = state[1][row_no][i]
            self.right_face[row_no][i] = state[4][row_no][i]
        
        if row_no == 0:
            self.up_face = rotate_face_clockwise(self.up_face)
        else:
            self.down_face = rotate_face_anticlockwise(self.down_face)

        self.set_state()


    def rotate_Uprime_D(self, row_no):
        state = self.get_state_copy()

        for i in range(3):
            self.front_face[row_no][i] = state[1][row_no][i]
            self.left_face[row_no][i] = state[4][row_no][i]
            self.back_face[row_no][i] = state[3][row_no][i]
            self.right_face[row_no][i] = state[2][row_no][i]

        if row_no == 0:
            self.up_face = rotate_face_anticlockwise(self.up_face)
        else:
            self.down_face = rotate_face_clockwise(self.down_face)


        self.set_state()

    def rotate_F(self):
        
        state = self.get_state_copy()

        third_column_leftface_reversed = list(reversed([row[2] for row in state[1]]))
        first_column_rightface_reversed = list(reversed([row[0] for row in state[3]]))

        for i in range(3):
            self.up_face[2][i] = third_column_leftface_reversed[i]
            self.down_face[0][i] = first_column_rightface_reversed[i]
            self.right_face[i][0] = state[0][2][i]
            self.left_face[i][2] = state[5][0][i]
            
        self.front_face = rotate_face_clockwise(self.front_face)

        self.set_state()
    
    def rotate_Fprime(self):

        state = self.get_state_copy()

        third_row_upface_reversed = list(reversed(state[0][2]))
        first_row_downface_reversed = list(reversed(state[5][0]))

        for i in range(3):
            self.up_face[2][i] = state[3][i][0]
            self.left_face[i][2] = third_row_upface_reversed[i]
            self.down_face[0][i] = state[1][i][2]
            self.right_face[i][0] = first_row_downface_reversed[i]

        self.front_face = rotate_face_anticlockwise(self.front_face)

        self.set_state()

    def rotate_B(self):

        state = self.get_state_copy()

        first_row_upface_reversed = list(reversed(state[0][0]))
        third_row_downface_reversed = list(reversed(state[5][2]))

        for i in range(3):
            self.up_face[0][i] = state[3][i][2]
            self.left_face[i][0] = first_row_upface_reversed[i]
            self.down_face[2][i] = state[1][i][0]
            self.right_face[i][2] = third_row_downface_reversed[i]

        self.back_face = rotate_face_clockwise(self.back_face)

        self.set_state()
    
    def rotate_Bprime(self):
        
        state = self.get_state_copy()

        first_column_leftface_reversed = list(reversed([row[0] for row in state[1]]))
        third_column_rightface_reversed = list(reversed([row[2] for row in state[3]]))

        for i in range(3):
            self.up_face[0][i] = first_column_leftface_reversed[i]
            self.right_face[i][2] = state[0][0][i]
            self.down_face[2][i] = third_column_rightface_reversed[i]
            self.left_face[i][0] = state[5][2][i]

        self.back_face = rotate_face_anticlockwise(self.back_face)

        self.set_state()

    def rotate_R(self):
        self.rotate_R_Lprime(2)
        
    def rotate_Rprime(self):
        self.rotate_Rprime_L(2)

    def rotate_R2(self):
        self.rotate_R()
        self.rotate_R()
    
    def rotate_L(self):
        self.rotate_Rprime_L(0)
    
    def rotate_Lprime(self):
        self.rotate_R_Lprime(0)
    
    def rotate_L2(self):
        self.rotate_L()
        self.rotate_L()
    
    def rotate_U(self):
        self.rotate_U_Dprime(0)
    
    def rotate_Uprime(self):
        self.rotate_Uprime_D(0)

    def rotate_U2(self):
        self.rotate_U()
        self.rotate_U()
    
    def rotate_D(self):
        self.rotate_Uprime_D(2)
    
    def rotate_Dprime(self):
        self.rotate_U_Dprime(2)
    
    def rotate_D2(self):
        self.rotate_D()
        self.rotate_D()
    
    def rotate_F2(self):
        self.rotate_F()
        self.rotate_F()

    def rotate_B2(self):
        self.rotate_B()
        self.rotate_B()

    def __str__(self):
        up_str = (f"UP FACE:    {self.up_face}\n")
        left_str = (f"LEFT FACE:  {self.left_face}\n")
        front_str = (f"FRONT FACE: {self.front_face}\n")
        right_str = (f"RIGHT FACE: {self.right_face}\n")
        back_str = (f"BACK FACE:  {self.back_face}\n")
        down_str = (f"DOWN FACE:  {self.down_face}")

        printout = up_str + left_str + front_str + right_str + back_str + down_str

        return printout


def rotate_face_clockwise(face):
    face_copy = copy.deepcopy(face)

    for i in range(3):
        face_copy[i][2] = face[0][i]
        face_copy[i][1] = face[1][i]
        face_copy[i][0] = face[2][i]

    return face_copy


def rotate_face_anticlockwise(face):
    face_copy = copy.deepcopy(face)

    for i in range(3):
        face_copy[i][0] = list(reversed(face[0]))[i]
        face_copy[i][1] = list(reversed(face[1]))[i]
        face_copy[i][2] = list(reversed(face[2]))[i]

    return face_copy