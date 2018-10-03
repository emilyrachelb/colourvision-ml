#   Filename:       FileCheck.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           October 2, 2018
#   Description:    JPEG Validation and file cleanup

import os
from sys import stdout as stdout
from PIL import Image
from Spinner import Spinner
import warnings


# warning suppression
def warn(*args, **kwargs):
    pass
warnings.warn = warn


class FileCheck:

    @staticmethod
    def verify(self):
        stdout.write("{:<40}".format("Checking JPEG files..."))
        Spinner().start()

        for root, subdirs, files in os.walk('./imageset'):
            for file in files:
                if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
                    filename = os.path.join(root, file)
                    try:
                        img = Image.open('./' + filename)
                        img.verify()
                    except (IOError, SyntaxError) as e:
                        with open('bad_files.txt', 'a') as f:
                            f.write(filename + '\n')

        Spinner().stop()
        stdout.write('\b     [Done]')
        stdout.write("\n")
        stdout.flush()

    @staticmethod
    def remove(self):
        stdout.write("{:<40}".format("Removing Bad Files..."))
        Spinner().start()

        with open('bad_files.txt', 'r') as f:
            for line in f:
                os.system("rm {}".format(line))

        Spinner().stop()
        stdout.write('\b     [Done]')
        stdout.write("\n")
        stdout.flush()
