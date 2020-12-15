"""
Argument parser for configuring various IR handling options.  
"""

import argparse

import utils.argparse_extend as argparse_extend

# Argument parser
argparser = argparse.ArgumentParser(prog='ir/ir', 
                                    description='Load a vdp puzzle from an intermediate representation', 
                                    add_help=False)
# Hack around not being able to use help messages in both a parent and a child parser. Adding text as part of a 
# group description is retained when this parser is inherited by another.
_irgroup = argparser.add_argument_group('IR handling arguments')

_irgroup.add_argument('puzzle_folder_path', metavar='puzzlepath', 
                      type=lambda x: argparse_extend.dir_path_type(x, 'puzzlepath'), 
                      help='Folder containing IRs for training and candidate models')

# Optional arguments to configure IR loading
_irgroup.add_argument('--ir-config', choices=['UnaryGuardedConjunctive'], default='UnaryGuardedConjunctive', 
                      dest='ir_config', 
                      help='[Experts only] Configure loading VDP puzzle from IR')
# Other optional arguments
_irgroup.add_argument('--puzzlename', default=None, help='[Logging] Name of the puzzle. Same as puzzlepath by default.')

# TODO (high): add option and support to load ir filtered through a given file 
#  containing pre-approved objects and relations.
