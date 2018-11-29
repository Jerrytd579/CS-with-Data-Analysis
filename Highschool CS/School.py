import numpy as np, matplotlib.pyplot as plt
# print("Hello world!")
# x = 2
# y = 3.4
# # Here is how to find the type of a variable
# print(type(x))
# x = 'John'
# print(type(x))
# a = 5 + 2
# print(a)
# b = 9/5
# print(b)
# c = 9 // 5
# print(c)
# d = 2 ** 4
# print(d)
# test_grade = float(input("What did you get on the test?"))
# print(type(test_grade))
#
# quote = '''When I was your age, I wasn't sitting around
# playing with my iPhone all day.  I was out there
# in the coal mines working 168 hours a week.'''
#
# isDone = True
#
# temperature = 40
# wind_speed = 12
#
# if(temperature >= 100 and wind_speed < 5):
#     print("Wear shorts!")
# elif(temperature < 50 or wind_speed >= 40):
#     print("Don't go outside!")
#     print("You'll blow away!")
# else:
#     print("Go outside!")

# students = ['Mike', 'Reilly', 'Clara', 'John', 'Jim']
# print(students[0])
# print(students[-2])
#
# print("The first student's name is " + students[0])


import math
from pylab import plot, show, title, xlabel, ylabel, legend, savefig
# x = 2
# y = 3.4
# print(type(x))
# x = 'John'
# print(type(x))
# a = 5 ** 2
# print(a)
#
# first_name = 'John'
# last_name = 'Connor'
# multiple_lines = '''This is a long string of nonsense and spans multiple
# lines.  It is just an example and you will not need this for every
# string that you use.'''
#
# temperature = 50
# wind_speed = 30
# if (temperature >= 90 and wind_speed < 10):
#     print("Watch out for flies on the beach!")
# elif(temperature <= 10 or wind_speed > 80):
#     print("Avoid the beach!")
# else:
#     print("You might want to visit the beach.")
#
# print(3 / 2)
# print(3 // 2)
# print('{0:.3f}'.format(1.0/7))
# print("Hi!", end='') # Don't insert a new line after we print this
#
# # Lists
# grades = [90, 98, 75, 100, 99, 83, 88, 94, 'Peanut butter']
#
# print(grades[3])
# print(grades[1])
# print(grades[1:5]) # Grabs elements 1 through 5, exclusive of 5
# print(grades[-2]) # Grabs the second to last element
# print(grades[0:6:2]) #Grabs elements 0 to 6, exclusive of 6, jumping 2 values at a time [start:stop:step]
# print(len(grades)) # Prints how many elements there are in grades
# grades.remove('Peanut butter') # Remove this value
# print(grades)
# grades.append(85) # Append this value to the end of grades
# print(grades.pop()) # Pull off the last value and return it.  List is now one value shorter.
# grades.extend([70, 92, 87]) # Append all of these values to the end of grades
# print(grades)
# print(sorted(grades)) # Sort the list by number, smallest to largest by default
#
# sentence = "Hello, what's your name?"
# print(sentence[7]) # Grab character at index 7
# print(sentence[2:8]) # Get characters at indices 2 through 8, exclusive of 8
#
# nombre = "Marcos"
# ciudad = "Sevilla"
# print ("Hola, me llamo " + str(nombre) + " y soy de " + str(ciudad) + ".")
# # Alternate way of printing
# print ("Hola, me llamo {0} y soy de {1}.".format(nombre, ciudad))
#
# # Dictionaries
# town_directory = {'Bixler': 'Island Heights', 'Jones': 'Brick', 'Mom': 'Toms River'}
# print(town_directory.keys()) # Print out all keys
# print(town_directory.values()) # Print out all values
#
# for key, value in town_directory.items(): # Iterates through all key-value pairs and prints them
#     print(key, value)
#
# # Tuples - These are simply immutable (cannot change size or values) lists
# # Can separate values with commas, or do the same but with parentheses at start and end
# a = 2, 3, 7, 4
# b = (4, 9, 32, 11)
#
# # Sets - Unordered, unique items
# s = {'Mark', 'Paul', 'Joe', 'Bill', 'Dinosaur', 'Joe'}
# print(s) # Prints all unique items in the set


# nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
# years = range(2000, 2013)
# plot(years, nyc_temp, marker='o') # x-values, y-values, optional info about markers, etc.
# show()
#
# nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
# nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
# nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
# months = range(1, 13)
# plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012) # plots them in pairs
# legend([2000, 2006, 2012])
# title('Average Monthly Temperature in NYC')
# xlabel('Month')
# ylabel('Average Temperature (F)')
# savefig('NYC Monthly Temperatures.png')

