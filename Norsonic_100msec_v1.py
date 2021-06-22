# -*- coding: utf-8 -*-
"""
Program created to read all 100 msec data from daily XLSX files from Norsonic 145 SLM at Vardfjellet and
to combine it and then to spit out daily files suitable for analysis by the IOA AMWG software.

Created on Mon Marn 08 09:10:06 2021

Columns:
864000		Markers	LAeq [dB]	LAFmax [dB]	LAFmin [dB]
Lfeq 6.30 Hz (1/3) [dB]	Lfeq 8 Hz (1/3) [dB]	Lfeq 10 Hz (1/3) [dB]	Lfeq 12.5 Hz (1/3) [dB]	Lfeq 16 Hz (1/3) [dB]	Lfeq 20 Hz (1/3) [dB]	Lfeq 25 Hz (1/3) [dB]	Lfeq 31.5 Hz (1/3) [dB]	Lfeq 40 Hz (1/3) [dB]	Lfeq 50 Hz (1/3) [dB]	Lfeq 63 Hz (1/3) [dB]	Lfeq 80 Hz (1/3) [dB]	Lfeq 100 Hz (1/3) [dB]	Lfeq 125 Hz (1/3) [dB]	Lfeq 160 Hz (1/3) [dB]	Lfeq 200 Hz (1/3) [dB]	Lfeq 250 Hz (1/3) [dB]	Lfeq 315 Hz (1/3) [dB]	Lfeq 400 Hz (1/3) [dB]	Lfeq 500 Hz (1/3) [dB]	Lfeq 630 Hz (1/3) [dB]	Lfeq 800 Hz (1/3) [dB]	Lfeq 1 kHz (1/3) [dB]	Lfeq 1.25 kHz (1/3) [dB]	Lfeq 1.6 kHz (1/3) [dB]	Lfeq 2 kHz (1/3) [dB]	Lfeq 2.5 kHz (1/3) [dB]	Lfeq 3.15 kHz (1/3) [dB]	Lfeq 4 kHz (1/3) [dB]	Lfeq 5 kHz (1/3) [dB]	Lfeq 6.3 kHz (1/3) [dB]	Lfeq 8 kHz (1/3) [dB]	Lfeq 10 kHz (1/3) [dB]	Lfeq 12.5 kHz (1/3) [dB]	Lfeq 16 kHz (1/3) [dB]	Lfeq 20 kHz (1/3) [dB]
LfFmax 6.30 Hz (1/3) [dB]	LfFmax 8 Hz (1/3) [dB]	LfFmax 10 Hz (1/3) [dB]	LfFmax 12.5 Hz (1/3) [dB]	LfFmax 16 Hz (1/3) [dB]	LfFmax 20 Hz (1/3) [dB]	LfFmax 25 Hz (1/3) [dB]	LfFmax 31.5 Hz (1/3) [dB]	LfFmax 40 Hz (1/3) [dB]	LfFmax 50 Hz (1/3) [dB]	LfFmax 63 Hz (1/3) [dB]	LfFmax 80 Hz (1/3) [dB]	LfFmax 100 Hz (1/3) [dB]	LfFmax 125 Hz (1/3) [dB]	LfFmax 160 Hz (1/3) [dB]	LfFmax 200 Hz (1/3) [dB]	LfFmax 250 Hz (1/3) [dB]	LfFmax 315 Hz (1/3) [dB]	LfFmax 400 Hz (1/3) [dB]	LfFmax 500 Hz (1/3) [dB]	LfFmax 630 Hz (1/3) [dB]	LfFmax 800 Hz (1/3) [dB]	LfFmax 1 kHz (1/3) [dB]	LfFmax 1.25 kHz (1/3) [dB]	LfFmax 1.6 kHz (1/3) [dB]	LfFmax 2 kHz (1/3) [dB]	LfFmax 2.5 kHz (1/3) [dB]	LfFmax 3.15 kHz (1/3) [dB]	LfFmax 4 kHz (1/3) [dB]	LfFmax 5 kHz (1/3) [dB]	LfFmax 6.3 kHz (1/3) [dB]	LfFmax 8 kHz (1/3) [dB]	LfFmax 10 kHz (1/3) [dB]	LfFmax 12.5 kHz (1/3) [dB]	LfFmax 16 kHz (1/3) [dB]	LfFmax 20 kHz (1/3) [dB]
LfFmin 6.30 Hz (1/3) [dB]	LfFmin 8 Hz (1/3) [dB]	LfFmin 10 Hz (1/3) [dB]	LfFmin 12.5 Hz (1/3) [dB]	LfFmin 16 Hz (1/3) [dB]	LfFmin 20 Hz (1/3) [dB]	LfFmin 25 Hz (1/3) [dB]	LfFmin 31.5 Hz (1/3) [dB]	LfFmin 40 Hz (1/3) [dB]	LfFmin 50 Hz (1/3) [dB]	LfFmin 63 Hz (1/3) [dB]	LfFmin 80 Hz (1/3) [dB]	LfFmin 100 Hz (1/3) [dB]	LfFmin 125 Hz (1/3) [dB]	LfFmin 160 Hz (1/3) [dB]	LfFmin 200 Hz (1/3) [dB]	LfFmin 250 Hz (1/3) [dB]	LfFmin 315 Hz (1/3) [dB]	LfFmin 400 Hz (1/3) [dB]	LfFmin 500 Hz (1/3) [dB]	LfFmin 630 Hz (1/3) [dB]	LfFmin 800 Hz (1/3) [dB]	LfFmin 1 kHz (1/3) [dB]	LfFmin 1.25 kHz (1/3) [dB]	LfFmin 1.6 kHz (1/3) [dB]	LfFmin 2 kHz (1/3) [dB]	LfFmin 2.5 kHz (1/3) [dB]	LfFmin 3.15 kHz (1/3) [dB]	LfFmin 4 kHz (1/3) [dB]	LfFmin 5 kHz (1/3) [dB]	LfFmin 6.3 kHz (1/3) [dB]	LfFmin 8 kHz (1/3) [dB]	LfFmin 10 kHz (1/3) [dB]	LfFmin 12.5 kHz (1/3) [dB]	LfFmin 16 kHz (1/3) [dB]	LfFmin 20 kHz (1/3) [dB]

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


#%% Function to calculate energy

def powerUp(x):
    try:
        y = 10**(x/10)
    except:
        y = 0
    return y

def get_100ms_data(fd_index, total_items, item_number, fd, fl):
    print('{0:2d}\t\t{1:2d}\t{2:2d}'.format(fd_index, total_items, item_number), end="")
    df = pd.read_excel(os.path.join(fd, fl), raw_data_sheet, skiprows=1)                 # Working version of code
    # df = pd.read_excel(os.path.join(fd, fl), raw_data_sheet, skiprows=1, nrows=20)      # Use following for testing only
    print('\t{0:6d}\t{1:4d}\t{2:s}'.format(len(df), 112, fl))
    df.drop(labels=['Markers', 'LAFmax [dB]', 'LAFmin [dB]'], axis=1, inplace=True)

    # Remove unecessary LfFMin & LdFMax columns
    remove_columns = []
    for col in df.columns:
        if type(col) is str:
            if 'LfFmax' in col:
                remove_columns.append(col)
            if 'LfFmin' in col:
                remove_columns.append(col)
    df.drop(labels = remove_columns, axis=1, inplace=True)

    # Remove unecessary Lfeq columns
    remove_columns = [ 'Lfeq 6.30 Hz (1/3) [dB]',     'Lfeq 8 Hz (1/3) [dB]',   'Lfeq 10 Hz (1/3) [dB]', 'Lfeq 12.5 Hz (1/3) [dB]',    'Lfeq 16 Hz (1/3) [dB]',
                         'Lfeq 20 Hz (1/3) [dB]',    'Lfeq 25 Hz (1/3) [dB]', 'Lfeq 31.5 Hz (1/3) [dB]',   'Lfeq 40 Hz (1/3) [dB]',    'Lfeq 1 kHz (1/3) [dB]',
                      'Lfeq 1.25 kHz (1/3) [dB]',  'Lfeq 1.6 kHz (1/3) [dB]',   'Lfeq 2 kHz (1/3) [dB]', 'Lfeq 2.5 kHz (1/3) [dB]', 'Lfeq 3.15 kHz (1/3) [dB]',
                         'Lfeq 4 kHz (1/3) [dB]',    'Lfeq 5 kHz (1/3) [dB]', 'Lfeq 6.3 kHz (1/3) [dB]',   'Lfeq 8 kHz (1/3) [dB]',   'Lfeq 10 kHz (1/3) [dB]',
                      'Lfeq 12.5 kHz (1/3) [dB]',   'Lfeq 16 kHz (1/3) [dB]',  'Lfeq 20 kHz (1/3) [dB]']
    df.drop(labels = remove_columns, axis=1, inplace=True)

    df = df.rename(columns={df.columns[1] : 'Timestamp'})
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format = r'%d.%m.%Y %H:%M:%S.%f')
    df.index = df['Timestamp']
    df.drop(labels=[df.columns[0], 'Timestamp'], axis=1, inplace=True)
    return(df)

def filter_100ms_data(df):
    df.sort_values(by='Timestamp', inplace = True)  # Sort data in data order
    df = df.resample('100L').mean()                 # Pad data to provide continuous record (Maybe add -99.99)
    return(df)

def apply_AWeight(df, AWeight):
    for col_index, col in enumerate(df.columns):
        # print('AW: ', col_index, col)
        df[col] = df[col] + AWeight[col_index]
    return(df)

def add_third_octave_bands(usecols, df, new_label):
    df['Sum'] = 0
    # for col in all_data.columns[1:8]:
    for col in usecols:
        df['Sum'] += df[col].apply(powerUp)
    df['Sum'] = 10.0*df['Sum'].apply(np.log10)
    df = df.rename(columns={'Sum' : new_label})
    return(df)

def write_100ms_csv(df, file_name, label):
    # Only retain columns which are needed
    # df = df[['Timestamp', 'LAeq']]
    if label[-2] == '-':
        file_name = 'VF-' + file_name + '-100msec' + label[-2:] + '.csv'
    else:
        file_name = 'VF-' + file_name + '-100msec.csv'
    df.to_csv(os.path.join(write_folder, file_name), columns=[label], index=True, date_format=r'%H:%M:%S.%f', float_format='%.2f')

def plot_100ms(df, date):
    df = df.resample('1T').mean()
    # Plot results of overall assessment   
    plt.figure()
    #plt.axis([2,12,20,60])
    plt.plot(df['LAeq [dB]'], 'k-', label= 'A-Weight', linewidth=1)
    plt.plot(df['LAeq-A'],    'r-', label= '50-200Hz', linewidth=1)
    plt.plot(df['LAeq-B'],    'b-', label='100-400Hz', linewidth=1)
    plt.plot(df['LAeq-C'],    'g-', label='200-800Hz', linewidth=1)
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
                temp_data = get_100ms_data(folder_index, len(folder), index+1, item, data_files[folder_index][index])
                if index == 0:                                                          # Combine data into single file
                    data = temp_data
                else:
                    data = pd.concat([data, temp_data])
                del temp_data
            fname = data_files[folder_index][index][0:10]
        else:
            data = get_100ms_data(folder_index, 1, 1, folder, data_files[folder_index])   # Read in 10 min data from xlsx
            fname = data_files[folder_index][0:10]

        data = apply_AWeight(data, AWeighting)                                            # Apply A-weighting to 1/3 octave bands
        data = add_third_octave_bands(usecols_A, data, 'LAeq-A')                          #  50 - 200 Hz from octave bands
        data = add_third_octave_bands(usecols_B, data, 'LAeq-B')                          # 100 - 400 Hz from octave bands
        data = add_third_octave_bands(usecols_C, data, 'LAeq-C')                          # 200 - 800 Hz from octave bands
        data = filter_100ms_data(data)                                                    # Arrange in date order and pad to 10m intervals
        write_100ms_csv(data, fname, 'LAeq [dB]')                                         # Create csv of A-weighted data
        write_100ms_csv(data, fname, 'LAeq-A')                                            # Create csv of  50-200 Hz data
        write_100ms_csv(data, fname, 'LAeq-B')                                            # Create csv of 100-400 Hz data
        write_100ms_csv(data, fname, 'LAeq-C')                                            # Create csv of 200-800 Hz data
        plot_100ms(data, fname)                                                           # Plot daily data
        del data

# Show all plots
plt.show()

if G_DEBUG:
    t1 = dt.datetime.now()
    time_required = (t1-t0).total_seconds()*1.0/60.
    print("\nTime required: {0:.4} minutes".format(time_required))