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
from bokeh.plotting import figure
from bokeh.io import output_file, show, save, curdoc
from bokeh.models import Range1d
from bokeh.models.sources import ColumnDataSource
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
    sl, tl = fileParser(os.path.join(fd, fl))
    print('{0:2d}\t{1:2d}\t{2:2d}'.format(fd_index, total_items, item_number), end="")
    df =   pd.read_csv(os.path.join(fd, fl), sep='\t', skiprows=sl+tl+4, header=None, names=octave_headers, engine='python') # Working version of code
    print('\t{0:6d}\t{1:4d}\t{2:s}'.format(len(df), 112, fl))
    # print(df.head())
    # print(df.tail())
    # print(df.dtypes)
    # print(df.columns)
    df.drop(labels=['LAFmax [dB]', 'LAFmin [dB]'], axis=1, inplace=True)

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

    # df = df.rename(columns={df.columns[] : 'Timestamp'})
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format = r'%Y-%m-%d %H:%M:%S.%f')
    df.index = df['Timestamp']
    df.drop(labels=[df.columns[0], 'Timestamp'], axis=1, inplace=True)
    # Replace any noentry values with Nan
    df[df<-99] = np.NaN
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

    # Prepare the output file
    output_file('{0}.html'.format(date))
    curdoc().theme = 'light_minimal'
  
    x = pd.date_range('0:00:30', '23:59:30', freq='1T')

    # Create a figure object
    f = figure(title='NOISE ASSESSMENT AT VARDAFJELLET: Date: {0}'.format(date),
                          x_axis_type="datetime",
                          plot_width=1800,
                          plot_height=900)
    y = df['LAeq [dB]']
    f.line(x=x, y=y, color="black", line_width = 1, legend_label= 'A-Weight')
    y = df['LAeq-A']
    f.line(x=x, y=y, color=  "red", line_width = 1, legend_label= '50-200Hz')
    y = df['LAeq-B']
    f.line(x=x, y=y, color= "blue", line_width = 1, legend_label='100-400Hz')
    y = df['LAeq-C']
    f.line(x=x, y=y, color="green", line_width = 1, legend_label='200-800Hz')
    
    f.sizing_mode = "stretch_both"
    f.title.text_font_size = "30px"           # Text / font size
    f.title.align = "center"                  # Location of title
    f.xaxis.axis_label = 'Time of Day'
    f.yaxis.axis_label = 'Sound Pressure Level / dB(A) re. 20 uPa'
    f.x_range = Range1d(start=x[0], end=x[-1])
    f.xaxis[0].ticker.desired_num_ticks = 12
    f.xaxis[0].ticker.num_minor_ticks = 2
    f.grid.grid_line_color = "gray"                 # Define line colour for both axes
    f.grid.grid_line_alpha = 0.95                   # Define line transparency for both axes
    f.grid.grid_line_dash = [5, 3]                  # Define dash line ratio in pixels for both axes
    f.legend.location = "top_right"                 # Location in text
    f.outline_line_color = 'black'
    show(f)
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
        data = get_100ms_data(folder_index, 1, 1, text_folders, folder)  # Read in 10 min data from xlsx
        fname = folder[11:21]
        data = apply_AWeight(data, AWeighting)                           # Apply A-weighting to 1/3 octave bands
        data = add_third_octave_bands(usecols_A, data, 'LAeq-A')         #  50 - 200 Hz from octave bands
        data = add_third_octave_bands(usecols_B, data, 'LAeq-B')         # 100 - 400 Hz from octave bands
        data = add_third_octave_bands(usecols_C, data, 'LAeq-C')         # 200 - 800 Hz from octave bands
        data = filter_100ms_data(data)                                   # Arrange in date order and pad to 10m intervals
        write_100ms_csv(data, fname, 'LAeq [dB]')                        # Create csv of A-weighted data
        write_100ms_csv(data, fname, 'LAeq-A')                           # Create csv of  50-200 Hz data
        write_100ms_csv(data, fname, 'LAeq-B')                           # Create csv of 100-400 Hz data
        write_100ms_csv(data, fname, 'LAeq-C')                           # Create csv of 200-800 Hz data
        plot_100ms(data, fname)                                          # Plot daily data
        del data

if G_DEBUG:
    t1 = dt.datetime.now()
    time_required = (t1-t0).total_seconds()*1.0/60.
    print("\nTime required: {0:.4} minutes".format(time_required))