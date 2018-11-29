# import csv
#
# with open('seattle_temp_data.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         print(row)
#         print(row[0])
#         print(row[0],row[1],row[2],)

# import csv
#
# with open('seattle_temp_data.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     dates = []
#     colors = []
#     for row in readCSV:
#         color = row[3]
#         date = row[0]
#
#         dates.append(date)
#         colors.append(color)
#
#     print(dates)
#     print(colors)

# import csv
#
# with open('example.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     dates = []
#     colors = []
#     for row in readCSV:
#         color = row[3]
#         date = row[0]
#
#         dates.append(date)
#         colors.append(color)
#
#     print(dates)
#     print(colors)
#
#     # now, remember our lists?
#
#     whatColor = input('What color do you wish to know the date of?:')
#     coldex = colors.index(whatColor)
#     theDate = dates[coldex]
#     print('The date of',whatColor,'is:',theDate)

import csv
from pylab import plot, show, title, xlabel, ylabel, legend, savefig

with open ('seattle_temp_data_1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    Dates = []
    Max_TemperatureC = []
    Min_TemperatureC = []
    Mean_TemperatureC = []
    num = 1
    for row in readCSV:
        Date = row[0]
        Max_Temp = row[1]
        Mean_Temp = row[2]
        Min_Temp = row[3]

        Dates.append(num)
        num += 1
        Max_TemperatureC.append(Max_Temp)
        Mean_TemperatureC.append(Mean_Temp)
        Min_TemperatureC.append(Min_Temp)

# Dates = range(1948, 2015)
plot(Dates, Max_TemperatureC, Dates, Min_TemperatureC, Dates, Mean_TemperatureC)
legend(["Max_TemperatureC", "Min_TemperatureC", "Mean_TemperatureC"])
title('Seattle Temperature Data')
xlabel('Dates')
ylabel('Temperature')
show()
