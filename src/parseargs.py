# pparseargs.py

import argparse
import sys

input_map_filename = ''

parser = argparse.ArgumentParser(
    prog='Determine Robot Path',
    description='''this description was indented weird but that is okay''',
    epilog='''
            likewise for this epilog whose whitespace will
        be cleaned up and whose words will be wrapped
        across a couple lines''')


def parse_the_command_line_attrubutes():

    my_parser = argparse.ArgumentParser(description='Determine shortest path for robot to its destination')
    my_parser.add_argument('--inputfilename', dest='input_file_name', action='store', required=True,
                            help='Enter the input map file name.')
    args = parser.parse_args()
    print(vars(args))

    my_parser.parse_args(['--inputfilename3'])

    if args.inputfilename:
        input_map_filename = args.inputfilename
    else:
        print('Error, no map filename exists')
        sys.exit()



if __name__ == '__main__':
    parse_the_command_line_attrubutes()
    print("input_map_filename", input_map_filename)