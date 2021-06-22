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


#%% Function to calculate energy

def powerUp(x):
    try:
        y = 10**(x/10)
    except:
        y = 0
    return y

def get_10min_data(fd_index, total_items, item_number, fd, fl):
    print('{0:2d}\t\t{1:2d}\t{2:2d}'.format(fd_index, total_items, item_number), end="")
    df_info = pd.read_excel(os.path.join(fd, fl), ten_min_sheet, nrows=1)
    data_items = df_info.iloc[0,0]
    data_cols =  df_info.columns[1]
    print('\t{0:4d}\t{1:4d}'.format(data_items, data_cols), end="")
    print('\t{0:s}'.format(fl))
    df = pd.read_excel(os.path.join(fd, fl), ten_min_sheet, skiprows=1)
    df.drop(labels=['Markers', 'LAFmax [dB]', 'LAFmin [dB]'], axis=1, inplace=True)
    df = df.rename(columns={df.columns[1] : 'DateTime'})
    df['DateTime'] = pd.to_datetime(df['DateTime'], format = r'%d.%m.%Y %H:%M:%S.%f')
    df.index = df['DateTime']
    df.drop(labels=[df.columns[0], 'DateTime'], axis=1, inplace=True)
    if len(df) != data_items:
        print('Lost data items: XLS:{1:6d} DF:{2:6d}'.format(data_items, len(df)))
    return(df)

def filter_10min_data(df):
    df.sort_values(by='DateTime', inplace = True)  # Sort data in data order
    df = df.resample('10T').mean()                 # Pad data to provide continuous record (Maybe add -99.99)
    return(df)

def write_10min_csv(df, file_name):
    file_name = 'VF-' + file_name + '-10min.csv'
    # data.to_csv(os.path.join(write_folder, file_name), date_format = r'%H:%M %d/%m/%Y')
    df.to_csv(os.path.join(write_folder, file_name), date_format = r'%H:%M')

def plot_10min(df, date):
    # Plot results of overall assessment
    plt.figure()
    #plt.axis([2,12,20,60])
    plt.plot(df['LAeq [dB]'], 'ro-', label='10min SPL', linewidth=2)
    plt.xlabel('Time of Day')
    plt.ylabel('Sound Pressure Level / dB(A) re. 20 uPa')
    plt.grid('on', which=u'major', axis=u'both')
    plt.title('NOISE ASSEESSMENT AT VARDAFJELLET: Date: {0}'.format(date))
    plt.legend(loc='best')
    return()


#%% - Read main input text file

if G_DEBUG:
    t0 = dt.datetime.now()
print("INFORMATION: Importing A-weighted data from Norsonics files...  \n\n")

#Create header line for output data
print("Index","\tTotal Files","\tFile#","\tLines","\tColumns","\tFile Name")

# Cycle through necessary folders and add data into Pandas dataframe
for folder_index, folder in enumerate(data_folders):
    if not processed[folder_index]: 
        if type(folder) is list:
            for index, item in enumerate(folder):                                       # Read in 10 min data from xlsx
                temp_data = get_10min_data(folder_index, len(folder), index+1, item, data_files[folder_index][index])
                if index == 0:                                                          # Combine data into single file
                    data = temp_data
                else:
                    data = pd.concat([data, temp_data])
                del temp_data
            fname = data_files[folder_index][index][0:10]
        else:
            data = get_10min_data(folder_index, 1, 1, folder, data_files[folder_index]) # Read in 10 min data from xlsx
            fname = data_files[folder_index][0:10]
            
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