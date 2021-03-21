# main.py
'''Must have pip install parameterixed import installed
    and pytest & pytest-html '''



from collections import defaultdict
from collections import namedtuple
import argparse
import sys
import time
import src.globals
import src.buildencodedmap
from src.determinepath import *

number_epochs = 0
max_number_epochs = 100
max_path_length = 200
named_tuple_list_of_power_outlets = namedtuple("index", ["location", "time", "length"])
list_of_power_outlets = []
power_dictionary_statistics = defaultdict(list)


def report_statistics():
    ''' Report the lowest time entries for each power outlet. '''
    # print(power_dictionary_statistics)
    for key, value in power_dictionary_statistics.items():
        sorted_values = sorted(value)
        #print('KEY={}   VALUE= {}'.format(key, sorted_values))
        li = sorted_values[0]
        time = li[0]
        print("({}, {})".format(key, time))

def parse_the_command_line_attrubutes():
    ''' Parse the command line for the map file. '''
    my_parser = argparse.ArgumentParser(
        prog='Determine Robot Path',
        description='''Determine shortest path for robot to its destinations.''')

    my_parser.add_argument('-i', required=True, dest='input_file_name', action='store',
                            help='Enter the input map file name.')
    args = my_parser.parse_args()
    return args.input_file_name


def main_program():
    input_map_file = parse_the_command_line_attrubutes()

    epochs_completed = False

    build_encoded_map(r'../input/' + input_map_file)

    while not epochs_completed:
        global number_epochs
        number_epochs = 0
        src.globals.path_time = 0
        src.globals.length_of_chain = 0
        path_length = 0
        while True: # not simulation_run_completed:
            number_epochs += 1
            path_length += 1

            c = determine_possible_path_for_current_robot_cell_position(src.globals.current_location_of_robot)
            new_location_to_move_to = c.find_valid_possible_move()
            update_linked_list_path_time_and_legnth(new_location_to_move_to)
            src.globals.current_location_of_robot = new_location_to_move_to

            if number_epochs == max_number_epochs:
                epochs_completed = True
                break
            elif src.globals.cell_dictionary[src.globals.current_location_of_robot].cell_type == 'O':
                src.globals.simulation_completed_valid = True
                power_dictionary_statistics[src.globals.current_location_of_robot].append([src.globals.path_time])
                break
            elif path_length == max_path_length:
                print("Max Number Path Lenghts met", flush=True)
                break

        if epochs_completed: # | globals.simulation_completed_valid  | path_length == max_path_length:
            epochs_completed = True

    report_statistics()

if __name__ == '__main__':
    main_program()