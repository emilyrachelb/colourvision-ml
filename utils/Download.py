#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Filename:       download.py
#   Author:         Samantha Emily-Rachel Belnavis
#   Date:           October 4, 2018
#   Description:    Downloads a set of basic colour swatches

import os
import tarfile

from six.moves import urllib

from sys import stdout as stdout


class Download:
    # pylint: disable=line-too-long
    IMAGESET_URL = 'https://chryseplanitia.nyc3.cdn.digitaloceanspaces.com/colourvision/archive/imageset_oct-4-2018.tar.gz'
    PRETRAIN_INCEPTION_V3 = 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz'
    # pylint: enable=line-too-long

    def download_and_extract_pretrained_model(self):
        dest_directory = './inception'
        if not os.path.exists(dest_directory):
            os.makedirs(dest_directory)
        filename = self.PRETRAIN_INCEPTION_V3
        filepath = os.path.join(dest_directory, filename)

        if not os.path.exists(filepath):
            def _progress(count, block_size, total_size):
                stdout.write('\r>> Downloading %s %s.1f%%' %
                             (filename, float(count * block_size) / float(total_size) * 100))
                stdout.flush
            filepath, _ = urllib.request.urlretrieve(self.PRETRAIN_INCEPTION_V3, filepath, _progress)


    def download_and_extract_imageset(self):
        dest_directory = './imagesets/unprocessed'
        if not os.path.exists(dest_directory):
            os.makedirs(dest_directory)
        filename = self.IMAGESET_URL.split('/')[-1]
        filepath = os.path.join(dest_directory, filename)

        if not os.path.exists(filepath):
            def _progress(count, block_size, total_size):
                stdout.write('\r>> Downloading %s %.1f%%' %
                             (filename, float(count * block_size) / float(total_size) * 100.0))

                stdout.flush()
            filepath, _ = urllib.request.urlretrieve(self.IMAGESET_URL, filepath, _progress)

            print()
            statinfo = os.stat(filepath)
            print('Successfully downloaded',  filename, statinfo.st_size, 'bytes.')

        tarfile.open(filepath, 'r:gz').extractall(dest_directory)
