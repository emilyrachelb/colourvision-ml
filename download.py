#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Filename:       download.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           July 14, 2018
#   Description:    Downloads a set of basic colour swatches

import os
from PIL import Image

# create file counter to show download progress
fileCounter = 1

redFileCount = 6384
redFileCounter = 1

orangeFileCount = 7314
orangeFileCounter = 1

yellowFileCount = 8301
yellowFileCounter = 1

greenFileCount = 8840
greenFileCounter = 1

blueFileCount = 4410
blueFileCounter = 1

purpleFileCount = 1686
purpleFileCounter = 1

greyFileCount = 2843
greyFileCounter = 1

whiteFileCount = 2927
whiteFileCounter = 1

blackFileCount = 3925
blackFileCounter = 1

brownFileCount = 2095
brownFileCounter = 1

totalFileCount = redFileCount + orangeFileCount + yellowFileCount + greenFileCount + blueFileCount + purpleFileCount + greyFileCount + +whiteFileCount + blackFileCount + brownFileCount

# Location for all the urls where the files go
# Image sources are all from the image-net.org synsets
redImageList = './colourlists/old/red.txt'
orangeImageList = './colourlists/old/orange.txt'
yellowImageList = './colourlists/old/yellow.txt'
greenImageList = './colourlists/old/green.txt'
blueImageList = './colourlists/old/blue.txt'
purpleImageList = './colourlists/old/purple.txt'
greyImageList = './colourlists/old/grey.txt'
whiteImageList = './colourlists/old/white.txt'
blackImageList = './colourlists/old/black.txt'
brownImageList = './colourlists/old/brown.txt'

def createDirectories():
    os.system('mkdir -p imageset/red')
    os.system('mkdir -p imageset/orange')
    os.system('mkdir -p imageset/yellow')
    os.system('mkdir -p imageset/green')
    os.system('mkdir -p imageset/blue')
    os.system('mkdir -p imageset/purple')
    os.system('mkdir -p imageset/grey')
    os.system('mkdir -p imageset/white')
    os.system('mkdir -p imageset/black')
    os.system('mkdir -p imageset/brown')


# check if an existing imageset directory exists. if it does,
# delete and create new empty directories in their place
if (os.path.exists('./imageset') == True):
    print("An imageset directory already exists! It will be deleted "
          "and replaced with an EMPTY directory")
    os.system('rm -rf ./imageset')
    createDirectories()
else:
    print("Creating imageset directory...")
    createDirectories()

# download all the images
print("Starting imageset download")

with open(redImageList, 'r') as f:
    for line in f:
        os.system("wget --timeout=10 -q -O imageset/red/red-{}.jpg {}".format(redFileCounter, line))
        print("Got file {} of {} in the red image set".format(redFileCounter, redFileCount))
        print("Files downloaded: {} of {}\n".format(fileCounter, totalFileCount))
        redFileCounter += 1
        fileCounter += 1

with open(orangeImageList, 'r') as f:
    for line in f:
        os.system("wget --timeout=10 -q -O imageset/orange/orange-{}.jpg {}".format(orangeFileCounter, line))
        print("Got file {} of {} in the orange image set".format(orangeFileCounter, orangeFileCount))
        print("Files downloaded: {} of {}\n".format(fileCounter, totalFileCount))
        orangeFileCounter += 1
        fileCounter += 1

with open(yellowImageList, 'r') as f:
    for line in f:
        os.system("wget --timeout=10 -q -O imageset/yellow/yellow-{}.jpg {}".format(yellowFileCounter, line))
        print("Got file {} of {} in the yellow image set".format(yellowFileCounter, yellowFileCount))
        print("Files downloaded: {} of {}\n".format(fileCounter, totalFileCount))
        yellowFileCounter += 1
        fileCounter += 1

with open(greenImageList, 'r') as f:
    for line in f:
        os.system("wget --timeout=10 -q -O imageset/green/green-{}.jpg {}".format(greenFileCounter, line))
        print("Got file {} of {} in the green image set".format(greenFileCounter, greenFileCount))
        print("Files downloaded: {} of {}\n".format(fileCounter, totalFileCount))
        greenFileCounter += 1
        fileCounter += 1

with open(blueImageList, 'r') as f:
    for line in f:
        os.system("wget --timeout=10 -q -O imageset/blue/blue-{}.jpg {}".format(blueFileCounter, line))
        print("Got file {} of {} in the blue image set".format(blueFileCounter, blueFileCount))
        print("Files downloaded: {} of {}\n".format(fileCounter, totalFileCount))
        blueFileCounter += 1
        fileCounter += 1

with open(purpleImageList, 'r') as f:
    for line in f:
        os.system("wget --timeout=10 -q -O imageset/purple/purple-{}.jpg {}".format(purpleFileCounter, line))
        print("Got file {} of {} in the purple image set".format(purpleFileCounter, purpleFileCount))
        print("Files downloaded: {} of {}\n".format(fileCounter, totalFileCount))
        purpleFileCounter += 1

with open(greyImageList, 'r') as f:
    for line in f:
        os.system("wget --timeout=10 -q -O imageset/grey/grey-{}.jpg {}".format(greyFileCounter, line))
        print("Got file {} of {} in the grey image set".format(greyFileCounter, greyFileCount))
        print("Files downloaded: {} of {}\n".format(fileCounter, totalFileCount))
        greyFileCounter += 1
        fileCounter += 1

with open(whiteImageList, 'r') as f:
    for line in f:
        os.system("wget --timeout=10 -q -O imageset/white/white-{}.jpg {}".format(whiteFileCounter, line))
        print("Got file {} of {} in the white image set".format(whiteFileCounter, whiteFileCount))
        print("Files downloaded: {} of {}\n".format(fileCounter, totalFileCount))
        whiteFileCounter += 1
        fileCounter += 1

with open(blackImageList, 'r') as f:
    for line in f:
        os.system("wget --timeout=10 -q -O imageset/black/black-{}.jpg {}".format(blackFileCounter, line))
        print("Got file {} of {} in the black image set".format(blackFileCounter, blackFileCount))
        print("Files downloaded: {} of {}\n".format(fileCounter, totalFileCount))
        blackFileCounter += 1
        fileCounter += 1

with open(brownImageList, 'r') as f:
    for line in f:
        os.system("wget --timeout=10 -q -O imageset/brown/brown-{}.jpg {}".format(brownFileCounter, line))
        print("Got file {} of {} in the brown image set".format(brownFileCounter, brownFileCount))
        print("Files downloaded: {} of {}\n".format(fileCounter, totalFileCount))
        brownFileCounter += 1
        fileCounter += 1

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

# Resize images
os.system('clear')
print("Resizing Images. This will take a while...")

# Resize images
for root, subdirs, files in os.walk('./imageset'):
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
            print(os.path.join(root, file))
            filename = os.path.join(root, file)
            img = Image.open(filename)
            img = img.resize([299, 299], Image.ANTIALIAS)

print("Program Finished! You may start the model training process now.")

print("Program Finished! You may start the model training process now.")