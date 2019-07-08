import csv
import os
import matplotlib.pyplot as plt
import numpy as np 

readers = []
points = []
deltaminmax = 10


def openfile(filename):
    textread = open(filename, "r")
    reader = []
    for row in textread:
        reader.append(round(float(row), 3))
    return reader

def one(reader, files, typeg):
    graphtypes[typeg](points[0], readers[0])
    plt.axis([0, len(readers[0]), np.min(readers[0])-deltaminmax, np.max(readers[0])+deltaminmax])
    plt.title(os.path.basename(files[0]))

def two(readers, files, typeg):
    plt.subplot(121)
    graphtypes[typeg](points[0], readers[0])
    plt.axis([0, len(readers[0]), np.min(readers[0])-deltaminmax, np.max(readers[0])+deltaminmax])
    plt.title(os.path.basename(files[0]))

    plt.subplot(122)
    graphtypes[typeg](points[1], readers[1])
    plt.axis([0, len(readers[1]), np.min(readers[1])-deltaminmax, np.max(readers[1])+deltaminmax])
    plt.title(os.path.basename(files[1]))

def three():
    plt.subplot(131)
    graphtypes[typeg](points[0], readers[0])
    plt.axis([0, len(readers[0]), np.min(readers[0])-deltaminmax, np.max(readers[0])+deltaminmax])
    plt.title(os.path.basename(files[0]))

    plt.subplot(132)
    graphtypes[typeg](points[1], readers[1])
    plt.axis([0, len(readers[1]), np.min(readers[1])-deltaminmax, np.max(readers[1])+deltaminmax])
    plt.title(os.path.basename(files[1]))

    plt.subplot(133)
    graphtypes[typeg](points[2], readers[2])
    plt.axis([0, len(readers[2]), np.min(readers[2])-deltaminmax, np.max(readers[2])+deltaminmax])
    plt.title(os.path.basename(files[2]))

def dot(p, v):
    plt.plot(p, v,'ro')

def bar(p, v):
    plt.bar(p, v)

def line(p, v):
    plt.plot(p, v, '-o')

options = { 1 : one, 
            2 : two,
            3 : three,
}

graphtypes = { "dot" : dot,
                "bar" : bar,
                "line" : line,
}

def plotfiles(files, typeg='', overlapped=False):

    if not typeg:
        typeg = "dot" 

    for singlefile in files: 
        reader = openfile(singlefile)
        readers.append(reader)
        p = list(range(len(reader)))
        points.append(p)
    
    if not overlapped:
        plt.figure(1)
        options[len(files)](readers, files, typeg)
    else:
        fig, ax = plt.subplots()
        ax.plot(points[0], readers[0], label="first")
        ax.plot(points[1], readers[1], label="second")
        ax.legend()
    plt.show()




 