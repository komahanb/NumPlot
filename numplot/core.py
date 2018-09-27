#from . import helpers

# Import matplotlib
import matplotlib.pylab as plt

# Configure 
plt.rcParams['xtick.direction'] = 'out'
plt.rcParams['ytick.direction'] = 'out'

# Optionally set font to Computer Modern to avoid common missing font errors
params = {
  'axes.labelsize': 20,
  'legend.fontsize': 14,
  'xtick.labelsize': 20,
  'ytick.labelsize': 20,
  'text.usetex': True}
plt.rcParams.update(params)

# Latex math
plt.rcParams['text.latex.preamble'] = [r'\usepackage{sfmath}']
plt.rcParams['font.family'] = 'sans-serif'
# plt.rcParams['font.sans-serif'] = 'courier'
plt.rcParams['font.size'] = 18
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['lines.linewidth'] = 4
plt.rcParams['lines.color'] = 'r'

# Make sure everything is within the frame
plt.rcParams.update({'figure.autolayout': True})

# These are the "Tableau 20" colors as RGB.    
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]    
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)

import numpy as np

def get_hmm():
    """Get a thought."""
    return 'hmmm...'

def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())

# We encapsulate data as Map
# We define Style
# Once a Style is associated with Map we have defined a View
# map   = Map(datafilename)
# style = Style(axes, labels, colors, lines, title, etc)
# 
# map.setStyle(style)
# map.view()
# 
# map.compare(map_list, style_list) # or make a map with key as datamap and value as style
# 
# map.view(style)/map.plot(style)
# view.compare(view2) --> extract styles from vies

# Map
class Map(dict):
    """
    A plotable map implementation that extends python's dictionary
    class with plotting facilities from Matplotlib.

    Author: Komahan Boopathy (komahan@gatech.edu)
    """
    def __init__(self, fname, delimiter=',', map_name=None, *args, **kw):
        super(Map, self).__init__(*args, **kw)

        self.map_name = map_name
        
        # Determine the number of lines
        num_lines = sum(1 for line in open(fname))
    
        # Initialize dictionary and add matrix entires
        # d = {}
        with open(fname) as f:    
            # Read first line to determine keys
            first_line = f.readline()
            try:
                keys = first_line.split(delimiter)
                nkeys = len(keys)
                if nkeys == 0:
                    raise "no header??"
            except:
                print("Error: No keys found! Check delimiter input : comma or space?")
                raise
    
            # Create a table to store values
            A = np.zeros([nkeys, num_lines-1])    
            lnum = 0
            for line in f:
                vals = line.split(delimiter)
                vnum = 0
                for v in vals:
                    A[vnum,lnum] = float(v)
                    vnum += 1
                lnum += 1
        
            # Create a map with columns of A
            vnum = 0
            for key in keys:
                self[key.strip()] = A[vnum,:]
                vnum += 1
                
        return

    def plot(self, xkey, ykeys = None):
        # Use the map's keys if the keys to plot are  not supplied
        if ykeys is None:
            ykeys = self.keys()
            
        # Plot each key aloing y axis
        for ykey in ykeys:
            plt.plot(self[xkey], self[ykey], '-o', lw = 2, label = ykey)

        # Return the plot handle
        return plt


    def twin_plot(self, xkey, y1keys, y2keys):        
        fig, ax1 = plt.subplots()
    
        # Plot each key aloing y axis
        for ykey in y1keys:
            ax1.plot(self[xkey], self[ykey], '-', lw = 2, label = ykey)

        ax2 = ax1.twinx()
        # Plot each key aloing y axis
        for ykey in y2keys:
            ax2.plot(self[xkey], self[ykey], '--', lw = 2, label = ykey)

        # Return the plot handle
        return plt, fig, ax1, ax2


    def compare(self, xkey, ykeys, map2):
        # Use the map's keys if the keys to plot are  not supplied
        if ykeys is None:
            ykeys = self.keys()
            
        # Plot each key aloing y axis
        for ykey in ykeys:
            plt.plot(self[xkey], self[ykey], lw = 2, label = ykey + " " + self.map_name)

        # Plot each key aloing y axis
        for ykey in ykeys:
            plt.plot(map2[xkey], map2[ykey], lw = 2, label = ykey + " " + map2.map_name)

        # Return the plot handle
        return plt
    
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
            plt.plot(self.map[xkey]/xscale, self.map[ykey]/yscale, '-o',lw = 2, label = ykey)

        # Plot save and close
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend(loc=legend)
        plt.savefig(outputfile, bbox_inches='tight', pad_inches=0.05)
        plt.close()
        
        # Return the plot handle
        return
    
class Compare:
    '''
    To compare two or more data sets. Dissimilar data sets can not be
    compared, therefore make sure they are comparable. This is where
    dataname becomes handy.

    1. two datamaps are there to compare
    3. two plot objects created using datamaps are there to compare
    '''
    def __init__(datalist):
        self.datalist = datalist        
        return
    
    def compare(self, xkey, ykeys, map1, map2):
        # Use the map's keys if the keys to plot are  not supplied
        if ykeys is None:
            ykeys = map1.keys()
            
        # Plot each key aloing y axis
        for ykey in ykeys:
            plt.plot(map1[xkey], map1[ykey], lw = 2, label = map1.map_name + " " + ykey)

        # Plot each key aloing y axis
        for ykey in ykeys:
            plt.plot(map2[xkey], map2[ykey], lw = 2, label = map2.map_name + " " + ykey)

        # Return the plot handle
        return plt

if __name__ == "__main__":

    data = Map('data.csv')
    print data
    stop
    
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
