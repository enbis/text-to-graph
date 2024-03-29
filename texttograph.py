import csv
import os
import matplotlib.pyplot as plt
import numpy as np 
import os
import matplotlib.pyplot as plt
import numpy as np 
import argparse

readers = []
points = []
deltaminmax = 0.01

def openfile(filename):

    textread = open(filename, "r")
    reader = []
    for row in textread:
        try:
            reader.append(round(float(row), 3))
        except:
            print("Corrupted data, not a float. Step over.")
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

def three(readers, files, typeg):
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
    plt.plot(p, v,'o')

def bar(p, v):
    plt.bar(p, v)

def line(p, v):
    plt.plot(p, v, '-')

def linedot(p, v):
    plt.plot(p, v, '-o')

def linex (p,v):
    plt.plot(p, v, '-x')

options = { 1 : one, 
            2 : two,
            3 : three,
}

graphtypes = { "dot" : dot,
                "bar" : bar,
                "line" : line,
                "linedot" : linedot,
                "linex" : linex,
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
        for i, f in enumerate(files):
            if typeg == "bar":
                ax.bar(points[i], readers[i], label=os.path.basename(f))
            elif typeg == "dot":
                ax.scatter(points[i], readers[i], label=os.path.basename(f))
            else:
                ax.plot(points[i], readers[i], label=os.path.basename(f))
            ax.legend()
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Test argparse")

    parser.add_argument("-f", "--files", nargs='*', type=str,
                        help="Files to be parsed as chart")
    
    parser.add_argument("-t", "--type", nargs=1, type=str,
                        help="Type of charts - dot, line, bar, linedot, linex")

    parser.add_argument("-o", "--overlap", nargs=1, type=bool,
                        help="Overlap or not the charts")

    args = parser.parse_args()

    if (args.files) != None:
        print(args.files)
    
    if (args.type) != None:
        print(args.type)

    if (args.overlap) != None:
        print(args.overlap)

    plotfiles(args.files, typeg=args.type[0], overlapped=args.overlap[0])
    

if __name__ == "__main__":
    main()
 