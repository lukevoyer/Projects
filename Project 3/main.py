# Author: Luke Voyer
# Major: IT
# Creation Date: 9/21/2020
# Due Date: 9/18/2020
# Course: Advanced Scientific Programming
# Professor Name: Dr. Schweisinger
# Assignment: File Formats
# Filename: main.py
# Purpose: Read in a json file with MTG data, parse data for 'Creature' entries,
#          delete duplicates, sort alphabetically, and export certain fields from
#          the JSON file to a CSV file

# import libraries needed for parsing and printing
import json
import csv


# Function Name: get_data
# Function Inputs: none
# Function Outputs: json_parsed - A dictionary of parsed data from a specified JSON file
# Function Purpose: Read in a JSON file and return a parsed dictionary
def get_data():
    
    # open file ('M21.json must be in this directory') 
    try:
        with open('M21.json', encoding='utf-8') as f:
            
            # read data into an object
            data = f.read()
  
            # Parse as JSON
            json_parsed = json.loads(data)
            
        # print found file message
        print("File found and loaded.")
    
    # file not found exception
    except FileNotFoundError:
    
        # print found file message
        print("File does not exist, edit open filename to correct. Exiting...")
        
        # Quit when error fails the program
        quit()
        
    # Return dictionary containing JSON data
    return json_parsed

# Function Name: get_creatures
# Function Inputs: dict - dictionary with JSON data 
# Function Outputs: json_creat - A parsed list containing only cards of type 'Creature'
#                   with no duplicates
# Function Purpose: Read in a dictionary and return a parsed list containing 
#                   only cards of type 'Creature' with no duplicates
def get_creatures(dict):
    # Instantiate creature list
    json_creat = []
    
    # Instantiate an iterator
    i = 0
    
    # for each card in dictionary's cards
    for card in dict['data']['cards']:
        
        # for each creature card
        if card['types'] == ['Creature']:
            
            # system to check if cards already exist in the dataset,
            # given that duplicates appear one after another
            if i == 0:
                    json_creat.append(card)
                    i = i + 1
            else: 
                # duplicate check
                if json_creat[i - 1]['name'] != card['name']:
                    json_creat.append(card)
                    i = i + 1
                    
    # return creatue list
    return json_creat

# Function Name: alpha_sort
# Function Inputs: list - List of creatures from a parsed JSON file
# Function Outputs: list - List of creatures from a parsed JSON file, alphabetized
# Function Purpose: Sorts a list given in, alphabetically using bubble sort
def alpha_sort(list):
    # Bubble sort
    for i in range(0,len(list)-1):
        if list[i]['name'] > list[i+1]['name']:
            list[i], list[i+1] = list[i+1], list[i]
    
    # Return sorted list
    return list

# Function Name: parse_list
# Function Inputs: list - Alphabetized, trimmed, list of creatures from a parsed JSON file
# Function Outputs: new_list - Smaller list of fields we want
# Function Purpose: Parses a list given in and returns a smaller list of fields we actually want
def parse_list(list):

    # Declare new list to output
    new_list = []
    
    for c in list:
        # Declare a new addition to the output list
        new_add = []
        
        # Parse only fields we need from input list
        new_add.append(c['name'])
        new_add.append(c['type'])
        new_add.append(c['manaCost'])
        new_add.append(c['convertedManaCost'])
        new_add.append(c['power'])
        new_add.append(c['toughness'])
        
        # Append found fields to output list
        new_list.append(new_add)
        
    # Return output list
    return new_list

# Function Name: write_file
# Function Inputs: list - Alphabetized, trimmed, and parsed list of creatures from a parsed JSON file
# Function Outputs: none
# Function Purpose: Instanitates a csv writer from the csv package, prints a header, and th content of the
#                   list to a csv file, formatted
def write_file(list):
    # Declare output file
    try:
        with open('output.csv', mode='w', newline='') as output_file:
            # Instantiate csv writer
            output_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
            # Print header titles
            output_writer.writerow(['name', 'type', 'manaCost', 'convertedManaCost', 'power', 'toughness'])
        
            # Print list to csv
            for i in list:
                output_writer.writerow(i) 
    
        # Confirm print
        print("Output csv created in program directory.")
    
    # file write permission error
    except PermissionError:
    
        # print write permission error message
        print("Cannot write to csv (File possibly open in the background). Exiting...")
        
        # Quit when error fails the program
        quit()
    return 0

# Function Name: parse_list
# Function Inputs: none
# Function Outputs: none
# Function Purpose: run 'main' functions
def main():
    # Get json data into python dict
    json_dict = get_data()
    
    # Parse, and alphabetically sort, the JSON dictionary for creatures, no duplicates
    creatures = alpha_sort(get_creatures(json_dict))
    
    # Write contents to a csv file
    write_file(parse_list(creatures))
    return 0

# Python conventions for main function
if __name__ == '__main__':
    # Run main function
    main()