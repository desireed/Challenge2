from collections import namedtuple

# globals
cell_dictionary = {}    # master dictionary of all cells
X_SIZE = 5
Y_SIZE = 5
head_of_chain_cell = '00'   # dictionary key of cell
length_of_chain = 0

class data_single_cell:
    x = 0
    y = 0
    xy_key = ''
    head_of_chain = False
    tail_of_chain = False
    header_prev_cell = None  # Doubly linked list
    header_next_cell = None

    # start off with undefined cell cell_type
    cell_type = 'U'


def build_encoded_map(input_file):
    xy_namedtuple = namedtuple('index', ['x', 'y'])

    start_index = xy_namedtuple(x=0, y=0)

    matrix_size = xy_namedtuple(X_SIZE, Y_SIZE)

    field_matrix = [['0' for x in range(matrix_size.x)] for y in range(matrix_size.y)]

#     try:
#         with open('input/0.txt') as inf:
# #        with open(input_file) as inf:
#             for j in range(matrix_size.y):
#                 map_line = inf.readline().strip()
#                 print(map_line, end='\n')
#                 for i in range(matrix_size.y):
#                     field_matrix[i][j] = map_line[i]
#                     print(field_matrix[i][j])
#     except FileNotFoundError:head_of_chain_cell
#         print('The data file is missing')


    for j in range(matrix_size.y):
        if j == 0: object_line = "XXXXX"
        if j == 1: object_line = "X.&.X"
        if j == 2: object_line = "X...X"
        if j == 3: object_line = "o..~X"
        if j == 4: object_line = "XXXoX"
        for i in range(matrix_size.x):
            field_matrix[i][j] = object_line[i]

    cell = namedtuple('direction', ['cell_type', 'valid', 'time_step', 'final'])

    # Index over all cells frmo the input map matrix that hold the maps cell types.
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

            # set beginning of the doubly linked list
            if c.cell_type == '&':
                c.head_of_chain = True
                head_of_chain_cell = c.xy_key  # cell where the robot starts at

            # encode the master list of symbols into the cell dictionary
            if (cell_x == matrix_size.x - 1):
                E = cell(cell_type='U', valid=False, time_step=1, final=False)
            elif (cell_x <= matrix_size.x - 1):
                E = cell(cell_type=field_matrix[cell_x + 1][cell_y], valid=True, time_step=1, final=False)

            if (cell_x == 0):
                W = cell(cell_type='U', valid=False, time_step=0, final=False)
            elif (cell_x <= matrix_size.x - 1):
                W = cell(cell_type=field_matrix[cell_x - 1][cell_y], valid=True, time_step=1, final=False)

            if (cell_y == 0):
                N = cell(cell_type='U', valid=False, time_step=0, final=False)
            elif (cell_y <= matrix_size.y - 1):
                N = cell(cell_type=field_matrix[cell_x][cell_y - 1], valid=True, time_step=1, final=False)

            if (cell_y == matrix_size.y - 1):
                S = cell(cell_type='U', valid=False, time_step=0, final=False)
            elif (cell_y <= matrix_size.y - 1):
                S = cell(cell_type=field_matrix[cell_x][cell_y + 1], valid=True, time_step=1, final=False)

            # if the robot '&' is in a cell direction then replace with a good valid cell '.'
            if (E.cell_type == '&'): E = cell(cell_type='.', valid=True, time_step=1, final=False)
            if (W.cell_type == '&'): W = cell(cell_type='.', valid=True, time_step=1, final=False)
            if (N.cell_type == '&'): N = cell(cell_type='.', valid=True, time_step=1, final=False)
            if (S.cell_type == '&'): S = cell(cell_type='.', valid=True, time_step=1, final=False)

            # if the cell is '~' then set time_step=3
            if (E.cell_type == '~'): E = cell(cell_type='~', valid=True, time_step=3, final=False)
            if (W.cell_type == '~'): W = cell(cell_type='~', valid=True, time_step=3, final=False)
            if (N.cell_type == '~'): N = cell(cell_type='~', valid=True, time_step=3, final=False)
            if (S.cell_type == '~'): S = cell(cell_type='~', valid=True, time_step=3, final=False)

            # if the cell is final 'O' then set final to True
            if (E.cell_type == 'O'): E = cell(cell_type='O', valid=True, time_step=1, final=True)
            if (W.cell_type == 'O'): W = cell(cell_type='O', valid=True, time_step=1, final=True)
            if (N.cell_type == 'O'): N = cell(cell_type='O', valid=True, time_step=1, final=True)
            if (S.cell_type == 'O'): S = cell(cell_type='O', valid=True, time_step=1, final=True)

            # update a single cell entry of class c (data)
            c.E = E
            c.W = W
            c.N = N
            c.S = S

            # add new class to dictionary
            cell_dictionary[str(c.x) + str(c.y)] = c

    for y in range(matrix_size.y):
        for x in range(matrix_size.x):
            cc = cell_dictionary[str(x) + str(y)]
            print(cc.x, cc.y, cc.cell_type)
            print('\t' + 'N= ' + cc.N.cell_type)
            print('\t' + 'S= ' + cc.S.cell_type)
            print('\t' + 'E= ' + cc.E.cell_type)
            print('\t' + 'W= ' + cc.W.cell_type)

if __name__ == '__main__':
    build_encoded_map('../input/0.txt')