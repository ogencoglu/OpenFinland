'''
Author         : Oguzhan Gencoglu
Contact        : oguzhan.gencoglu@tut.fi
Created        : 16.11.2015
Latest Version : 16.11.2015
'''

# Import required packages
from __future__ import print_function
from set_wd import set_wd
import json
import numpy as np
from datetime import datetime
import itertools
import zipfile
import StringIO
 
                    
def extract_field(page, key):
    # returns a generator for all the "key" fields in a page
    # E.g. extract_field(data[0], 'body')
    
    if key in page:
        yield page[key]
    if 'comments' in page.keys():
        for comment in page['comments']:
            for gen in extract_field(comment, key):
                yield gen 
            

if __name__ == '__main__':
    
    # Read all json files from zip file without uncompressing
    page_count = 0
    post_count = 0
    zf = zipfile.ZipFile('Suomi24-2015-05-25_JSON.zip', 'r')
    for f in zf.namelist():
        start = datetime.now()
        print("\nReading", f)
        sio = StringIO.StringIO(zf.read(f))  
        data = json.load(sio)
        print("\tNumber of pages:", len(data))
        page_count = page_count + len(data)
        
        # extract all dates
        dates = []
        for page in data:
            dates.append(extract_field(page, 'created_at'))
        dates = list(itertools.chain.from_iterable(dates))
        print("\tNumber of messages:", len(dates))
        post_count = post_count + len(dates)
        dates_file = open(f[:-5] + '-dates.txt', 'w') 
        for item in dates:
            dates_file.write("%s\n" % str(item/1000))
        dates_file.close()
            
        stop = datetime.now()
        print("\t\tLoading Time: %s"%str(stop - start))
    zf.close()
    print("\nTotal number of pages:", page_count)
    print("\nTotal number of messages:", post_count)
