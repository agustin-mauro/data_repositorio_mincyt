#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 00:25:17 2024

@author: Agustin Mauro
"""

"""
This script is designed to convert a collection of JSON files, representing 
records in the MINCyT repository, into a CSV file. 
Each record is a dictionary with items. Each item represents metadata for a 
specific repository record, such as a publication or research paper.

The CSV file is created and named 'final.csv' in the current working directory.
It consists of several columns, including 'title,' 'authors', 'date,'
 'subject,' 'abstract,' 'affiliation,' 'publisher,' 'language,' and 'url.'

The script iterates through all files in the current directory with a '.json' 
extension. 
For each JSON file, it attempts to load the JSON data and extract records. 
If successful, it opens or creates the CSV file in append mode and uses a 
DictWriter to write the extracted information into the CSV file.

For each record in the JSON data, the script extracts specific information such 
as title, authors, date, subject, abstract, language, URL, publisher, and 
affiliations. 
It then writes this information as a row in the CSV file.

If there are JSON decoding errors or any other exceptions during processing, 
the script handles them by printing informative error messages and 
continues processing the remaining files.

Note: The script assumes a specific structure in the JSON files, 
where relevant information is found under certain key names such as 
'dc.title', 'dc.creator', etc. 
Additionally, it uses the '***' separator for multi-valued fields like 
'dc.subject' and 'affs' to create a string representation in the CSV file.

The script complements the script '1_retrieve_and_save_mincyt_data.py' that
retrieves data from the MINCyT repository's API, and saves it in the 
appropriate format
"""

import json
import csv
import os

# File paths
json_folder = os.getcwd()
csv_filename = "final.csv"
csv_filepath = os.path.join(json_folder, csv_filename)

# Create the CSV file and write header
with open(csv_filepath, 'w', newline='', encoding='utf-8') as csv_file:
    # Define the fieldnames for the CSV columns
    fieldnames = ['title', 'authors', 'date', 'subject', 'abstract', 
                  'affiliation', 'publisher', 'language', 'url']
    
    # Create a CSV writer using DictWriter, specifying the fieldnames
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write the header row with the fieldnames to the CSV file
    writer.writeheader()


# Iterate through JSON files in the current directory
for filename in os.listdir(json_folder):
    # Check if the file has a '.json' extension
    if filename.endswith('.json'):
        # Open the JSON files
        with open(os.path.join(json_folder, filename), encoding='utf-8') as json_file:
            try:
                # Load JSON data
                data = json.load(json_file)
                
                # Open or create the CSV file in append mode
                with open(csv_filepath, 'a', newline='', encoding='utf-8') as csv_file:
                    # Create a CSV writer using DictWriter
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    
                    # Loop through each record in the JSON data
                    for record in data:
                        # Extract information from each record
                        # Each record its an item from the repository
                        
                        # TITLE
                        # Extract the title from the 'dc.title' field in the current record.
                        # If 'dc.title' is not present in the record, set the 'title' variable to an empty string.
                        # Same operation for the other items.
                        title = record.get('dc.title', '')
                        
                        # SUBJECT
                        # In the original data 'dc.subject' it's a list
                        # Convert list to a string using *** and remove trailing '***'
                        # The *** separator is used because CorText interprets it as such
                        subject = ' *** '.join(record.get('dc.subject', [])).rstrip(' *** ')
                        
                        # AUTHORS
                        authors = ' *** '.join(record.get('dc.creator', [])).rstrip(' *** ')
                        
                        # DATE
                        # Ensure the date has the correct format (XXXX)
                        # Some entries look like YEAR-MM-DD or YEAR-MM
                        date = record.get('dc.date', '')[:4]
                        
                        # ABSTRACT
                        # Abstracts have a list structure where only the first item is relevant
                        abstract = record.get('dc.description', [''])[0]
                        
                        # LANGUAGE
                        language = record.get('dc.language', '')
                        
                        # URL
                        url = record.get('url', '')
                        
                        # PUBLISHER
                        publisher = record.get('dc.publisher', '')
                        
                        # AFFILIATIONS
                        affiliation = ' *** '.join(record.get('affs', [])).rstrip(' *** ')
                        
                        # Write the extracted information to the CSV file
                        writer.writerow({'title': title, 
                                         'authors': authors, 
                                         'date': date, 
                                         'subject': subject, 
                                         'abstract': abstract, 
                                         'language': language, 
                                         'url': url, 
                                         'publisher': publisher, 
                                         'affiliation': affiliation})
            
            except json.JSONDecodeError as json_error:
                print(f"Error decoding JSON in file {filename}: {json_error}")
            except Exception as e:
                # Handle any other exceptions that may occur and continue with the next file
                print(f"Error processing file {filename}: {e}")
                continue
