#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Filename:       download.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           July 14, 2018
#   Description:    Downloads a set of basic colour swatches

import os
from PIL import Image

totalFileCount = 28463
fileCounter = 0

redFileCount = 2687
redFileCounter = 1

orangeFileCount = 2604
orangeFileCounter = 1

yellowFileCount = 2573
yellowFileCounter = 1

greenFileCount = 2487
greenFileCounter = 1

blueFileCount = 3430
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

# Location for all the urls where the files go
# Image sources are all from the image-net.org synsets
redImageList = './colourlists/red.txt'
orangeImageList = './colourlists/orange.txt'
yellowImageList = './colourlists/yellow.txt'
greenImageList = './colourlists/green.txt'
blueImageList = './colourlists/blue.txt'
purpleImageList = './colourlists/purple.txt'
greyImageList = './colourlists/grey.txt'
whiteImageList = './colourlists/white.txt'
blackImageList = './colourlists/black.txt'
brownImageList = './colourlists/brown.txt'

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

# 'red' photos
with open(redImageList, 'r') as f:
    for line in f:
        os.system("wget -qO --timeout=10 imageset/red/red-{}.jpg {}".format(redFileCounter, line))
        print("Got file {} of {} in the red image set".format(redFileCounter, redFileCount))
        print("Files downloaded: {} of {}".format(fileCounter, totalFileCount))
        redFileCounter += 1
        fileCounter += 1

with open(orangeImageList, 'r') as f:
    for line in f:
        os.system("wget -qO --timeout=10  imageset/orange/orange-{}.jpg {}".format(orangeFileCounter, line))
        print("Got file {} of {} in the orange image set".format(orangeFileCounter, orangeFileCount))
        print("Files downloaded: {} of {}".format(fileCounter, totalFileCount))
        orangeFileCounter += 1
        fileCounter += 1

with open(yellowImageList, 'r') as f:
    for line in f:
        os.system("wget -qO --timeout=10  imageset/yellow/yellow-{}.jpg {}".format(yellowFileCounter, line))
        print("Got file {} of {} in the yellow image set".format(yellowFileCounter, yellowFileCount))
        print("Files downloaded: {} of {}".format(fileCounter, totalFileCount))
        yellowFileCounter += 1
        fileCounter += 1

with open(greenImageList, 'r') as f:
    for line in f:
        os.system("wget -qO --timeout=10  imageset/green/green-{}.jpg {}".format(greenFileCounter, line))
        print("Got file {} of {} in the green image set".format(greenFileCounter, greenFileCount))
        print("Files downloaded: {} of {}".format(fileCounter, totalFileCount))
        greenFileCounter += 1
        fileCounter += 1

with open(blueImageList, 'r') as f:
    for line in f:
        os.system("wget -qO --timeout=10  imageset/blue/blue-{}.jpg {}".format(blueFileCounter, line))
        print("Got file {} of {} in the blue image set".format(blueFileCounter, blueFileCount))
        print("Files downloaded: {} of {}".format(fileCounter, totalFileCount))
        blueFileCounter += 1
        fileCounter += 1

with open(purpleImageList, 'r') as f:
    for line in f:
        os.system("wget -qO --timeout=10  imageset/purple/purple-{}.jpg {}".format(purpleFileCounter, line))
        print("Got file {} of {} in the purple image set".format(purpleFileCounter, purpleFileCount))
        print("Files downloaded: {} of {}".format(fileCounter, totalFileCount))
        purpleFileCounter += 1

with open(greyImageList, 'r') as f:
    for line in f:
        os.system("wget -qO imageset/grey/grey-{}.jpg {}".format(greyFileCounter, line))
        print("Got file {} of {} in the grey image set".format(greyFileCounter, greyFileCount))
        print("Files downloaded: {} of {}".format(fileCounter, totalFileCount))
        greyFileCounter += 1
        fileCounter += 1

with open(whiteImageList, 'r') as f:
    for line in f:
        os.system("wget -qO --timeout=10  imageset/white/white-{}.jpg {}".format(whiteFileCounter, line))
        print("Got file {} of {} in the white image set".format(whiteFileCounter, whiteFileCount))
        print("Files downloaded: {} of {}".format(fileCounter, totalFileCount))
        whiteFileCounter += 1
        fileCounter += 1

with open(blackImageList, 'r') as f:
    for line in f:
        os.system("wget -qO --timeout=10  imageset/black/black-{}.jpg {}".format(blackFileCounter, line))
        print("Got file {} of {} in the black image set".format(blackFileCounter, blackFileCount))
        print("Files downloaded: {} of {}".format(fileCounter, totalFileCount))
        blackFileCounter += 1
        fileCounter += 1

with open(brownImageList, 'r') as f:
    for line in f:
        os.system("wget -qO --timeout=10  imageset/brown/brown-{}.jpg {}".format(brownFileCounter, line))
        print("Got file {} of {} in the brown image set".format(brownFileCounter, brownFileCount))
        print("Files downloaded: {} of {}".format(fileCounter, totalFileCount))
        brownFileCounter += 1
        fileCounter += 1

# Verify files
os.system('clear')
print("Verifying files. This may take a while...")
for filename in os.listdir('./imageset'):
    if filename.endswith('.jpg'):
        try:
            img = Image.open('./'+filename)
            img.verify()
        except (IOError, SyntaxError) as e:
            print('Bad file: ', filename)
            with open('bad_files.txt', 'a') as f:
                f.write(filename + '\n')
# Resize images
print("Resizing Images. This will take a while...")
for filename in os.listdir('./imageset'):
    if filename.endswith('.jpg'):
        img = Image.open(filename)
        img = img.resize([299, 299], Image.ANTIALIAS)

print("Program Finished! You may start the model training process now.")