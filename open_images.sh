#!/bin/bash

# create directories
mkdir -p open_images/train
mkdir -p open_images/validate
mkdir -p open_images/test

# get training images

aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_0.tar.gz open_images/train 
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_1.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_2.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_3.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_4.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_5.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_6.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_7.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_8.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_9.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_a.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_b.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_c.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_d.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_e.tar.gz open_images/train
aws s3 --no-sign-request cp s3://open-images-dataset/tar/train_f.tar.gz open_images/train

# get validation set
aws s3 --no-sign-request cp s3://open-images-dataset/tar/validation.tar.gz open_images/validate

# get test set
aws s3 --no-sign-request cp s3://open-images-dataset/tar/test.tar.gz open_images/test
