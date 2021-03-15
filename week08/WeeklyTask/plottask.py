# Display a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# Author: Fiona Healy Donnelly

# importing relevant functions
import matplotlib.pyplot as plt
import numpy as np

# Creating my functions
def f(x):
    return (x)
def g(x):
    return (x**2)
def h(x):
    return (x**3)    

xAxis = np.array(range(0,5))
x1 = f(xAxis)
x2 = g(xAxis)
x3 = h(xAxis)

# Customising the plot
plt.plot(x1, color = "purple", marker = 'o', linestyle = 'dotted', markersize = 7, markeredgewidth=1, markeredgecolor='yellowgreen')
plt.plot(x2, color = "green", marker = 'o', linestyle = 'dotted', markersize = 7, markeredgewidth=1, markeredgecolor='darkorange')
plt.plot(x3, color = "blue", marker = 'o', linestyle = 'dotted', markersize = 7, markeredgewidth=1, markeredgecolor='red' )
plt.legend(["f(x)","g(x2)", "h(x3)"])

# Changing the fonts
csfont = {'fontname': 'Calibri'}
hfont = {'fontname': 'Calibri'}
plt.title('Plotting Functions', **csfont)
plt.xlabel('X Axis', **hfont)

SMALL_SIZE = 12
MEDIUM_SIZE = 14
BIGGER_SIZE = 16

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

# Setting the background color of the plot  
# using set_facecolor() method 
ax = plt.axes()
ax.set_facecolor("pink") 

# Show the plot
plt.show()

