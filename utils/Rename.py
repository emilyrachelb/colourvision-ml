#   Filename:       rename.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           October 02, 2018
#   Description:    Renames the files in the imageset directory
#
#   Copyright (c) 2017 - 2018 emily

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
from sys import stdout as stdout
from frameworking.Spinner import Spinner


class Rename:
    DIRECTORY = [
        './imageset/blue',
        './imageset/brown',
        './imageset/green',
        './imageset/grey',
        './imageset/orange',
        './imageset/purple',
        './imageset/red',
        './imageset/yellow'
    ]

    spinner = Spinner()

    def __init__(self):
        for x in range(0, len(self.DIRECTORY)):
            working_directory = self.DIRECTORY[x]
            files = os.listdir(working_directory)
            # files = [f.lower() for f in files]
            # files = sorted(files)

            # initialize file counter
            file_num = 1

            stdout.write("Renaming Files in {:<17}...    ".format(working_directory))
            self.spinner.start()

            for file in files:
                os.system('mv {}/{} {}/image{}.jpg'.format(working_directory, file, working_directory, file_num))
                file_num = file_num + 1

            self.spinner.stop()
            stdout.write('\b     [Done]')
            stdout.write("\n")
            stdout.flush()
