#!/usr/bin/env python3

'''
    Name: determinepath.py
    Author: Christine Desire Davis
    Date: 11 Mar 2021
'''


import random
import sys
from src.buildencodedmap import *
import src.globals

possible_good_valid_moves = []    # elements are N, S, E, W grid positions, in no particular order

class determine_possible_path_for_current_robot_cell_position():
    '''input the robot location node to test and select the next node to move to.'''
    def __init__(self, cell_node_to_test):
        self.cell_node_to_test = cell_node_to_test

    def find_valid_possible_move(self):
        possible_good_valid_moves = []

        if src.globals.cell_dictionary[self.cell_node_to_test].N.cell_type in ('.', '~', 'O'):
            possible_good_valid_moves.append(src.globals.cell_dictionary[self.cell_node_to_test].N.location)

        if src.globals.cell_dictionary[self.cell_node_to_test].S.cell_type in ('.', '~', 'O'):
            possible_good_valid_moves.append(src.globals.cell_dictionary[self.cell_node_to_test].S.location)

        if src.globals.cell_dictionary[self.cell_node_to_test].E.cell_type in ('.', '~', 'O'):
            possible_good_valid_moves.append(src.globals.cell_dictionary[self.cell_node_to_test].E.location)

        if src.globals.cell_dictionary[self.cell_node_to_test].W.cell_type in ('.', '~', 'O'):
            possible_good_valid_moves.append(src.globals.cell_dictionary[self.cell_node_to_test].W.location)

        try:
            next_move = random.randint(0, len(possible_good_valid_moves)-1)
            move_robot_to_new_location = possible_good_valid_moves[next_move]
        except Exception as e:
            print(e)
            print('Exception Randint has no correct range')
            sys.exit()

        return move_robot_to_new_location


class update_linked_list_path_time_and_legnth():
    ''' Update linked list path and update time & length of chain. '''
    def __init__(self, new_location_to_move_to):
        self.new_location_to_move_to = new_location_to_move_to
        self.create_linked_list_between_robot_cell_and_new_cell()

    def create_linked_list_between_robot_cell_and_new_cell(self):
        src.globals.cell_dictionary[self.new_location_to_move_to].header_prev_cell = \
            src.globals.current_location_of_robot
        src.globals.cell_dictionary[src.globals.current_location_of_robot].header_next_cell = \
            self.new_location_to_move_to
        self.update_time_and_length_of_path()

    def update_time_and_length_of_path(self):
        src.globals.length_of_chain += 1
        if src.globals.cell_dictionary[self.new_location_to_move_to].cell_type == '~':
            src.globals.path_time += 3
        else:
            src.globals.path_time += 1



