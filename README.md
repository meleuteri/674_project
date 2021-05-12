# 674_project
project for cs674



# Requirements

Ubuntu >= 14.04

CUDA >= 10.1.243 

pytorch >= 1.7 (pytorch 1.8.1 + CUDA 11.X is unstable)

python >= 3.6

GCC >= 7.4.0


# Getting started

Use the command "python downloader.py -a --cleanup=True" to download and unzip all the data files into their required locations for the rest of the code

file MakeData.py turns the data from the unzipped folder of .txt files into a list of tuples, (scene, label)

file train.py tries to build a model and save its weights

Contributions:

Matthew Eleuteri:
All of MakeData.py, and train.py lines 39-61

Jerry Fu:
All of downloader.py

Sharon Shao:
