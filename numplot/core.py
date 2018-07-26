from . import helpers
import matplotlib.pyplot as plt
import numpy as np

def get_hmm():
    """Get a thought."""
    return 'hmmm...'

def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())

class Map(dict):
    """
    A plotable map implementation that extends python's dictionary
    class with plotting facilities from Matplotlib.

    Author: Komahan Boopathy (komahan@gatech.edu)
    """
    def __init__(self, fname, *args, **kw):
        super(Map, self).__init__(*args, **kw)
    
        # Determine the number of lines
        num_lines = sum(1 for line in open(fname))
    
        # Initialize dictionary and add matrix entires
        # d = {}
        with open(fname) as f:    
            # Read first line to determine keys
            first_line = f.readline()
            keys = first_line.split()
            nkeys = len(keys)
            if nkeys == 0:
                raise "no header??"
    
            # Create a table to store values
            A = np.zeros([nkeys, num_lines-1])    
            lnum = 0
            for line in f:
                vals = line.split()
                vnum = 0
                for v in vals:
                    A[vnum,lnum] = float(v)
                    vnum += 1
                lnum += 1
        
            # Create a map with columns of A
            vnum = 0
            for key in keys:
                self[key] = A[vnum,:]
                vnum += 1
                
        return

    def plot(self, xkey, ykeys = None):
        # Use the map's keys if the keys to plot are  not supplied
        if ykeys is None:
            ykeys = self.keys()
            
        # Plot each key aloing y axis
        for ykey in ykeys:
            plt.plot(self[xkey], self[ykey], lw = 2, label = ykey)

        # Return the plot handle
        return plt
