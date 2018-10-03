#   Filename:       run.py.py
#   Author:         emily
#   Date:           October 02, 2018
#   Description:    ML Model Generation
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

from FileCheck import FileCheck
from Rename import Rename
from Resize import Resize
from Download import Download
import os

Download()
FileCheck().verify()
FileCheck().remove()
Rename()
Resize()

os.system('python retrain.py '
          '--bottleneck_dir=bottlenecks '
          '--model_dir=inception '
          '--summaries_dir=training_summaries/long '
          '--output_graph=retrained_graph.pb '
          '--output_labels=retrained_labels.txt '
          '--image_dir=imageset/')

