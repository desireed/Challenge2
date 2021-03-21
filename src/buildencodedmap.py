# buildencodedmap.py

from collections import namedtuple
import sys
import src.globals

matrix_size = src.globals.xy_namedtuple(src.globals.X_SIZE, src.globals.Y_SIZE)
print_once = True

# The class structure which is used for each coordinate no the map
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
    cell_type = 'U'


def build_encoded_map(input_file):

    # Get the map from the input file
    try:
        with open(input_file) as inf:
            lines = inf.readlines()

            i = 0
            j = 0
            linesfixed = []
            for line in lines:
                line = line.strip()
                linesfixed.append(line.split(' '))
            src.globals.X_SIZE = len(line)
            src.globals.Y_SIZE = len(linesfixed)

            field_matrix = [['0' for x in range(0, src.globals.Y_SIZE)] for y in range(0, src.globals.X_SIZE)]

            while j < src.globals.Y_SIZE:
                i = 0
                line = linesfixed[j]
                src.globals.Y_SIZE = len(linesfixed)
                src.globals.X_SIZE = len(line)
                while i < src.globals.X_SIZE:
                    field_matrix[i][j] = line[i]
                    i += 1
                j += 1

            global print_once
            if print_once:
                print("START", flush=True)
                for row in linesfixed:
                    print(row, flush=True)
                print("END", flush=True)
                print_once = False

    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

    cell = namedtuple('direction', ['location', 'cell_type', 'valid', 'time_step', 'final'])

    matrix_size = src.globals.xy_namedtuple(src.globals.X_SIZE, src.globals.Y_SIZE)

    # Index over all cells from the input map matrix that hold the maps cell types.
    # Build up the surrounding cells (N, S, E, W) for the robot's surrounding when a
    # direction is selected.

    cell_x = 0
    cell_y = 0
    robot_found = False

    # start filling out the map cell contents with neighboring data
    for cell_y in range(matrix_size.y):
        for cell_x in range(matrix_size.x):
            c = data_single_cell()
            c.x = cell_x
            c.y = cell_y
            c.xy_key = (str(cell_x) + str(cell_y))
            c.cell_type = field_matrix[cell_x][cell_y] # get the single cell object type of master map of cell symbols

            # set beginning of the doubly linked list to current cell in to be cell_dictionary
            if c.cell_type == '&':
                c.start_of_chain = True
                c.head_of_chain_cell = c.xy_key  # cell where the robot starts at
                c.header_prev_cell = None
                src.globals.current_location_of_robot = c.xy_key
                robot_found = True

            # Build list of power outlets from the map
            if c.cell_type == 'O':
                src.globals.list_of_power_outlets.append(c.xy_key)

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

            # add cell_time_to_enter the class data_single_cell valid path
            if c.cell_type == '.':  c.cell_time_to_enter = 1
            # if c.cell_type == 'O':  c.cell_time_to_enter = 1
            # if c.cell_type == '~':  c.cell_time_to_enter = 3


            # update a single cell class entry of class c (data)
            c.E = E
            c.W = W
            c.N = N
            c.S = S

            # add new class to dictionary
            src.globals.cell_dictionary[c.xy_key] = c

    # After the list of power outlets have been collected
    # remove any power outlet that is trapped by an X or U on all sides N,S,E,W
    to_remove = []
    length_list_of_power_outlets = len(src.globals.list_of_power_outlets)
    for i in range(len(src.globals.list_of_power_outlets)):
        c = src.globals.cell_dictionary[src.globals.list_of_power_outlets[i]]
        if (((c.N.cell_type == 'X') | (c.N.cell_type == 'U')) &
                ((c.S.cell_type == 'X') | (c.S.cell_type == 'U') )&
                ((c.E.cell_type == 'X') | (c.E.cell_type == 'U') )&
                ((c.W.cell_type == 'X') | (c.W.cell_type == 'U'))):
            to_remove.append(c.xy_key)
    for i in range(len(to_remove)):
        src.globals.list_of_power_outlets.remove(to_remove[i])
        removed = (to_remove[i])
        print('Removed invalid "O" location {} because it is trapped on NSEW directions.'.format(to_remove[i]))

    for y in range(matrix_size.y):
        for x in range(matrix_size.x):
            cc = src.globals.cell_dictionary[str(x) + str(y)]
            print(cc.x, cc.y, cc.cell_type)
            print('\t' + 'N= ' + cc.N.cell_type + '  ' + cc.N.location)
            print('\t' + 'S= ' + cc.S.cell_type + '  ' + cc.S.location)
            print('\t' + 'E= ' + cc.E.cell_type + '  ' + cc.E.location)
            print('\t' + 'W= ' + cc.W.cell_type + '  ' + cc.W.location)

    if src.globals.list_of_power_outlets is None:
        assert('ERROR: No power outlets found in map.')
        raise

    if not robot_found:
        assert('ERROR: No robot found in map.')
        raise