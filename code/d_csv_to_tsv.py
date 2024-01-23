#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 03:01:02 2022

@author: Agustin Mauro
"""

import csv

def convert_csv_to_tsv(csv_file_name, tsv_file_name):
    """
    This function converts a csv file to a tsv file
    """
    with open(csv_file_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        with open(tsv_file_name, 'w') as tsv_file:
            tsv_writer = csv.writer(tsv_file, delimiter='\t')
            for row in csv_reader:
                tsv_writer.writerow(row)

convert_csv_to_tsv('final.csv', 'final.tsv')
