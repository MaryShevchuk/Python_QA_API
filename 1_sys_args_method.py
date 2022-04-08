import argparse

parser = argparse.ArgumentParser()

"""
Все параметры для add_argument
name or flags - either a name or a list of option string, e.g. foo or -f, --f
action - the basic  type of action to be taken when this argument is encountered at the command line 
nargs - the number of command-line arguments that should be consumed 
const - a constant value required by some actionand nargs selection 
default - the value produced if the argument is absent from the command line 
type - the type to which the command-line argument should be converted 
choices - a container of the allowable values for the argument
required -  whether or not the command-line option may be omitted (optionals only)
help - a brief description of what the argument does 
metavar - a name for the argument in usage messages
dest - the name of the attribute to be added to the object returned by parse_args()
 
"""

parser.add_argument('--method', '-m', action='store',
                    help='Method to make request',
                    default='GET')

parser.add_argument('--url', 'u', action='store',
                    help='Url to make request to',
                    required=True)

parser.add_argument('--save', '-s',
                    action='append_const',
                    const='const_to_save',
                    dest='const_collection',
                    default=[],
                    help='Store params in list',
                    required=False)

parser.add_argument('--save2', '-s2',
                    action='append_const',
                    const='const_to_save',
                    dest='const_collection',
                    default=[],
                    help='Store params in list',
                    required=False)

args =parser.parse_args()
print(args) #Словарь с аргументами

#Парсим все что положили
args = parser.parse_args()

#Это словарь из которого можно вытащить аргументы
print(args)