###############################
## Task: Create a csv file in Excel with 3 rows of fake data.  Modify the code above to read in the data
## from the file and create a similar plot to the one above.
## This tutorial will help: https://pythonprogramming.net/reading-csv-files-python-3/


# for i in range(10):
#     print(i) # i is just a placeholder for the current value.  Iterates from 0 to 10 (exclusive)
#
# x = 1
# while (x <= 10):
#     print(x)
#     x += 1 # There is no x++ shortcut in Python
#
# # The continue and break keywords work exactly the same as in Java
# sentence = "Hello, what's new with you?"
# print(sentence.split()) # Splits sentence into a list, breaking it up by space
#
# squares = [x**2 for x in range(9)]
# print(squares) # Takes all integers from 0 to 9 (exclusive), square each, and print them out
#
# def circle_area(radius):
#     return math.pi * radius ** 2
#
# print(circle_area(5))
#
#
# def circle_circum(radius = 2):
#     return 2 * math.pi * radius
#
# print(circle_circum()) # Will use default value of 2 specified in function
# print(circle_circum(4)) # Will use 4 as the input value instead



# def pow(c, d):
#     print(c ** d)
#
# if __name__ == '__main__':
#     a = float(input('Enter first float: '))
#     b = float(input('Enter second float: '))
#     pow(a,b)

# import csv
#
# first_line = True
# with open('/Users/mbixler/PyCharmProjects/seattle_temp_data.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     dates = []
#     max_temps = []
#     mean_temps = []
#     min_temps = []
#
#     for row in readCSV:
#         # Skip first line
#         if first_line == True:
#             first_line = False
#             continue
#         if (row[1] != 'NA' and row[2] != 'NA' and row[3] != 'NA' and row[1] >= row[3]):
#             dates.append(row[0])
#             max_temps.append(1.8 * float(row[1]) + 32)
#             mean_temps.append(1.8 * float(row[2]) + 32)
#             min_temps.append(1.8 * float(row[3]) + 32)
#
#     day = range(len(max_temps))
#     print(len(day))
#     print(len(max_temps))
#     plot(day, max_temps, color = 'c', linewidth = 0.5) # marker = 'o', markersize = 0.5,
#     plot(day, mean_temps, color = 'g', linewidth = 0.5)
#     plot(day, min_temps, color = 'm', linewidth = 0.5)
#     legend(['Max Temp', 'Mean Temp', 'Min Temp'])
#     title('Daily Temperature (F) in Seattle ')
#     xlabel('Days After 1/1/48')
#     ylabel('Temperature (F)')
#     savefig('Seattle Temperatures.png', dpi = 200)
#     show()


## There are certain limitations in pylab.  It is not easy to add text labels, gridlines, etc. to the graph
## We will cycle back to this using matplotlib

## A directory that contains many modules is called a package.
## Indenting is compulsory in Python!
## It is considered good practice to indent with 4 spaces. You may configure your
## editor to map the Tab key to a 4-space indentation.
## You should not write very long lines that span over more than 80 characters.as
## Write well-spaced code: put whitespaces after commas, around arithmetic operators, etc.

# Reading files
# f = open('sample_file.txt', 'r')
# for line in f:
#     print(line)
# f.close()

# Get current directory
#import os
#print(os.getcwd())

# List all files in current directory
#print(os.listdir(os.curdir))

# os.path.walk generates a list of filenames in a directory tree

# Grab s list of all text (or any other kind) of files in a directory
# import glob
# for name in glob.glob('*.txt'):
#    print (name)

## Catching exceptions
# while True:
#     try:
#         x = int(input('Please enter a number: '))
#         break
#     except ValueError:
#         print('That was not a valid Steven count. Try again...')

## Object-oriented stuff...
## __init__ is Python is the constructor
## Just as we can use this.name = name in Java to set the instance variable, we do the same
## in Python via self.name = name
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def set_age(self, age):
#         self.age = age
#     def set_major(self, major):
#         self.major = major
#
# # Creates a student object and sets the name instance variable to Anna
# anna = Student('Anna')
# # Uses setter (mutator) method to set Anna's instance variable for her age to 21
# anna.set_age(21)
# # Uses another setter method to do the same for her major instance variable
# anna.set_major('Mathematics')

# Methods can be given default input parameters
# In this example, x will be set equal to 4 if the user does not specify an input parameter
# If they do specify an input parameter, it will use that instead
# def cube_number(x = 4):
#     print (x ** 3)
#
# cube_number(5)
# cube_number() # Uses default value of 4

