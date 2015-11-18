'''
Author         : Oguzhan Gencoglu
Contact        : oguzhan.gencoglu@tut.fi
Created        : 16.11.2015
Latest Version : 16.11.2015
'''

# Import required packages
from set_wd import set_wd
import numpy as np
import datetime as dt
import numpy as np
import zipfile
import StringIO
from add_to_path import add_to_path
add_to_path("Templates\Python\Dates")
from date_functions import int2date, parse_date_column
add_to_path("Templates\Python\Other")
from unique_rows import unique_rows
from itertools import groupby
import matplotlib.pyplot as plt

if __name__ == '__main__':
    
    '''
    zf = zipfile.ZipFile('all_dates.zip', 'r')
    for f in zf.namelist():
        sio = StringIO.StringIO(zf.read(f))  
        all_dates = sio.read().split('\r\n')[:-1]
    zf.close()
    
    all_dates = [int(x) for x in all_dates]
    all_dates_sorted = sorted(all_dates)
    all_dates_sorted = all_dates_sorted[132:] # remove wrong dates from 1970
    np.save('all_dates_sorted.npy', all_dates_sorted)
    '''
    
    # Read sorted dates
    all_dates_sorted = np.load('all_dates_sorted.npy') # contact me for the tidy data
    int2date_vec = np.vectorize(int2date)
    all_dates_sorted = int2date_vec(all_dates_sorted)
    
    # Parse date values
    all_dates_sorted = parse_date_column(all_dates_sorted, ['y', 'm', 'd', 'h', 'min'])
    calender = all_dates_sorted[:,:3]
    tod = all_dates_sorted[:,3:]
    
    # get unique rows and counts
    #uniq_calender = unique_rows(calender)
    #uniq_tod = unique_rows(tod)
    calender_date = [dt.date(calender[i,0], calender[i,1], calender[i,2]) for i in range(calender.shape[0])]
    uniq_calender = np.array(sorted(set(calender_date)))
    uniq_calender_count = [len(list(g)) for k, g in groupby(calender_date)]
    tod_mins = np.sort(tod[:,0]*60 + tod[:,1])
    uniq_tod_mins = np.array(sorted(set(tod_mins)))
    uniq_tod_count = np.array([len(list(g)) for k, g in groupby(tod_mins)])
    
    
    # Time of the day plot
    plt.figure()
    plt.scatter(uniq_tod_mins/60.0, uniq_tod_count/float(np.sum(uniq_tod_count)),  alpha=0.5)
    plt.xlabel("Time of the day", fontsize=17)
    plt.title("Probability Distribution", fontsize=20)
    plt.axis([-0.5, 24.5, 0, 1.3e-3]) 
    ax = plt.gca()
    ax.grid(True)
    plt.show()
    
    # History of number of posts plot
    plt.figure()
    plt.plot(uniq_calender, np.cumsum(uniq_calender_count))
    plt.xlabel("Date", fontsize=17)
    plt.ylabel("Cumulative Number of Posts", fontsize=17)
    plt.title("History of Suomi24", fontsize=20)
    ax = plt.gca()
    ax.fill_between(uniq_calender, 0, np.cumsum(uniq_calender_count), alpha=0.3)
    ax.grid(True)
    plt.show()    


    