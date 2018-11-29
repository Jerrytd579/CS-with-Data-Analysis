from pylab import plot, show, title, xlabel, ylabel, legend, savefig
import matplotlib.pyplot as plt
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
# # 1.0/7 to 3 decimal places
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
# print ("Hola, me llamo {0} y soy de {1}".format(nombre, ciudad) + ".")
#
# # Dictionaries
# town_directory = {'Bixler': 'Island Heights', 'Jones': 'Brick', 'Mom': 'Toms River'}
# print(town_directory.keys()) # Print out all keys
# print(town_directory.values()) # Print out all values
#
# for key, value in town_directory.items(): # Iterates through all key-value pairs and prints them
#     print(key, value)

# Tuples - These are simply immutable (cannot change size or values) lists
# Can separate values with commas, or do the same but with parentheses at start and end
a = 2, 3, 7, 4
b = (4, 9, 32, 11)

# Sets - Unordered, unique items
# s = {'Mark', 'Paul', 'Joe', 'Bill', 'Dinosaur', 'Joe'}
# print(s) # Prints all unique items in the set


nyc_temp = [53.9, 56.3, 56.4, 53.4, 54.5, 55.8, 56.8, 55.0, 55.3, 54.0, 56.7, 56.4, 57.3]
years = range(2000, 2013)
plot(years, nyc_temp, marker='o') # x-values, y-values, optional info about markers, etc.
show()
#
nyc_temp_2000 = [31.3, 37.3, 47.2, 51.0, 63.5, 71.3, 72.3, 72.7, 66.0, 57.0, 45.3, 31.1]
nyc_temp_2006 = [40.9, 35.7, 43.1, 55.7, 63.1, 71.0, 77.9, 75.8, 66.6, 56.2, 51.9, 43.6]
nyc_temp_2012 = [37.3, 40.9, 50.9, 54.8, 65.1, 71.0, 78.8, 76.7, 68.8, 58.0, 43.9, 41.5]
months = range(1, 13)
plot(months, nyc_temp_2000, months, nyc_temp_2006, months, nyc_temp_2012) # plots them in pairs
legend([2000, 2006, 2012])
title('Average Monthly Temperature in NYC')
xlabel('Month')
ylabel('Average Temperature (F)')
plt.show()
savefig('NYC Monthly Temperatures.png')

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

# def circle_area(radius):
#     return math.pi * radius ** 2
#
# print(circle_area(5))
#
#
# def circle_circum(radius = 2):
#     return 2 * math.pi * radius

# print(circle_circum()) # Will use default value of 2 specified in function
# print(circle_circum(4)) # Will use 4 as the input value instead



# def pow(c, d):
#     print(c ** d)
#
# if __name__ == '__main__':
#     a = float(input('Enter first float: '))
#     b = float(input('Enter second float: '))
#     pow(a,b)