## Chapter 3 - Numpy
## Numpy is a tool that provides structures and functions that perform very fast numerical
## computations in Python.  It involves heavy use of arrays.

## Recommended notation for importing numpy
#import numpy as np
# a = np.array([0, 1, 2, 3])
# print(a)
# print(len(a))
# print(a.shape)
# b = np.array([[0, 1, 2], [3, 4, 5]])
# c = np.linspace(0, 1, 6) # start, end, num-points
# print(c)
# d = np.ones((3, 4))
# print(d)
# e = np.zeros((5, 2))
# print(e)
# f = np.eye(3)
# print(f)
# g = np.random.rand(4)  # 4 numbers between 0 and 1
# print(g)

## Recommended notation for importing matplotlib
#import matplotlib.pyplot as plt, numpy as np
# x = np.linspace(0, 3, 20) # 20 points between 0 and 3, inclusive
# y = np.linspace(0, 9, 20) # 20 points between 0 and 9, inclusive
# plt.plot(x, y)
# plt.show()

# import matplotlib.pyplot as plt, numpy as np
# t = np.linspace(0, 4 * math.pi, 200)
# x = np.cos(t)
# y = np.sin(t)
# plt.plot(t, x, t, y)
# plt.xlim([-0.25, 4 * math.pi + 0.25])
# plt.ylim([-1.25, 1.25])
# plt.show()

## Checkpoint: Add another series for cos(t - pi) and color it orange
## Also add a legend to the graph
# t = np.linspace(0, 4 * math.pi, 200)
# x = np.cos(t)
# y = np.sin(t)
# z = np.cos(t - math.pi)
# plt.plot(t, x, t, y)
# plt.plot(t, z, color='orange')
# plt.xlim([-0.25, 4 * math.pi + 0.25])
# plt.ylim([-1.25, 1.25])
# legend(['cos t', 'sin t', 'cos(t-pi'])
# plt.show()

# a = np.arange(10) # Array with ints from 0 to 10, exclusive
# print(a)
# print(a[3]) # Prints element at index 3
# print(a[::-1])  # Prints array backwards

# np.random.seed(3) # Set the seed
# k = np.random.randint(0, 100, 15) # Generates 15 random integers from 0 to 100, exclusive
# print(k)

## Activity: Go to the tutorial at https://www.labri.fr/perso/nrougier/teaching/matplotlib/ and
## duplicate all steps until you get to "Figures, Subplots, Axes and Ticks"
## Keep this sample code in your PyCharm notes, as you will need it again!

## Checkpoint: A confused man is wandering around town.  Each minute, he takes a
## random number of steps, between 0 and 3, in either the north (positive y) or south (negative y) direction.
## Write code to simulate where he is at each one minute interval, then plot his position as a function of time.
## Do this for 100 minutes.  Title the graph, and add axis labels.

# import numpy as np, matplotlib.pyplot as plt
# time = 0
# y = [0]
# z = np.linspace(25, 25, 100)
# xbryanisstupid = [0]
# ybryanisstupid = [0]
# while time <= 100:
#     ybryanisstupid = np.random.randint(-3, 4, 100)
#     y = np.cumsum(ybryanisstupid)
#     time += 1
# xbryanisstupid = np.linspace(0, 101, 100)
#
# print(ybryanisstupid)
# print(xbryanisstupid)
#
# plt.plot(xbryanisstupid, y, xbryanisstupid, z)
# legend(['Position', 'Death'], fontsize=12)
# title('Drunk Man Stumbling Near a Cliff...', fontsize=40)
# plt.xlabel('Minutes', fontsize=20)
# plt.ylabel('Distance From Starting Point', fontsize = 20)
# # plt.ylim([-3, 3])
# plt.show()


## Bonus: If he ends up more than 25 steps north at any point in time, he will fall off of a cliff.  Plot a red
## horizontal line on the graph at y = 25 to indicate the position of the cliff.
## This will help the user visualize if he fell or not.

## Even bigger bonus!: Make a text label and arrow to point out what the red horizontal line means.

## Mathematical operations operate on the entire array
# a = np.arange(20)
# a += 5
# print(a)
# a *= 2
#
## You can compare each element of one array to another
# a = np.array([9, 22, 3, 4, 72, 8, -23])
# b = np.array([4, 22, 1, -5, 2, 90, -65])
# print(a == b)
#
# c = np.sort(a)
# print(c)
#
## Or do mathematical operations on the entire array
# print(np.sum(a))
# print(np.mean(a))
# print(np.max(a))
# print(np.argmax(a))
#

## Checkpoint: Can you convert a normal Python list into its more useful cousin, the numpy array?
## If so, how?  Give an example.  If not, why?

