#   Filename:       sort.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           October 04, 2018
#   Description:    sort images into respective directory
#
#   Copyright (c) 2018 Samantha Emily-Rachel Belnavis

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
import cv2
import numpy as np

from color_extractor import ImageToColor


class Sort:
    IMAGE_SOURCE_DIR = './imageset/train_set'
    settings = {'rows': 299, 'crop': 1}
    @staticmethod
    def get_root():
        print(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        npz = np.load('./preprocess/color_names.npz')
        image_to_colour = ImageToColor(npz['samples'], npz['labels'],self.settings)

        files = os.listdir(self.IMAGE_SOURCE_DIR)
        for file in files:
            # noinspection PyUnresolvedReferences
            img = cv2.imread(file)
            print(image_to_colour.get(img))
