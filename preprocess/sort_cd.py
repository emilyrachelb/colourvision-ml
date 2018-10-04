#   Filename:       get_originals.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           October 03, 2018
#   Description:    grabs the original image files
#
#   Copyright (c) 2017 - 2018 Samantha Emily-Rachel Belnavis

#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:

#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.

import os
from colormap import rgb2hex
from sys import stdout as stdout
from frameworking import Spinner

colour_dirs = [
    'black',
    'blue',
    'brown',
    'cyan',
    'dark_blue',
    'dark_brown',
    'dark_green',
    'dark_red',
    'dark_teal',
    'gold',
    'green',
    'light_blue',
    'light_green',
    'magenta',
    'maroon',
    'mustard',
    'navy_blue',
    'olive',
    'orange',
    'pink',
    'purple',
    'red',
    'sky_blue',
    'teal',
    'yellow'
]

with open('colourlist.txt', 'r') as list:
    for line in list:
        rgb_string = line[line.find("[")+1:line.find("]")]

        r_value = int(rgb_string.split(', ')[0])
        g_value = int(rgb_string.split(', ')[1])
        b_value = int(rgb_string.split("{}, {}, ".format(r_value, g_value))[1])
        hex_string = rgb2hex(r_value, g_value, b_value).strip('#')

        colour_name = line.split('] ')[1]
        colour_name = colour_name.replace(" ", "_")


        print(rgb_string)
        print(r_value)
        print(g_value)
        print(b_value)
        print(hex_string)
        print(colour_name)