## We can use polynomials
# fn = np.poly1d([4, -5, -6])
# print(fn(0))
# print(fn.roots)

# x = np.linspace(0, 1, 50)
# y = np.cos(x) + 0.4 *np.random.rand(50)
# p = np.poly1d(np.polyfit(x, y, 2))
# t = np.linspace(0, 1, 200)
# plt.plot(x, y, 'o', t, p(t), '-')
# plt.show()

## Checkpoint: What the heck is this polyfit stuff above?  Comment each line of code with what you think it does.


# # # Mathematical operations operate on the entire array
# # import numpy as np
# # a = np.arange(20) # Prints out integers from 0 to 19
# # a += 5 # Adds five to all of them, in this case 5 to 24
# # print(a)
# # a *= 2
#
# # You can compare each element of one array to another
# import numpy as np
# a = np.array([9, 22, 3, 4, 72, 8, -23])
# b = np.array([4, 22, 1, -5, 2, 90, -65])
# print(a == b) # Prints out whether or not a = b as true false
# # Should print false, true, false, false, false, false false
#
# c = np.sort(a)
# print(c)
# # Sorts stuff in a in order and puts it into c
#
# # Or do mathematical operations on the entire array
# print(np.sum(a))
# print(np.mean(a))
# print(np.max(a))
# print(np.argmax(a)) # Finds the maximum value in that array and tells you the index for where you found that
# # Argmin finds the index of the mininmum, tells you the position where its at


## Checkpoint: Can you convert a normal Python list into its more useful cousin, the numpy array?
## If so, how?  Give an example.  If not, why?
# import numpy as np
# a = [1,2]
# np.asarray(a)
# np.array(a)

# We can use polynomials

# fn = np.poly1d([4, -5, -6]) # Plotting a polynomial, co-efficients to highest level to lowest =  4x^2 - 5x - 6
# print(fn(0)) # Function evaluated at 0
# print(fn.roots) # Tells you the real or imaginary roots

## You can load files using numpy as well
## The following will load all data in the txt file into an array.  You can also use this for csv or xlsx
# data = np.loadtxt('data/populations.txt')

## This series of commands loads the data from each column into lists called year, hares, etc.
## The .T method is the transpose, which switches columns into rows or vice-versa
## Data is at http://www.scipy-lectures.org/_downloads/populations.txt
#data = np.loadtxt('data/populations.txt')
# year, hares, lynxes, carrots = data.T # trick: columns to variables
# plt.axes([0.2, 0.1, 0.5, 0.8])
# plt.plot(year, hares, year, lynxes, year, carrots)
# plt.legend(('Hare', 'Lynx', 'Carrot'), loc=(1.05, 0.5))
# plt.show()

# We can generate heat maps from data.  This example just creates some random data before plotting it.
# image = np.random.rand(30, 30)
# plt.imshow(image, cmap=plt.cm.hot)
# plt.colorbar()
# plt.show()

# x = np.linspace(0, 1, 50)
# y = np.cos(x) + 0.4 *np.random.rand(50)
# p = np.poly1d(np.polyfit(x, y, 2))
# t = np.linspace(0, 1, 200)
# plt.plot(x, y, 'o', t, p(t), '-')
# plt.show()

## Checkpoint: What the heck is this polyfit stuff above?  Comment each line of code with what you think it does.

## Reading in all csv files from a directory, creating a graph for each, and saving that graph to a file

import csv
import re
from datetime import datetime

# import glob
# # Grab all of the csv files that end in "_weather_2014"
# # We're going to make a separate plot for each city with weather data
# for file in glob.glob('*_weather_2014.csv'):
#     # For this file, grab the portion of the file name before "_weather_2014.csv"
#     # \w means characters and \s means spaces
#     # Read up on regex (regular expressions for more info)
#     match = re.search(r'([\w\s]+)_weather_2014.csv',file)
#     # Grab the part of the file name with the city name
#     city = match.group(1)
#     # Get dates, high, and low temperatures from file.
#     filename = city + str('_weather_2014.csv')
#     with open(filename) as f:
#         reader = csv.reader(f)
#         header_row = next(reader)
#         # Remember to start with empty lists for each file.  We don't want data leaking in from previous files.
#         dates, highs, lows = [], [], []
#         for row in reader:
#             try:
#                 current_date = datetime.strptime(row[0], "%Y-%m-%d")
#                 high = int(row[1])
#                 low = int(row[3])
#             except ValueError:
#                 print(file, current_date, 'missing data')
#             else:
#                 dates.append(current_date)
#                 highs.append(high)
#                 lows.append(low)
#
#     # Plot data.
#     fig = plt.figure(dpi=128, figsize=(10, 6))
#     plt.plot(dates, highs, c='red', alpha=0.5)
#     plt.plot(dates, lows, c='blue', alpha=0.5)
#     plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#
#     # Format plot.
#     title = "Daily High and Low Temperatures - 2014\n{}".format(city)
#     plt.title(title, fontsize=20)
#     plt.xlabel('', fontsize=16)
#     fig.autofmt_xdate()
#     plt.ylabel("Temperature (F)", fontsize=16)
#     plt.tick_params(axis='both', which='major', labelsize=16)
#     #plt.ylim(10, 120)
#     plt.savefig(city + str("_weather.png"), dpi=72)

