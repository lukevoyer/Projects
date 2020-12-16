# Author: Lukeyer
# Major: IT
# Creation Date: 9/2/2020
# Due Date: 9/4/2020
# Course: Advanced Scientific Programming
# Professor Name: Dr. Schweisinger
# Assignment: Store Statistics
# Filename: main.py
# Purpose: Read in statistics within a .dat file for any number of departments
#          and preform actions on the data, presenting results in an
#          orderly fashion.

# Import statistics for later use in averaging
import statistics

# Declare hard-coded list for standard monthly sales for later use
standard_monthly_sales = [23.0,33.1,21.0,23.5,54.0,34.3,35.0,45.0,56.3,45.6,34.0,55.0]

# Declare lists at runtime to store data later in the program
monthly_sales_list = []
month_sales_avg = []
above_amt = []
below_amt = []
performace = []
satisfaction = []

# Ask for file name and read into variable 'fnam'
fnam = input("Enter file name: ")

# With the file open, for each line in said file, split the line into
# seperate seperate strings, convert to floats, then add those lists
# of each line (department) to another list (of monthly sales)
with open(fnam) as f:
    for line in f:
        lst_float = [float(x) for x in line.split()]
        monthly_sales_list.append(lst_float)


for sales in monthly_sales_list:
    # For each department list, calculate the average using the 'statistics' package imported above,
    # format results to one decimal point, and append to a list of monthly sales averages
    month_sales_avg.append(float(format(statistics.mean(sales),'.1f')))

# For each department, and each month, check whether sales are above or below the standard monthly sales
for i in range(0,len(monthly_sales_list)):
    # Set counts to zero for that month
    above = 0;
    below = 0;
    for j in range(0,12):
        # If above monthly sales, add on to 'above', otherwise add to 'below'
        if monthly_sales_list[i][j] >= standard_monthly_sales[j]:
            above = above + 1
        else:
            below = below + 1
    # Append to lists
    above_amt.append(above)
    below_amt.append(below)

# For the length of any number of departments in a list...
for i in range(0,len(monthly_sales_list)):
    # ...if sales amounts fall 'below' standard monthly sales more than four times...
    if below_amt[i] > 4:
        # ..deem performace 'unsatisfied'...
        satisfaction.append("unsatisfied")
    else:
        # ...otherwise 'satisfied'
        satisfaction.append("satisfied")

# Format 'pretty print' headers...
print("\n")
print("Store\tStatistics")
print("Dept\tAverage\t\tAbove\tBelow\tPerformance")  
print("----\t-------\t\t-----\t-----\t-----------")

#..and print over the course of any number of departments
for i in range(0,len(monthly_sales_list)):
    print(str((i+1)) + "\t" + str(month_sales_avg[i]) + "\t\t" + str(above_amt[i]) + "\t" + str(below_amt[i]) + "\t" + satisfaction[i])