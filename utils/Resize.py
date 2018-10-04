import os
from utils.Spinner import Spinner
from sys import stdout as stdout


class Resize:
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

    def __init__(self):
        stdout.write("{:<40}".format("Resizing Images..."))
        self.spinner.start()
        for x in range(0, len(self.DIRECTORY)):
            working_directory = self.DIRECTORY[x]
            files = os.listdir(working_directory)

            for file in files:
                os.system('mogrify -resize 299x299 {}/{}'.format(working_directory, file))

        self.spinner.stop()
        stdout.write('\b     [Done]')
        stdout.write('\n')
        stdout.flush()