## Find some other data of interest to you, as this project will likely take a few days of work.
## It could be from NOAA, NASA, Zillow, etc.
## Kaggle is a website that you must create a login for, but has a plethora of datasets.



# Another example of a powerful plotting technique using best-fit line (80th order polynomial)
# This is an example of overfitting the data (using a best-fit line with too high of an order).
# np.random.seed(0)
# x = np.linspace(-1, 1, 2000)
# y = np.cos(x) + 0.3*np.random.rand(2000)
# p = np.polynomial.Chebyshev.fit(x, y, 80)
# t = np.linspace(-1, 1, 2000)
# plt.plot(x, y, 'g.')
# plt.plot(t, p(t), 'k-', lw=3)
# plt.show()

# # Example of a Mandelbrot plot
# # You might get some runtime warnings when you run this.
# from numpy import newaxis
# def compute_mandelbrot(N_max, some_threshold, nx, ny):
#     # A grid of c-values
#     x = np.linspace(-2, 1, nx)
#     y = np.linspace(-1.5, 1.5, ny)
#     c = x[:,newaxis] + 1j*y[newaxis,:]
#     # Mandelbrot iteration
#     z = c
#     for j in range(N_max):
#         z = z**2 + c
#     mandelbrot_set = (abs(z) < some_threshold)
#     return mandelbrot_set
# mandelbrot_set = compute_mandelbrot(50, 50., 601, 401)
# plt.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5])
# plt.gray()
# plt.show()

## Chapter 4 - Matplotlib
## Pyplot provides the interface to the matplotlib object-oriented plotting library
## You must have this statement to use it: from matplotlib import pyplot as plt
## Remember that you don't have to call it plt, but I would recommend that you do for simplicity.

## Mostly a review of what we've done in chapter 3 and the online tutorial previously

# # Create a figure of size 10x6 inches, 80 dots per inch
# plt.figure(figsize=(10, 6), dpi=80)
# # Create a new subplot from a grid of 1x1
# plt.subplot(1, 1, 1)
# X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# C, S = np.cos(X), np.sin(X)
# # Plot cosine with a blue continuous line of width 2.5 (pixels)
# plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
# # Plot sine with a green continuous line of width 2.5 (pixels)
# plt.plot(X, S, color="green", linewidth=2.5, linestyle="-")
# # Set x limits
# plt.xlim(X.min() * 1.1 , X.max() * 1.1)
# # Set x tick marks
# plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
#            [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
# # Set y limits
# plt.ylim(C.min() * 1.1, C.max() * 1.1)
# # Set y tick marks
# plt.yticks([-1, 0, +1],
#            [r'$-1$', r'$0$', r'$+1$'])
# # Add title
# plt.title(r'$Cosine\ and\ Sine\ vs.\ Angle$')
# # Add x-label
# plt.xlabel(r'$Angle$')
# # Add legend
# plt.legend([r'$Cosine$',r'$Sine$'])
# # Add grid lines
# plt.grid()
# # Save figure using 72 dots per inch
# # plt.savefig("trig_graph.png", dpi=72)
# plt.show()

# Scatter plot example
# n = 1024
# X = np.random.normal(0,1,n) # Create 1024 points using the Normal distribution, 68% will fall between -1 and 1, etc.
# Y = np.random.normal(0,1,n)
# plt.scatter(X,Y)
# plt.show()

# # Bar graph example
# n = 12
# X = np.arange(n)
# Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
# plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
# plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
# for x, y in zip(X, Y1):
#     plt.text(x + 0.4, y + 0.05, '%.2f ' % y, ha='center', va='bottom')
# for x, y in zip(X, Y2):
#     plt.text(x + 0.4, -y - 0.15, '%.2f ' % y, ha='center', va='bottom')
# plt.ylim(-1.25, +1.25)
# plt.show()

