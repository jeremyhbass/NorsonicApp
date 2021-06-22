#%% - Import all necessary modules
from __future__ import division
# Standard modules
import pandas as pd
import datetime as dt
import numpy as np
import os                          # Note: os.walk is very slow

# Non-standard modules
# import scandir                     # Used in preference as much faster - https://stackoverflow.com/questions/32455262/os-walk-very-slow-any-way-to-optimise
import Tkinter as tk               # GUI creation
import tkMessageBox                # Windows message box

# Local modules
from constants import *


#%% Helper function to combine levels from multiple octave bands
def powerUp(x):
    try:
        return 10**(x/10)
    except:
        return 0


#%% Create messagebox in tkMessagebox to give user information

def messageBox(boxType, title, message):
    top = tk.Tk()
    top.withdraw()
    if boxType.lower() == 'error':
        tkMessageBox.showerror(title, message)
    elif boxType.lower() == 'warning':
        tkMessageBox.showwarning(title, message)
    elif boxType.lower() == 'information':
        tkMessageBox.showinfo(title, message)
    else:                                  # Now hide it
        print 'Message box type unknown'
    top.destroy()


#%% Used to parse data within pandas df

# Read main (second) part of data block containing 1/3 OB data
def parse_block(df):
    # Note - LN1=L1, LN2=L10, LN3=L50,LN4=L90 & LN5=L99
    df.index = df[df.columns[0]]
    df.drop([df.columns[0]], inplace=True, axis=1)
    for col in df.columns:
        if NO_ENTRY in str(df[col].values):
            df[col] = pd.to_numeric(df[col], errors = 'coerce')
    return df


# Function to ensure data is in correct time/date order    
def reorder(df):
    print "INFORMATION: Resequencing data...           ",
    #df.sort_values(by='Start Time', inplace = True)
    df.sort_index(inplace = True)                    # Make sure data is arranged in data order
    print "...complete."
    return df


# Function to pad data so that it provides a continuous time/date record (with blank padded missing data)
def pad(df):
    print "INFORMATION: Padding data...                ",
    df = df.resample('100L').pad(limit=1)
    if G_DEBUG: print 'Total number of lines of 10 min data -   padded: {}'.format(len(df))
    print "...complete."
    return df


# Function to pad data so that it provides a continuous time/date record (with blank padded missing data)
def filter(df):
    print "INFORMATION: Filtering data...              ",
    if G_RANGE == 0:
        df = df[['Partial Over All']]
    elif G_RANGE == 1:
        df = df[['50 Hz','63 Hz','80 Hz','100 Hz','125 Hz','160 Hz','200 Hz']]
    elif G_RANGE == 2:
        df = df[['100 Hz','125 Hz','160 Hz','200 Hz','250 Hz','315 Hz','400 Hz']]
    elif G_RANGE == 3:
        df = df[['200 Hz','250 Hz','315 Hz','400 Hz','500 Hz','630 Hz','800 Hz']]
    else:
        if G_DEBUG: print 'WARNING: Illegal G_RANGE value entered: {:d}'.format(G_RANGE)
    # Now combine 1/3 octave band levels
    if G_RANGE in {1, 2, 3}:
        # Now form energetic / logarithmic sum of octave bands, which are already A-weighted for Rion
        df = df.assign(Sum = lambda x: 0.0)
        for col in df.columns[0:7]:
            df['Sum'] += df[col].apply(powerUp)
        df['Sum'] = (df['Sum'].apply(np.log10)) * 10.0
        df = df.rename(columns={'Sum'              : 'LAeq'})
    else:
        # Now rename columns to something standard
        df = df.rename(columns={'Partial Over All' : 'LAeq'})
    # Only retain columns which are needed
    df = df[['LAeq']]
    print "...complete."
    return df


# Write out data in single, nicely formatted output file
def write_data(df,output_folder):
    print "INFORMATION: Writing data..."
    dates = df.index
    startDay = dt.datetime(df.index.min().year,df.index.min().month,df.index.min().day)
    stopDay = dt.datetime(df.index.max().year,df.index.max().month,df.index.max().day)
    day = dt.timedelta(days=1)
    date1 = startDay
    #Create header line for output file data
    print "\nFilename","\t\tDate","\tItems","\t% Complete","\tStart Date","\t\tStop Date"
    while date1 <= stopDay:
        dailyData = df[(dates >= date1) & (dates < (date1 + day))]
        if G_RANGE   == 0: # 100 - 400 Hz from Parial Over All
            output_file =  'data-' + date1.strftime('%Y-%m-%d') + '-Partial.csv'
        if G_RANGE   == 1: #  50 - 200 Hz from octave bands
            output_file =  'data-' + date1.strftime('%Y-%m-%d') + '-50_200.csv'
        elif G_RANGE == 2: # 100 - 400 Hz from octave bands
            output_file =  'data-' + date1.strftime('%Y-%m-%d') + '-100_400.csv'
        elif G_RANGE == 3: # 200 - 800 Hz from octave bands
            output_file =  'data-' + date1.strftime('%Y-%m-%d') + '-200_800C.csv'
        else:              # Unknown
            output_file =  'data-' + date1.strftime('%Y-%m-%d') + '.csv'
        print output_file,
        print "\t" + date1.strftime('%Y-%m-%d'),
        print "\t%s" % str(len(dailyData)),
        print "\t%5.1f" % (float(100*len(dailyData))/float(DAILY_ITEMS)),
        print "\t", date1,
        print "\t", date1 + day
        dailyData.to_csv(os.path.join(output_folder,output_file),
                         index=True, 
                         date_format = '%d/%m/%y %H:%M:%S.%f',
                         index_label = 'Start Time',
                         float_format = '%.1f')
        date1 = date1 + day
    return


if __name__ == "__main__":
    print 'ALERT! - Please note that you are running this function module directly!!!'
    print 'ALERT! -'
    print 'ALERT! - The intention is that this function module is imported into other code,'
    print 'ALERT! - and not run directly as a stand-alone piece of code.'