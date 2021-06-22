# -*- coding: utf-8 -*-
"""
Program created to read all 100 msec data from daily XLSX files from Norsonic 145 SLM at Vardfjellet and
to combine it and then to spit out daily files suitable for analysis by the IOA AMWG software.

Created on Mon Marn 08 09:10:06 2021

@author: bass
"""

#%% - Import all necessary modules

print("INFORMATION: Importing modules...                             ", end="")
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
print("...complete.")

# Local modules
from constants import *
# from functions import *


#%% Define necessary functions

def get_10min_data(fd_index, total_items, item_number, fd, fl):
    sl, tl = fileParser(os.path.join(fd, fl))
    print('{0:2d}\t{1:2d}\t{2:2d}'.format(fd_index, total_items, item_number), end="")
    data_cols =  3
    print('\t{0:4d}\t{1:4d}\t{2:s}'.format(tl, data_cols, fl))
    df = pd.read_csv(os.path.join(fd, fl), sep='\t', skiprows=sl, nrows=tl, engine='python')
    df.drop(labels=['SVG145-3 LAFmax', 'SVG145-3 LAFmin'], axis=1, inplace=True)
    df = df.rename(columns={df.columns[0] : 'DateTime'})
    df = df.rename(columns={df.columns[1] : 'LAeq [dB]'})
    df['DateTime'] = pd.to_datetime(df['DateTime'], format = r'%Y-%m-%d %H:%M:%S.%f')
    df.index = df['DateTime']
    df.drop(labels=['DateTime'], axis=1, inplace=True)
    if len(df) != tl:
        print('Lost data items: XLS:{1:6d} DF:{2:6d}'.format(tl, len(df)))
    return(df)

def filter_10min_data(df):
    df.sort_values(by='DateTime', inplace = True)  # Sort data in data order
    df = df.resample('10T').mean()                 # Pad data to provide continuous record (Maybe add -99.99)
    return(df)

def write_10min_csv(df, file_name):
    file_name = 'VF-' + file_name + '-10min.csv'
    # data.to_csv(os.path.join(write_folder, file_name), date_format = r'%H:%M %d/%m/%Y')
    df.to_csv(os.path.join(write_folder, file_name), date_format=r'%H:%M', float_format='%.1f')

def plot_10min(df, date):
    # Plot results of overall assessment
    plt.figure()
    plt.plot(df['LAeq [dB]'], 'ro-', label='10min SPL', linewidth=2)
    plt.xlabel('Time of Day')
    plt.ylabel('Sound Pressure Level / dB(A) re. 20 uPa')
    plt.grid('on', which=u'major', axis=u'both')
    plt.title('NOISE ASSEESSMENT AT VARDAFJELLET: Date: {0}'.format(date))
    plt.legend(loc='best')
    return()

def fileParser(filePathName):   
    with open(filePathName,'r') as f:   
        
        ## Determine value of 'Markers:'
        #Discard 3 blank lines
        for line in range(3):
            f.readline()
        #Read 'Markers' on line 4
        data  = f.readline()
        data = data.split(':')
        fl = int(data[1]) + 6

        ## Determine line number of 10 min data - 'ProfileB:'
        ln = 4
        sl = ''
        while sl != 'ProfileB':
            data = f.readline()
            data = data.split(':')
            sl = data[0]
            ln += 1
        sl = int(ln)
        if sl != fl:
            print('xxx')

        ## Determine line number of 100 msec data - 'Profile:'
        tl = ''
        while tl != 'Profile':
            data = f.readline()
            data = data.split(':')
            tl = data[0]
            ln += 1
        tl = int(ln)
        tl = tl - sl - 3

    f.close()

    return(sl, tl)


#%% - Read main input text file

if G_DEBUG:
    t0 = dt.datetime.now()
print("INFORMATION: Importing A-weighted data from Norsonics files...  \n\n")

#Create header line for output data
print("Index\tTotal\tFile\tLines\tColumns\tFile Name")

# Cycle through necessary folders and add data into Pandas dataframe
for folder_index, folder in enumerate(text_files):
    if not text_processed[folder_index]:
        if G_DEBUG:
            print(data_folders, '\t',folder, end="")
        data = get_10min_data(folder_index, 1, 1, text_folders, folder) # Read in 10 min data from xlsx
        fname = folder[11:21]           
        data = filter_10min_data(data)                                                  # Arrange in date order and pad to 10m intervals
        write_10min_csv(data, fname)                                                    # Create csv of dataframe
        plot_10min(data, fname)                                                         # Plot daily data
        del data

# Show all plots
plt.show()

if G_DEBUG:
    t1 = dt.datetime.now()
    time_required = (t1-t0).total_seconds()*1.0/60.
    print("\nTime required: {0:.4} minutes".format(time_required))