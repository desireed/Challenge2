# globals.py

from collections import namedtuple

cell_dictionary = {}    # master dictionary of all cells
X_SIZE = 0
Y_SIZE = 0
current_location_of_robot = '00'
start_of_chain_cell = '00'   # linked list key of cell robot & starting position
length_of_chain = 0
path_time = 0
xy_namedtuple = namedtuple('index', ['x', 'y'])
list_of_power_outlets = []
