#!/usr/bin/env python3

'''
    Name: parseargs.py
    Author: Christine Desire Davis
    Date: 11 Mar 2021
'''

import os
import sys
import platform
import argparse
import src.globals

ROOT_DIR = ''

def parse_the_command_line_attributes():

    my_parser = argparse.ArgumentParser(
        prog='Determine Robot Path',
        description=''' Program to move a robot from start to power outlets in least amount of time. ''')
    my_parser.add_argument('-i', dest='input_file_name', action='store', required=True,
                            help='Enter the input map file name.')
    my_parser.add_argument('-pc', dest='pycharm', help='Run the program in pycharm.', action='store_true')

    args = my_parser.parse_args()
    print(vars(args))

    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = ROOT_DIR.replace('src', '')

    if args.pycharm:
        src.globals.run_in_pycharm = True

    if args.input_file_name:
        if src.globals.run_in_pycharm:
            src.globals.input_map_filename = ROOT_DIR + r'input/' + args.input_file_name
        else:
            src.globals.input_map_filename = ROOT_DIR + r'input/' + args.input_file_name
    else:
        print('ERROR, no map filename exists')
        sys.exit()

    print("OS = '{}'".format(platform.system()))
    print("RootDir = '{}'".format(ROOT_DIR))
    print("input_map_filename", src.globals.input_map_filename)

if __name__ == '__main__':
    parse_the_command_line_attributes()
    print("input_map_filename", src.globals.input_map_filename)