# # Contour maps!
# def f(x, y):
#     return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 -y ** 2)
# n = 256
# x = np.linspace(-3, 3, n)
# y = np.linspace(-3, 3, n)
# X, Y = np.meshgrid(x, y)
# plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap=plt.cm.hot)
# C = plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
# plt.clabel(C, inline=1, fontsize=10)
# plt.show()

# # Polar coordinate plotting
# plt.axes([0.025, 0.025, 0.95, 0.95], polar = True)
# N = 20
# theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
# radii = 10 * np.random.rand(N)
# width = np.pi / 4 * np.random.rand(N)
# bars = plt.bar(theta, radii, width=width, bottom=0.0)
# for r, bar in zip(radii, bars):
#     bar.set_facecolor(plt.cm.jet(r / 10.))
# bar.set_alpha(0.5)
# plt.show()

# 3-D contour plotting
# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = Axes3D(fig)
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.cool)
# ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap=plt.cm.cool)
# ax.set_zlim(-2, 2)
# plt.show()

## Great documentation for matplotlib options in section 4.6
## Full code examples in section 4.7

# # Awesome looking background
# eqs = []
# eqs.append((r"$W^{3\beta}_{\delta_1 \rho_1 \sigma_2} = U^{3\beta}_{\delta_1 \rho_1} + \frac{1}{8 \pi 2} \int^{\alpha_2}_{\alpha_2} d \alpha^\prime_2 \left[\frac{ U^{2\beta}_{\delta_1 \rho_1} - \alpha^\prime_2U^{1\beta}_{\rho_1 \sigma_2} }{U^{0\beta}_{\rho_1 \sigma_2}}\right]$"))
# eqs.append((r"$\frac{d\rho}{d t} + \rho \vec{v}\cdot\nabla\vec{v} = -\nabla p + \mu\nabla^2 \vec{v} + \rho \vec{g}$"))
# eqs.append((r"$\int_{-\infty}^\infty e^{-x^2}dx=\sqrt{\pi}$"))
# eqs.append((r"$F_G = G\frac{m_1m_2}{r^2}$"))
#
# plt.axes([0.025, 0.025, 0.95, 0.95])
#
# for i in range(24):
#     index = np.random.randint(0,len(eqs))
#     eq = eqs[index]
#     size = np.random.uniform(12,32)
#     x,y = np.random.uniform(0,1,2)
#     alpha = np.random.uniform(0.25,.75)
#     plt.text(x, y, eq, ha='center', va='center', color="#11557c", alpha=alpha,
#          transform=plt.gca().transAxes, fontsize=size, clip_on=True)
# plt.xticks(())
# plt.yticks(())
# plt.show()

## Chapter 5 - Scipy
## Scipy is the core package for scientific routines in Python.  It is meant to
## operate efficiently on numpy arrays, so that numpy and scipy work hand in hand.

# from scipy import linalg
# arr = np.array([[1, 2], [3, 4]])
# print(linalg.det(arr))
# arr = np.array([[3, 2], [6, 4]])
# print(linalg.det(arr))
#
# arr = np.array([[1, 2], [3, 4]])
# iarr = linalg.inv(arr)
# print(iarr)

## scipy.interpolate is useful for fitting a function from experimental data \
## and thus evaluating points where no measure exists

# from scipy.interpolate import interp1d
# measured_time = np.linspace(0, 1, 10)  # x-coordinate
# noise = (np.random.random(10)*2 - 1)
# measures = np.sin(2 * np.pi * measured_time) + noise # a sine function with some noise sprinkled in
#
# linear_interp = interp1d(measured_time, measures) # calculate the interpolated function
# interpolation_time = np.linspace(0, 1, 50) # x-coordinates for interpolated function
# linear_results = linear_interp(interpolation_time) # y-coordinates for interpolated function
# plt.plot(measured_time, measures, interpolation_time, linear_results)
# plt.legend(['function', 'interpolated function'])
# plt.show()

# # # Given some data, we can fit it to a data model of a certain form
# # # First, create some fake data
# from scipy import optimize
# x_data = np.linspace(-5, 5, num=50)
# y_data = 2.9 * np.sin(1.5 * x_data) + np.random.normal(size=50)
#
# # We want to fit the data to a model of the form f(x) = a * sin(bx)
# def test_func(x, a, b):
#     return a * np.sin(b * x)
# params, params_covariance = optimize.curve_fit(test_func, x_data, y_data, p0=[2, 2])
# print(params) # These are the unknown a and b values from our test_func

from scipy import stats
# samples = np.random.normal(size=1000)
# print(np.mean(samples))
# print(np.median(samples))
# print(stats.scoreatpercentile(samples, 90)) # What value is at the 90th percentile?

