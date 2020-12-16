# Author: Lukeyer
# Major: IT
# Creation Date: 9/16/2020
# Due Date: 9/18/2020
# Course: Advanced Scientific Programming
# Professor Name: Dr. Schweisinger
# Assignment: Basic Python Scripting
# Filename: main.py
# Purpose: Read in statistics within a .dat file for any number of departments
#          and preform actions on the data, presenting results in an
#          orderly fashion.


# Literals for initializing filename string
# and number of months observed in the data file
filename = ""
num_months = 12

# Function Name: list_avg
# Function Inputs: list - List of sales for that department
# Function Outputs: avg - Average of that dept.'s sales
# Function Purpose: Average a month's sales given a department's monthly sales for a given time frame

def list_avg(list):
    
    # Initialize sum
    sum = 0.0
    
    # Sum up total and divide by length to find average
    for t in list:
        sum = sum + t
    avg = float(format(sum / len(list),'.1f'))
    
    # Return average
    return avg

# Function Name: find_above
# Function Inputs: list - List of sales for that department
# Function Outputs: above - Number of month's above monthly average
# Function Purpose: Return a department's amount of months where sales were above the average

def find_above(list):

    # Initialize standard monthly slaes lists for comparison
    standard_monthly_sales = [23.0,33.1,21.0,23.5,54.0,34.3,35.0,45.0,56.3,45.6,34.0,55.0]
    
    # Initialize above count
    above = 0;
    
    # Compare list of sales standard monthly sales, find and count all scores below monthly averages
    for i in range(0,len(list)):
        
        if list[i] >= standard_monthly_sales[i]:
            above = above + 1
    return above

# Function Name: find_below
# Function Inputs: list - List of sales for that department
# Function Outputs: below - Number of month's below monthly average
# Function Purpose: Return a department's amount of months where sales were below the average

def find_below(list):

    # Initialize standard monthly slaes lists for comparison
    standard_monthly_sales = [23.0,33.1,21.0,23.5,54.0,34.3,35.0,45.0,56.3,45.6,34.0,55.0]
    
    # Initialize above count
    below = 0;
    
    # Compare list of sales standard monthly sales, find and count all scores below monthly averages
    for i in range(0,len(list)):

        if list[i] <= standard_monthly_sales[i]:
            below = below + 1
    return below

# Function Name: find_performance
# Function Inputs: list - List of sales for that department
# Function Outputs: "satisfied", "unsatisfied" - determaination of whether or not sales had been below > 4 months
# Function Purpose: Determines whether or not a department's sales had been below > 4 months

def find_performance(list):
    # For the length of any number of departments in a list...
    for i in range(0,len(list)):
        # ...if sales amounts fall 'below' standard monthly sales more than four times...
        if find_below(list) > 4:
            # ..deem performace 'unsatisfied'...
            return "unsatisfied"
        else:
            # ...otherwise 'satisfied'
            return "satisfied"

# Function Name: get_parent_folder
# Function Inputs: fnam - File path
# Function Outputs: path - Path of the parent folder
# Function Purpose: Grabs parent folder of input file recieved

def get_parent_folder(fnam):

    # Initialize path and parts list
    path = ""
    lst_path_parts = []
    
    # Get path parts minus one
    for x in fnam.split('\\'):
        lst_path_parts.append(x)
        
    del lst_path_parts[-1]
    
    # Reconstruct path
    for p in lst_path_parts:
        path = path + p
        path = path + "\\" 
    
    # Return parent path
    return path

# Function Name: get_data
# Function Inputs: fnam - File path
# Function Outputs: monthly_sales_list - Organized list of lists determining departments and their sales
# Function Purpose: Gets data from file and returns an organized list of lists determining departments and their sales

def get_data(fnam):
    # Initialize initial array
    lst_float = []
    
    # Open and read file
    with open(fnam) as f:
        for line in f:
            for x in line.split():
                # Append each value to list
                lst_float.append(float(x))

    # Initialize rows and columns based on months observed
    rows, cols = (num_months, int(len(lst_float) / num_months)) 
    
    # Initialize monthly sales list sperated per department
    monthly_sales_list = []
    
    # Fill monthly sales list per department
    for i in range(cols): 
        col = [] 
        for j in range(rows):
            col.append(lst_float[(i * 10) + (j)]) 
        monthly_sales_list.append(col) 
    
    # Return monthly sales list
    return monthly_sales_list

# Function Name: process_data
# Function Inputs: list - List of all monthly stats
# Function Outputs: outer_list - organized list of data
# Function Purpose: Processes and organizes data based on statistical analysis
def process_data(list):
    # Initialize variables for dictionary population
    outerList = []
    deptCode = 1
    
    # Populate list of dictionaries for each item in the list using helper functions
    for item in list:
        innerDict = {"Department":[], "Average":[], "Above":[], "Below":[], "Performance":[]}
        innerDict["Department"] = deptCode
        innerDict["Average"] = list_avg(item)

        innerDict["Above"] = find_above(item)

        innerDict["Below"] = find_below(item)

        innerDict["Performance"] = find_performance(item)

        deptCode += 1
        outerList.append(innerDict)
    
    # Return list of dictionaries
    return outerList

# Function Name: get_data
# Function Inputs: dict_list - Dictionary list of organized statistics, file_name - File path
# Function Outputs: monthly_sales_list - Organized list of lists determining departments and their sales
# Function Purpose: Wries organized data to output file in "pretty print"
def write_to_file(dict_list, file_name):
    
    # Generate file output path
    file_output_name = get_parent_folder(file_name)
    file_output_name += ("output.dat")

    # Open and write header to file
    f = open(file_output_name, "w")
    f.write('{:<10}'.format('Department'))
    f.write('{:^20}'.format('Average'))
    f.write('{:^0}'.format('Above'))
    f.write('{:^20}'.format('Below'))
    f.write('{:<10}'.format('Performance'))
    f.write("\n")
    f.write('{:<10}'.format('----------'))
    f.write('{:^20}'.format('-------'))
    f.write('{:^0}'.format('-----'))
    f.write('{:^20}'.format('----'))
    f.write('{:<10}'.format('-----------'))
    
    # Open and write list of results
    for i in range(len(dict_list)):
        f.write("\n")
        f.write('{:<16}'.format(str(dict_list[i]["Department"])))
        f.write('{:<14}'.format(str(dict_list[i]["Average"])))
        f.write('{:<12}'.format(str(dict_list[i]["Above"])))
        f.write('{:<13}'.format(str(dict_list[i]["Below"])))
        f.write('{:<14}'.format(str(dict_list[i]["Performance"])))
    f.close()
    return 0

# Function Name: main
# Function Inputs: none
# Function Outputs: none
# Function Purpose: Main load function
def main():
    # Populate filename
    filename = input("Enter input file name: ")
    
    # Write output to designated subfolder given an input file
    write_to_file(process_data(get_data(filename)), filename)
    return 0

# Run main function
main()
