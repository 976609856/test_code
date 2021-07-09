# Script Name   : folder_size.py
# Author        : Craig Richards
# Version       : 1.0.1

# Modifications : Modified the Printing method and added a few comments

import os
import sys  # Load the library module and the sys module for the argument vector'''

try:
    directory = sys.argv[1]  # Set the variable directory to be the argument supplied by user.
except IndexError:
    sys.exit("Must provide an argument.")

dir_size = 0  # Set the size to 0
fsizedicr = {'Bytes': 1,
             'Kilobytes': float(1) / 1024,
             'Megabytes': float(1) / (1024 * 1024),
             'Gigabytes': float(1) / (1024 * 1024 * 1024)}
