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
    def __init__(self, fname, data_name=None, *args, **kw):
        super(Map, self).__init__(*args, **kw)

        self.data_name = data_name
        
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
    
# what you want to plot --> txt with header, txt without headers
# Plot on dataset
# Compare two or more similar data sets
# Lets create a map for each data set and use it to encapsulate the data
# How you want to plot  --> automatic/manual

class Plot:
    def __init__(self, datafile = None):
        # Associate a data map with the plot object
        if isinstance(datafile, Map):            
            self.map  = datafile
        else:
            self.map  = Map(datafile)            
        return

    def setData(self, datafile):
        # Associate a data map with the plot object
        if isinstanceof(datafile, Map):            
            self.map  = datafile
        else:
            self.map  = Map(datafile)            
        return
    
    def plot(self, xkey, ykeys = None, xlabel = None, ylabel = None,  legend = None, title = None, outputfile = 'plot.pdf', xscale=1.0, yscale=1.0):
        # If no xkey use the first column as the xkey
        if xkey is None:
            xkey = self.map.keys()[0]
                
        # Use the map's keys if the keys to plot are  not supplied
        if ykeys is None:
            ykeys = self.map.keys()
            
        # Plot each key aloing y axis
        for ykey in ykeys:
            plt.plot(self.map[xkey]/xscale, self.map[ykey]/yscale, lw = 2, label = ykey)

        # Plot save and close
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend(loc=legend)
        plt.savefig(outputfile, bbox_inches='tight', pad_inches=0.05)
        plt.close()
        
        # Return the plot handle
        return

if __name__ == "__main__":
    
    # Wrap all these into context object
    datafile   = "ebeam.dat"
    outputfile = "ebeam.pdf"
    xkey       = "x"
    ykeys      = ["u", "v", "w", "phi", "theta", "psi"]
    xlabel     = "Axial coordinate [m]"
    ylabel     = "State Values"
    title      = ""
    legend     = "best"
    
    # Create a datamap
    plt = npl.Plot(datafile)
    # plt.setData(data)
    # plt.setContext(ctx)
    # plt.getPlot() --> and continue as if the rest is same as pyplot
    
    # plot and save
    plt.plot(xkey, ykeys, xlabel, ylabel, legend, title, outputfile)
