#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Filename:       download.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           July 14, 2018
#   Description:    Downloads a set of basic colour swatches

import os
from Spinner import Spinner
from sys import stdout as stdout


class Download():
    def __init__(self):
        stdout.write("{:<40}".format("Downloading Imageset..."))
        Spinner().start()
        # pylint: disable=line-too-long
        os.system('wget -qO imageset.zip https://chryseplanitia.nyc3.cdn.digitaloceanspaces.com/colourvision_imageset.zip')
        # pylint: enable=line-too-long
        Spinner().stop()
        stdout.write('\b     [Done]')
        stdout.write("\n")
        stdout.flush()

        stdout.write("{:<40}".format("Extracting Imageset..."))
        Spinner().start()
        os.system('unzip -qq imageset.zip')
        Spinner().stop()
        stdout.write('\b     [Done]')
        stdout.write("\n")
        stdout.flush()
