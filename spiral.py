#  File: Spiral.py
#  Student Name: Matias Ramirez de Alva
#  Student UT EID: mr59342

import sys




# Input: in_data - handle to the input file
# Output: integer size of the spiral, odd integer between 1 and 100
def get_dimension(in_data):

    lines = in_data.readline()
    
    size = int(lines)

    return size


# Input: n - size of spiral
# Output: returns a 2-D list representing a spiral

def create_spiral(n):
    
    # create necessary variables

    dimension = n


    if (type(dimension) is not int) or (dimension < 1) or (dimension > 99):
        print("Invalid Spiral Size")
    else:
        if dimension % 2 == 0:
            dimension += 1
            side_length = dimension - 1
            spiral_count = (side_length) / 2
            highest_num = (dimension**2)
        else:
            side_length = dimension - 1
            spiral_count = int((side_length) / 2)
            highest_num = (dimension**2)

    

    grid = [[1 for i in range(dimension)] for j in range(dimension)]
    
    ###OUTER/UNIVERSAL FUNCTIONS###
    curr_num = highest_num
    ###OUTER/UNIVERSAL FUNCTIONS###

    for depth in range(spiral_count):
        ###THIS CODE RENAMES A TOP SIDE###
        y_pos = side_length
        x_pos = side_length
        for i in range(y_pos):
            grid[depth][y_pos+depth] = curr_num
            curr_num -= 1
            y_pos -= 1
        ###THIS CODE RENAMES A LEFT SIDE###
        y_pos = side_length
        x_pos = side_length
        for i in range(x_pos):
            grid[i+depth][depth] = curr_num
            curr_num -= 1
        ###THIS CODE RENAMES A BOTTOM SIDE###
        y_pos = side_length
        x_pos = side_length
        for i in range(y_pos):
            grid[x_pos+depth][i+depth] = curr_num
            curr_num -= 1
        ###THIS CODE RENAMES A RIGHT SIDE###
        y_pos = side_length
        x_pos = side_length
        for i in range(x_pos):
            grid[x_pos+depth][y_pos+depth] = curr_num
            x_pos -= 1
            curr_num -= 1
        ###this code adjust nums for next spiral###
        side_length -= 2
        
        ###this code adjust nums for next spiral###
        ####################################
        
    return grid
    
    # for i in range(len(grid)):
        # print(grid[i])




# Input: in_data - handle to input file
#        spiral - the number spiral
# Output: calls method for each integer in file
def print_adjacent_sums(in_data, spiral):

    lines = in_data.readlines()

    for n in lines:
        try:
            numb = int(n.strip())
            ans = sum_adjacent_numbers(spiral, numb)
            print(ans)
        except:
            pass
        

# Input: spiral - the number spiral
#        n - the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    
    ###THE FOLLOWING FIND INDEXES OF N###
    num = n

    i_counter = 0
    j_counter = 0

    ind_1 = 0
    ind_2 = 0

    for i in spiral:
        i_counter = 0
        for j in i:
            if spiral[i_counter][j_counter] == num:
                ind_1 = str(i_counter)
                ind_2 = str(j_counter)
            i_counter += 1
        j_counter += 1
    
    ###THE FOLLOWING FINDS ADJACENT NUMS###
    
    ###converts indeces back to ints###
    i1 = int(ind_1)
    i2 = int(ind_2)

    ###checks if top left is in spiral###
    if ((i1 - 1) >= 0) and ((i2 - 1) >= 0):
        top_left = spiral[i1 - 1][i2 - 1]
    else:
        top_left = 0

    ###checks if top middle is in spiral###
    if ((i1 - 1) >= 0):
        top_middle = spiral[i1 - 1][i2]
    else:
        top_middle = 0

    ###checks if top right is in spiral###
    if ((i1 - 1) >= 0) and ((i2 + 1) <= (len(spiral) - 1)):
        top_right = spiral[i1 - 1][i2 + 1]
    else:
        top_right = 0

    ###checks if middle left is in spiral###
    if ((i2 - 1) >= 0):
        middle_left = spiral[i1][i2 - 1]
    else:
        middle_left = 0
    
    ###checks if middle right is in spiral###
    if ((i2 + 1) <= (len(spiral) - 1)):
        middle_right = spiral[i1][i2 + 1]
    else:
        middle_right = 0

    ###checks if bottom left is in spiral###
    if ((i1 + 1) <= (len(spiral) - 1) and ((i2 - 1) >= 0)):
        bottom_left = spiral[i1 + 1][i2 - 1]
    else:
        bottom_left = 0

    ###checks if bottom middle is in spiral###
    if ((i1 + 1) <= (len(spiral) - 1)):
        bottom_middle = spiral[i1 + 1][i2]
    else:
        bottom_middle = 0
    
    ###checks if bottom right is in spiral###
    if ((i1 + 1) <= (len(spiral) - 1)) and ((i2 + 1) <= (len(spiral) - 1)):
        bottom_right = spiral[i1 + 1][i2 + 1]
    else:
        bottom_right = 0

    positions = [top_left, top_middle, top_right, middle_left, middle_right, bottom_left, bottom_middle, bottom_right]

    ###sums all adjacent nums###
    answer = sum(positions)
    return answer

   

# Added for debugging only. No changes needed.
# Do not call this method in submitted version of your code.
# Input: spiral - the number spiral
# Output: printed spiral
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()


''' ##### DRIVER CODE #####
    ##### Remember to change the debug flag before submitting. '''

# set the input source - change to False before submitting
debug = False
if debug:
    in_data = open('spiral.in')
else:
    in_data = sys.stdin

# get the spiral size from the file
size = get_dimension(in_data)


# if valid spiral size
if size != -1:
    
    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)

    # use following line for debugging only
    # print_spiral(spiral)
    

    # process and print adjacent sums

    print_adjacent_sums(in_data, spiral)