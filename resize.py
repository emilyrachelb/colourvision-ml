import os
from PIL import Image

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