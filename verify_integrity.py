#   Filename:       verify_integrity.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           July 19 2018
#   Description:    This program validates JPEG files and
#                   writes the name of invalid files to a list

import PIL
import os
from PIL import Image

# Verify files
os.system('clear')
print("Verifying files. This may take a while...")

for root, subdirs, files in os.walk('./imageset'):
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
            print(os.path.join(root, file))
            filename = os.path.join(root, file)
            try:
                img = Image.open('./' + filename)
                img.verify()
            except (IOError, SyntaxError) as e:
                print('Bad file: ', filename)
                with open('bad_files.txt', 'a') as f:
                    f.write(filename + '\n')
