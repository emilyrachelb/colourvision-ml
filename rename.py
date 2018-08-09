import os

black_dir = './imageset/black/'
blue_dir = './imageset/blue/'
brown_dir = './imageset/brown/'
green_dir = './imageset/green/'
grey_dir = './imageset/grey/'
orange_dir = './imageset/orange/'
purple_dir = './imageset/purple/'
red_dir = './imageset/red/'
white_dir = './imageset/white/'
yellow_dir = './imageset/yellow/'

blackCounter = 1
blueCounter = 1
brownCounter = 1
greenCounter = 1
greyCounter = 1
orangeCounter = 1
purpleCounter = 1
redCounter = 1
whiteCounter = 1
yellowCounter = 1

baseUrl = 'http://samantharachelb.nyc3.digitaloceanspaces.com/tensorflow-image-sets/colourvision-imageset/'

for file in os.listdir(black_dir):
    dst = "black-" + str(blackCounter) + ".jpg"
    src = black_dir + file
    dst = black_dir + dst

    blackCounter += 1

    os.rename(src, dst)

    dst = "black-" + str(blackCounter) + ".jpg"
    with open('colourlists/black.txt', 'a') as f:
        f.write(baseUrl + "black/" + dst + '\n')

for file in os.listdir(blue_dir):
    dst = "blue-" + str(blueCounter) + ".jpg"
    src = blue_dir + file
    dst = blue_dir + dst

    blueCounter += 1

    os.rename(src, dst)
    dst = "blue-" + str(blueCounter) + ".jpg"
    with open('colourlists/blue.txt', 'a') as f:
        f.write(baseUrl + "blue/" + dst + '\n')

for file in os.listdir(brown_dir):
    dst = "brown-" + str(brownCounter) + ".jpg"
    src = brown_dir + file
    dst = brown_dir + dst

    brownCounter += 1

    os.rename(src, dst)
    dst = "brown-" + str(brownCounter) + ".jpg"
    with open('colourlists/brown.txt', 'a') as f:
        f.write(baseUrl + "brown/" + dst + '\n')

for file in os.listdir(green_dir):
    dst = "green-" + str(greenCounter) + ".jpg"
    src = green_dir + file
    dst = green_dir + dst

    greenCounter += 1

    os.rename(src, dst)
    dst = "green-" + str(greenCounter) + ".jpg"
    with open('colourlists/green.txt', 'a') as f:
        f.write(baseUrl + "green/" + dst + '\n')

for file in os.listdir(grey_dir):
    dst = "grey-" + str(greyCounter) + ".jpg"
    src = grey_dir + file
    dst = grey_dir + dst

    greyCounter += 1

    os.rename(src, dst)
    dst = "grey-" + str(greyCounter) + ".jpg"
    with open('colourlists/grey.txt', 'a') as f:
        f.write(baseUrl + "grey/" + dst + '\n')

for file in os.listdir(orange_dir):
    dst = "orange-" + str(orangeCounter) + ".jpg"
    src = orange_dir + file
    dst = orange_dir + dst

    orangeCounter += 1

    os.rename(src, dst)
    dst = "orange-" + str(orangeCounter) + ".jpg"
    with open('colourlists/orange.txt', 'a') as f:
        f.write(baseUrl + "orange/" + dst + '\n')

for file in os.listdir(purple_dir):
    dst = "purple-" + str(purpleCounter) + ".jpg"
    src = purple_dir + file
    dst = purple_dir + dst

    purpleCounter += 1

    os.rename(src, dst)
    dst = "purple-" + str(purpleCounter) + ".jpg"
    with open('colourlists/purple.txt', 'a') as f:
        f.write(baseUrl + "purple/" + dst + '\n')

for file in os.listdir(red_dir):
    dst = "red-" + str(redCounter) + ".jpg"
    src = red_dir + file
    dst = red_dir + dst

    redCounter += 1

    os.rename(src, dst)
    dst = "red-" + str(redCounter) + ".jpg"
    with open('colourlists/red.txt', 'a') as f:
        f.write(baseUrl + "red/" + dst + '\n')

for file in os.listdir(white_dir):
    dst = "white-" + str(whiteCounter) + ".jpg"
    src = white_dir + file
    dst = white_dir + dst

    whiteCounter += 1

    os.rename(src, dst)

    dst = "white-" + str(whiteCounter) + ".jpg"

    with open('colourlists/white.txt', 'a') as f:
        f.write(baseUrl + "white/" + dst + '\n')

for file in os.listdir(yellow_dir):
    dst = "yellow-" + str(yellowCounter) + ".jpg"
    src = yellow_dir + file
    dst = yellow_dir + dst

    yellowCounter += 1

    os.rename(src, dst)

    dst = "yellow-" + str(yellowCounter) + ".jpg"

    with open('colourlists/yellow.txt', 'a') as f:
        f.write(baseUrl + "yellow/" + dst + '\n')