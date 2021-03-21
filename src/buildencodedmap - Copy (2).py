from collections import namedtuple
#from globals import *
import globals

class data_single_cell:
    ''' The cell node that holds information of each cell in the field matrix.'''
    x = 0
    y = 0
    xy_key = ''
    head_of_chain_cell = False   # used to keep track of which node is the beginning of the linked list chain
    tail_of_chain_cell = False
    header_prev_cell = None  # Doubly linked list
    header_next_cell = None
    array_of_valid_moves = [4]
    array_of_used_choices = [4]
    cell_time_to_enter = 0


#    matrix_size = xy_namedtuple(X_SIZE, Y_SIZE)

    # start off with undefined cell cell_type
    cell_type = 'U'


def build_encoded_map(input_file):
#    xy_namedtuple = namedtuple('index', ['x', 'y'])

    #global xy_namedtuple
    start_index = globals.xy_namedtuple(x=0, y=0)
    print('start_index', start_index)
#    matrix_size = xy_namedtuple(X_SIZE, Y_SIZE)

    field_matrix = [['0' for x in range(matrix_size.x)] for y in range(matrix_size.y)]

# ERROR
#     try:
#        with open(input_file) as inf:
#             for j in range(matrix_size.y):
#                 map_line = inf.readline().strip()
#                 print(map_line, end='\n')
#                 for i in range(matrix_size.y):
#                     field_matrix[i][j] = map_line[i]
#                     print(field_matrix[i][j])
#     except FileNotFoundError:head_of_chain_cell
#         print('The data file is missing')

# with
    for j in range(matrix_size.y):
        if j == 0: object_line = "XXXXX"
        if j == 1: object_line = "X.&.X"
        if j == 2: object_line = "X...X"
        if j == 3: object_line = "o..~X"
        if j == 4: object_line = "XXXoX"
        for i in range(matrix_size.x):
            field_matrix[i][j] = object_line[i]

    cell = namedtuple('direction', ['location', 'cell_type', 'valid', 'time_step', 'final'])

    # Index over all cells from the input map matrix that hold the maps cell types.
    # Build up the surrounding cells (N, S, E, W) for the robot's surrounding when a
    # direction is selected.

    cell_x = 0
    cell_y = 0

    for cell_y in range(matrix_size.y):
        for cell_x in range(matrix_size.x):
            c = data_single_cell()
            c.x = cell_x
            c.y = cell_y
            c.xy_key = (str(cell_x) + str(cell_y))
            c.cell_type = field_matrix[cell_x][cell_y] # get the single cell object type of master map of cell symbols
            if c.cell_type  == '.':  c.cell_time_to_enter = 1

            # set beginning of the doubly linked list to current cell in to be cell_dictionary
            if c.cell_type == '&':
                c.start_of_chain = True
                c.head_of_chain_cell = c.xy_key  # cell where the robot starts at
                c.header_prev_cell = None
                global current_location_of_robot
                current_location_of_robot = c.xy_key

            # encode the master list of symbols into the cell dictionary
            if (cell_x == matrix_size.x - 1):
                E = cell(cell_type='U', location='U', valid=False, time_step=0, final=False)
            elif (cell_x <= matrix_size.x - 1):
                E = cell(cell_type=field_matrix[cell_x + 1][cell_y], location=(str(cell_x + 1) + str(cell_y)), valid=True, time_step=1, final=False)

            if (cell_x == 0):
                W = cell(cell_type='U', location='U',  valid=False, time_step=0, final=False)
            elif (cell_x <= matrix_size.x - 1):
                W = cell(cell_type=field_matrix[cell_x - 1][cell_y], location=(str(cell_x -1) + str(cell_y)), valid=True, time_step=1, final=False)

            if (cell_y == 0):
                N = cell(cell_type='U', location='U',  valid=False, time_step=0, final=False)
            elif (cell_y <= matrix_size.y - 1):
                N = cell(cell_type=field_matrix[cell_x][cell_y - 1], location=(str(cell_x) + str(cell_y - 1)), valid=True, time_step=1, final=False)

            if (cell_y == matrix_size.y - 1):
                S = cell(cell_type='U', location='U', valid=False, time_step=0, final=False)
            elif (cell_y <= matrix_size.y - 1):
                S = cell(cell_type=field_matrix[cell_x][cell_y + 1], location=(str(cell_x) + str(cell_y + 1)), valid=True, time_step=1, final=False)

            # if the robot '&' is in a cell direction then replace with a good valid cell '.'
            if (E.cell_type == '&'): E = cell(cell_type='.', location=E.location, valid=True, time_step=1, final=False)
            if (W.cell_type == '&'): W = cell(cell_type='.', location=W.location, valid=True, time_step=1, final=False)
            if (N.cell_type == '&'): N = cell(cell_type='.', location=N.location, valid=True, time_step=1, final=False)
            if (S.cell_type == '&'): S = cell(cell_type='.', location=S.location, valid=True, time_step=1, final=False)

            # if the cell is '~' then set time_step=3
            if (E.cell_type == '~'): E = cell(cell_type='~', location=E.location, valid=True, time_step=3, final=False)
            if (W.cell_type == '~'): W = cell(cell_type='~', location=W.location, valid=True, time_step=3, final=False)
            if (N.cell_type == '~'): N = cell(cell_type='~', location=N.location, valid=True, time_step=3, final=False)
            if (S.cell_type == '~'): S = cell(cell_type='~', location=S.location, valid=True, time_step=3, final=False)

            # if the cell is final 'O' then set final to True
            if (E.cell_type == 'O'): E = cell(cell_type='O', location=E.location, valid=True, time_step=1, final=True)
            if (W.cell_type == 'O'): W = cell(cell_type='O', location=W.location, valid=True, time_step=1, final=True)
            if (N.cell_type == 'O'): N = cell(cell_type='O', location=N.location, valid=True, time_step=1, final=True)
            if (S.cell_type == 'O'): S = cell(cell_type='O', location=S.location, valid=True, time_step=1, final=True)

            # add cell_time_to_enter to class data_single_cell
            if c.cell_type == '.':  c.cell_time_to_enter = 1
            if c.cell_type == 'O':  c.cell_time_to_enter = 1
            if c.cell_type == '~':  c.cell_time_to_enter = 3


            # update a single cell entry of class c (data)
            c.E = E
            c.W = W
            c.N = N
            c.S = S

            # add new class to dictionary
            cell_dictionary[c.xy_key] = c

    for y in range(matrix_size.y):
        for x in range(matrix_size.x):
            cc = cell_dictionary[str(x) + str(y)]
            print(cc.x, cc.y, cc.cell_type)
            print('\t' + 'N= ' + cc.N.cell_type + '  ' + cc.N.location)
            print('\t' + 'S= ' + cc.S.cell_type + '  ' + cc.S.location)
            print('\t' + 'E= ' + cc.E.cell_type + '  ' + cc.E.location)
            print('\t' + 'W= ' + cc.W.cell_type + '  ' + cc.W.location)

if __name__ == '__main__':
    build_encoded_map('../input/0.txt')