#   Filename:       remove_badfiles.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           July 19, 2018
#   Description:    This program removes the images
#                   in the list bad files from the imageset directory

import os

with open('bad_files.txt', 'r') as f:
    for line in f:
        os.system("rm {}".format(line))