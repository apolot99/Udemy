#           PYTHON 2 VERSUS PYTHON 3
# 99% of external packages that you download support python 3 and some are made exclusively for python 3 e.g django for web dev't
# If you know python 3, you already know python 2. You just need to learn a few syntax changes.

#           COMMAND LINE BASICS
# The command line allows you to programmatically move through your computer's directories.
#  cd-find your current directory
#  dir-list all files in a directory
#  cd (name of a folder)-if I want to move into a specific folder
#  cd .. - if I want to move up a directory
#  cls-clear entire command line screen
# Hidden files in a directory are denoted starting off with a dot

#           INSTALLING PYTHON
# Advantages of using python
#  -ability to learn it quickly
#  -involves less code
#  -syntax is easier to read(uses indentation instead of curly braces)
#  -utilized by every major technology company
#  -huge amount of open source libraries
#  -has standard libraries included
# Anaconda distribution includes python as well as many other useful libraries like jupiter
# Anaconda can be installed onto any major operationg system
# Types of environments (where you're gonna type your python code)
#  -Text Editors
#  -Full IDEs (Intergrated Developement Environment); designed specifically for python e.g PyCharm & Spyder
#  -Notebook environments (runs code on a cell based system)

#          GIT AND GITHUB OVERVIEW
# Github is a website where you can publish your git repositories and collaborate with other developers
# snapshots of your code on Github are known as commits

#         PYTHON DATA TYPES
# -Integers (whole numbers)
# -Floating point (whole numbers with decimals)
# -Strings (syntax of characters using either single or double quotes e.g "hello world")
# -Lists (ordered sequences that can hold a variety of object types. It is defined by square brackets and every object separated by comma.)
# -Dictionaries (unordered mappings for stroing objects using a key value paring)
# -Tuples (similar to strings but can not be changed. They use parenthesis)
# -Sets
# -Booleans (operators that allow you to convey either true or false)

# use the mod opeartor(%) to find out the remainder from dividing.
# If mod 2 results in anything other than zero then that number is odd.

#  RULES FOR CHOOSING VARIABLE NAMES IN PYTHON
#    -names can't start with a number
#    -there can be no spaces in the name instead use under score
#    -can't use any of these signs ("",<>/?|\!@#$%^&*~-+)
#    -names should be lower case
#    -avoid using words that have special meaning in python like 'list','str'

# python uses dynamic typing whihc means you can reassign varibales to different data types

# Indexing means when you want to grab a single character form a string
# indexing notation uses [] after the string
# Every single character has an index assignes to it
# Indexing starts at zero
# Reverse indexing helps you grab the last letter of a string however long that string is by just grabbing negavtive one 

# slicing allows you to grab a subsection of multiple characters i.e a slice of a string
# slicing has the following syntax; [start:stop:step]
#   start-is a numerical index for the slice start
#   stop-is the index you will go up to but not include
#   step-is the size of the 'jump' you take 

#     PROPERTIES OF STRINGS
# -Can not mutate or change

# numbers in strings can not be added.

# String interpolation means sticking a varibale in to a string.

# float formatting with the .format method follows this {value:width.precision f}

# dictionaries follow this {'string key':'value'}

# Tuples are useful when you are passing objects in your program and you do not want them to be accidentally changed.
# They provide data integrity

# Sets are unordered collection sof unique elements; there can only be one representative of the same object

# append means to add more lines to the end of a text file.

# Permissions means to be able to either read or write to a file or both.

#     READ WRITING AND APPENDING MODES
# -mode = 'r' is read only
# -mode = 'w' is write only (will overwrite files or create new)
# -mode = 'a' is append only (will add on to files)
# -mode = 'r+' is reading and writing
# -mode = 'w+' is writing and reading (overwrites existing files or creates a new file)