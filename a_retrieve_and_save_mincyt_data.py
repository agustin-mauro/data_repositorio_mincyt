#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:35:35 2024

@author: madam
"""

import urllib.request
import urllib.parse
import json

def retrieve_and_save_mincyt(query, results_per_page, start_page):
    """
    This function queries the MINCyT digital repositories using a specified search query,
    retrieves the data for all pages, and saves it to a single JSON file.

    Parameters:
    - query (str): The search query to be used.
    - results_per_page (str): The number of results to be retrieved per page.
    - start_page (str): The starting page number of results to be retrieved.

    For processing the data there is a complementary script called
    '2_data_extractor.py'
    """
    # URL template for MINCyT API
    mincyt_url = "https://repositoriosdigitales.mincyt.gob.ar/vufind/api/v1/search?{}"

    # Initialize an empty list to accumulate data from different pages
    all_data = []

    # Making a request to the MINCyT API with the provided parameters
    query_params = urllib.parse.urlencode({
        'lookfor': query,
        'type': 'AllFields',
        'sort': 'year asc',
        'prettyPrint': 'true',
        'limit': results_per_page,
        'page': start_page
    })

    with urllib.request.urlopen(mincyt_url.format(query_params)) as url:
        first_page_data = json.load(url)
#        print(first_page_data)

        # Append the data for the current page to the list
        all_data.extend(first_page_data.get('records', []))
        
        # Calculate the total number of pages needed to retrieve all results
        result_count = first_page_data.get('resultCount', 0)
        total_pages = (result_count + int(results_per_page)) // int(results_per_page)

        print(f"Total pages needed: {total_pages}")

        # Iterate over the pages and retrieve the results
        for page_number in range(2, total_pages + 1):
            with urllib.request.urlopen(mincyt_url.format(query_params + f'&page={page_number}')) as page_url:
                page_data = json.load(page_url)

                # Append the data for the current page to the list
                all_data.extend(page_data.get('records', []))

    # Save the accumulated data to a single JSON file
    with open('all_data.json', 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=4)

    print("Data retrieval and processing complete.")

# Example usage of the function
retrieve_and_save_mincyt("neuro*", "1000", "1")
