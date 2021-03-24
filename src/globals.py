#!/usr/bin/env python3

'''
    Name: globals.py
    Author: Christine Desire Davis
    Date: 11 Mar 2021
'''

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
original_robot_location = 00
input_map_filename = ''
run_in_pycharm = False
