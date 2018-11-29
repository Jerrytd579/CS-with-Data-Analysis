import matplotlib.pyplot as plt, csv, nltk
from pylab import plot

first_line = True

with open("C:/Users/jerry/Desktop/School Stuff/survey_results_public") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    for row in readCSV:
        if first_line == True:
            first_line = False
            continue


