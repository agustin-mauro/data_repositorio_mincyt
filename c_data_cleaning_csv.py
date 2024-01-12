#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 02:45:51 2024

@author: madam
"""
import csv
import os

def delete_row_with_string(string_to_remove, file_name, original_file_option='keep'):
    """
    Removes rows containing a specified string from a comma-separated values (CSV) file.

    Parameters:
        string_to_remove (str): The string to be removed from the rows. The removal is case-insensitive.
        file_name (str): The name of the input CSV file.
        original_file_option (str, optional): Determines whether to keep or delete the original file.
            - 'keep': Keep the original file.
            - 'delete': Delete the original file. Defaults to 'keep'.

    Output:
        The function creates two new files:
            - A cleaned CSV file named '<original_file_name>_new.csv', containing rows without the specified string.
            - A file named 'removed_entries_<string_to_remove>.csv', containing the removed rows.
        
        If 'original_file_option' is set to 'delete', the original file is deleted, and the cleaned file is renamed to '<original_file_name>'.
    """
    # Define the new file names for the cleaned file and the file with removed entries
    new_file_name = file_name[:-4] + '_new' + '.csv'
    removed_entries_file = 'removed_entries_' + string_to_remove + '.csv'
    
    # Open the original file, new file, and file for removed entries
    with open(file_name, 'r') as file, open(new_file_name, 'w') as new_file, open(removed_entries_file, 'w') as removed_entries:
        # Create CSV readers and writers
        reader = csv.reader(file)
        writer = csv.writer(new_file)
        removed_entries_writer = csv.writer(removed_entries)

        # Initialize a counter for removed rows
        row_count = 0
        # Convert the search string to lowercase for case-insensitive matching
        search_string_lower = string_to_remove.lower()

        # Iterate through each row in the original file
        for row in reader:
            # Convert the row to a list and make a lowercase version of it
            row_list = list(row)
            row_list_lower = [word.lower() for word in row_list]

            # Check if the search string is present in any word of the row (case-insensitive)
            if any(search_string_lower in word for word in row_list_lower):
                # If found, increment the counter, write the row to the file of removed entries, and skip to the next row
                row_count += 1
                removed_entries_writer.writerow(row)
                continue
            else:
                # If not found, write the row to the cleaned file
                writer.writerow(row)

        # Print the count of removed rows for the specified search string
        print(str(row_count) + ' x ' + string_to_remove)

    # If specified, delete the original file and rename the new file
    if original_file_option == 'delete':
        os.remove(file_name)
        os.rename(new_file_name, file_name)

# Example usage:
delete_row_with_string('redes neuronales', 'final.csv', 'delete')