## A statistical test is a decision indicator. For instance,
## if we have two sets of observations, that we assume are generated from Gaussian processes, we can use
## a T-test to decide whether the means of two sets of observations are significantly different:

# a = np.random.normal(0, 1, size=100)
# b = np.random.normal(1, 1, size=10)
# print(stats.ttest_ind(a, b))
## The resulting output is composed of:
## The T statistic value: it is a number the sign of which is proportional to the difference between the two
## randomprocesses and themagnitude is related to the significance of this difference.
## The p value: the probability of both processes being identical. If it is close to 1, the two process are almost
## certainly identical. The closer it is to zero, themore likely it is that the processes have different means.

## Calculating integrals in scipy
# from scipy.integrate import quad
# res, err = quad(np.sin, 0, np.pi/2) # Integrates f(x) = sin(x) from 0 to pi/2
# # Res is the answer, err is an estimate of the error
# print(res)

# Image processing
# from scipy import misc # Load an image
# from scipy import ndimage
# # Shifts, rotations, and zooms
# face = misc.face(gray=True)
# shifted_face = ndimage.shift(face, (50, 50))
# rotated_face = ndimage.rotate(face, 30)
# cropped_face = face[50:-50, 50:-50]
# zoomed_face = ndimage.zoom(face, 2)
# print(rotated_face.shape)
# #plt.subplot(151)
# plt.imshow(rotated_face, cmap=plt.cm.gray)
# plt.show()

## Chapter 6 - Documentation
## Numpy and scipy have extensive documentation
## Type "help function_name" to get help with that function

## Skipping chapters on advanced topics
## There's some great stuff in here, but we've got a limited amount of class time left!

## Chapter 15 - Statistics in Python
## The pandas module:
## We will store and manipulate this data in a pandas.DataFrame, from the pandas module.
## It is the Python equivalent of the spreadsheet table. It is different from a 2D numpy array
## as it has named columns, can contain a mixture of different data types by column,
## and has elaborate selection and pivotal mechanisms.

import pandas
## This is a csv file, but is delimited by ; instead of ,
## The (NA =not available) marker turns every instance of "." into NaN.
## Pandas can now ignore the NaN values so we can do statistical analysis.
## data = pandas.read_csv('examples/brain_size.csv', sep=';', na_values=".")

# t = np.linspace(-6, 6, 20)
# sin_t = np.sin(t)
# cos_t = np.cos(t)
# # We can print out this data as a nice table using a DataFrame
# print(pandas.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t}))

from scipy import stats
# x = np.linspace(-5, 5, 20)
# np.random.seed(1)
# # Normally distributed noise
# y = -5 + 3*x + 4 * np.random.normal(size=x.shape)
# # Create a data frame containing all the relevant variables
# data = pandas.DataFrame({'x': x, 'y': y})
# from statsmodels.formula.api import ols
# # Determine the ordinary least squares model for this data
# model = ols("y ~ x", data).fit()
# # Print out lots of details for this learned model
# print(model.summary())

## Seaborn combines simple statistical fits with plotting on pandas dataframes.
## This module is not part of Anaconda and must be installed separately.
## It is very powerful though, so take a look through what it can do in the notes.

# import matplotlib.pyplot as plt
# import pandas
# from pandas.tools import plotting
# from statsmodels.formula.api import ols
# # Load the data
# data = pandas.read_csv('iris.csv')
# print(data)
# # Express the species names as categories
# categories = pandas.Categorical(data['species'])
# # The parameter 'c' is passed to plt.scatter and will control the color
# plotting.scatter_matrix(data, c=categories.labels, marker='o')
# fig = plt.gcf()
# fig.suptitle("blue: setosa, green: versicolor, red: virginica", size=13)
# plt.show()

## Chapter 16 - Sympy: Symbolic Mathematics in Python
## SymPy defines three numerical types: Real, Rational and Integer.

import sympy as sym
## The Rational class represents a rational number as a pair of two Integers:
## The numerator and the denominator, so Rational(1, 2) represents 1/2,
## Rational(5, 2) 5/2 and so on.

## You have to declare your variables explicitly before using them:
x = sym.Symbol('x')
y = sym.Symbol('y')
# print(x + y + x - y)
# print(sym.expand((x + y) ** 3))
# print(sym.simplify((x + x * y) / x))
#
## Limits are easy to use in SymPy, they follow the syntax
## limit(function, variable, point), so to compute the limit of sin(x) / x
## as x approaches 0, you would use:
# print(sym.limit(sym.sin(x) / x, x, 0))
#
## Differentiation (aka derivatives)
## You can differentiate any SymPy expression.  The derivative of sin(x) with respect to x:
# print(sym.diff(sym.sin(x), x))
## Higher nth derivatives can be calculated using the diff(func, var, n)
## The second derivative of sin(2x) with respect to x:
 # print(sym.diff(sym.sin(2 * x), x, 2))
