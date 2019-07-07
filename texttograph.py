import csv
import os
import matplotlib.pyplot as plt
import numpy as np 

readers = []
points = []

def openfile(filename):
    textread = open(filename, "r")
    reader = []
    for row in textread:
        reader.append(round(float(row), 3))
    return reader

def one(files):
    plt.plot(points[0],readers[0],'ro')
    plt.axis([0, len(readers[0]), -10, 10])
    plt.title(os.path.basename(files[0]))

def two(files):
    plt.subplot(121)
    plt.plot(points[0],readers[0],'ro')
    plt.axis([0, len(readers[0]), -0.1, 0.1])
    plt.title(os.path.basename(files[0]))

    plt.subplot(122)
    plt.plot(points[1],readers[1],'ro')
    plt.axis([0, len(readers[1]), -0.2, 0.2])
    plt.title(os.path.basename(files[1]))

def three():
    print("Not implemented")

options = { 1 : one, 
            2 : two,
            3 : three,
}

def plotfiles(files):

    for singlefile in files: 
        reader = openfile(singlefile)
        readers.append(reader)
        p = list(range(len(reader)))
        points.append(p)
    
    plt.figure(1)
    options[len(files)](files)
    plt.show()




 