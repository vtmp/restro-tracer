# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import os
import csv
import logging

from rtracer import util

logging.basicConfig(level=logging.INFO)


def category_entry_to_set(entry):

    result = set()

    while len(entry) > 0:
        idx_start = entry.find('\'')
        idx_end = entry.find('\'', idx_start+1)
        
        if (idx_start != -1 and idx_end != -1):
            match = entry[idx_start+1:idx_end]
            result.add(match)
            entry = entry[idx_end+1:]
        else:
            return result

 
def get_business_ids_by_category(categories, csv_path_in):
    
    set_of_ids = set()
    counter = 0
    
    with open(csv_path_in, 'r') as csv_in:
        business_reader = csv.DictReader(csv_in, delimiter=',')
        
        for row in business_reader:
            logging.debug(row['categories'])
            category_tmp = category_entry_to_set(row['categories'])
            
            if len(categories.intersection(category_tmp)) > 0:
                set_of_ids.add(row['business_id'])
                counter += 1
                
    return set_of_ids
            

def write_csv_by_business_ids(set_of_ids, csv_path_in, csv_path_out):
    
    
    with open(csv_path_in, 'r') as csv_file_in, open(csv_path_out, 'w') as csv_file_out:    
        reader = csv.DictReader(csv_file_in, delimiter=',')        
        writer = csv.DictWriter(csv_file_out, fieldnames=reader.fieldnames)
    
        writer.writeheader()
        
        for row in reader:
            #print(row['business_id'])
            if row['business_id'] in set_of_ids:
                writer.writerow(row)
            
         
def write_filtered_by_category(categories, csv_folder_out):
    csv_folder_in = 'data_csv_small'
    
    path_business = os.path.join(util.get_data_path(), csv_folder_in, 'business.csv')
    set_of_ids = get_business_ids_by_category(categories, path_business)
    
    list_of_files = ['tip.csv', 'checkin.csv', 'review.csv', 'business.csv']
    
    for f in list_of_files:        
        path_in = os.path.join(util.get_data_path(), csv_folder_in, f)
        path_out = os.path.join(util.get_data_path(), csv_folder_out, f)
        
        write_csv_by_business_ids(set_of_ids,
                              csv_path_in=path_in,
                              csv_path_out=path_out)
                              

def main():
    
    categories = {'Restaurants'}
    write_filtered_by_category(categories, 'data_tmp')


if __name__ == '__main__':
    main()


            
        