## We can also do integrals.
## The integral (area under the curve) of sin(x) with respect to x:
# print(sym.integrate(sym.sin(x), x))
## The integral of x^3 with respect to x between -1 and 2:
# print(sym.integrate(x**3, (x, -1, 2)))

## Chapter 20 - Scikit-learn: Machine Learning in Python
## Machine Learning is about building programs with tunable parameters
## that are adjusted automatically so as to improve their behavior
## by adapting to previously seen data.
#
## Machine learning algorithms implemented in scikit-learn expect data
## to be stored in a two-dimensional array or matrix.
## The arrays can be either numpy arrays, or in some cases scipy.sparse matrices.
## The size of the array is expected to be [n_samples, n_features]
## n_samples: The number of samples: each sample is an item to process (e.g. classify).
## A sample can be a document, a picture, a sound, a video, an astronomical object,
## a row in database or CSV file, or whatever you can describe with a fixed set of quantitative traits.
## n_features: The number of features or distinct traits that can be used to describe
## each item in a quantitative manner. Features are generally real-valued, but
## may be boolean or discrete-valued in some cases.
#
## scikit-learn embeds a copy of the iris CSV file along with a function to load it into numpy arrays:
# from sklearn.datasets import load_iris
# iris = load_iris()
## The features of each sample flower are stored in the data attribute of the dataset:
#
# print(iris.data.shape)
# n_samples, n_features = iris.data.shape
# print(n_samples) # We have 150 samples
# print(n_features) # Each sample has data for 4 features

## Supervised learning is further broken down into two categories, classification and regression.
## In classification, the label is discrete, while in regression, the label is continuous.
## For example, in astronomy, the task of determining whether an object is a star,
## a galaxy, or a quasar is a classification problem: the label is from three distinct categories.
## On the other hand, we might wish to estimate the age of an object based on such
## observations: this would be a regression problem, because the label (age) is a continuous quantity.

## Classification: K nearest neighbors (kNN) is one of the simplest learning strategies:
## Given a new, unknown observation, look up in your reference database which ones
##  have the closest features and assign the predominant class.
## Let’s try it out on our iris classification problem:

# from sklearn import neighbors, datasets
# iris = datasets.load_iris()
# X, y = iris.data, iris.target
# # Use the kNN machine learning classifier
# knn = neighbors.KNeighborsClassifier(n_neighbors=1)
# # Learn from the iris data provided
# knn.fit(X, y)
# # What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
# print(iris.target_names[knn.predict([[3, 5, 4, 2]])])

from sklearn.datasets import load_digits
digits = load_digits()
# Plot the digits dataset: each image is 8x8 pixels
fig = plt.figure()
# for i in range(64):
#     ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
#     ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
# plt.show()

## A good first-step for many problems is to visualize the data using a
## Dimensionality Reduction technique. We’ll start with the
## most straightforward one, Principal Component Analysis (PCA).

## PCA seeks orthogonal linear combinations of the features which
## show the greatest variance, and as such, can help give you a
## good idea of the structure of the data set.

## This plot shows PCA trying to distinguish the individual digits from one another.
## The more separated the samples of a different color are, the better the algorithm
## is able to distinguish them from one another.

# from sklearn.decomposition import PCA
# pca = PCA(n_components=2)
# proj = pca.fit_transform(digits.data)
# plt.scatter(proj[:, 0], proj[:, 1], c=digits.target)
# plt.colorbar()
# plt.show()

## For most classification problems, it’s nice to have a simple, fast method
## to provide a quick baseline classification. If the simple and fast method is sufficient,
## then we don’t have to waste CPU cycles on more complex models. If not,
## we can use the results of the simple method to give us clues about our data.
## One good method to keep in mind is Gaussian Naive Bayes (sklearn.naive_bayes.GaussianNB).


from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split
# or from sklearn.model_selection import train_test_split (depends on version of sklearn)

## Split the data into training and validation sets
# X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)
## Train the model using Gaussian Naive Bayes on the training data
# clf = GaussianNB()
# clf.fit(X_train, y_train)
## Use the training model to predict the labels of the test data
# predicted = clf.predict(X_test)
# expected = y_test
## List of digit predictions
# print(predicted)
## List of actual digits
# print(expected)
## List showing whether we were correct for each prediction
# matches = (predicted == expected)
# print(matches.sum())
# print(len(matches))
# print("Accuracy was {}".format(matches.sum() / float(len(matches))))