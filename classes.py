#%% - Import all necessary modules
from __future__ import division
# Standard modules
import pandas as pd
import datetime as dt
import numpy as np
import os                          # Note: os.walk is very slow

# Non-standard modules
# import scandir                     # Used in preference as much faster - https://stackoverflow.com/questions/32455262/os-walk-very-slow-any-way-to-optimise

# Local modules
from constants import *
from functions import *


#%% Define classes for reading data files

#Define class relating to a specific datafile containing blocks of 10 min data
class File_Data(object):

    # Main initiation routine
    def __init__(self, file_name):
        self.file_name = file_name  # Full file name and path for datafile
        self.total_lines = 0        # No. of lines of data read from datafile
        return

    def __str__(self):
        return '{} {}'.format(self.file_name, self.total_lines)
    
    def get_block(self):
        try:
            block = pd.read_csv(self.file_name, skiprows=1, sep=',', low_memory=False, na_values = NO_ENTRY)
            block = parse_block(block)
            if G_DEBUG: print block
            self.total_lines += len(block)
            self.block = block
            return True        # All well
        except:
            if G_DEBUG: print 'TERMINATING: End of data...'
            return False        # Error reading block


# Define class relating to object containing all blocks of 10 min data from all data files
class All_Data(object):

    # Initialise the container which will hold all the available data
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.total_lines = 0  # Total no. of lines of data from individual datafiles
        self.total_files = 0  # Total number of files read
        self.files = []       # List of data files
        return

    def __str__(self):
        return '{} {} {} {}'.format(self.input_folder, self.output_folder, 
                                          self.total_lines, self.total_files)

    # Fill class object with all available data from individual file
    def get_file(self,name):
        if G_DEBUG: print 'In get_file'
        try:
            file = File_Data(file_name = name)
            read_data_ok = file.get_block()
            if read_data_ok:
                self.files.append(file)
                self.total_lines += file.total_lines
                self.total_files += 1
            return True
        except:
            if G_DEBUG: print 'TERMINATING: End of files...'
            return False

    # Fill class object with data from all available files
    def populate(self):
        if G_DEBUG: print 'In populate'
        print 'Folder Name','\t'*13,'     Files\t       Lines'  #Create header line for output data
        # Cycle through necessary folders and add data into Pandas dataframe
        for folder_name, subfolder_list, file_list in scandir.walk(self.input_folder):
            if folder_name.endswith('AUTO_LP'):
                if G_DEBUG: print '{}'.format(folder_name)
                if len(subfolder_list) > 0:
                    for subfolder in subfolder_list:
                        print 'WARNING: Unexpected folder in {} called {}'.format(folder_name, subfolder)
                for file in file_list:
                    file_name = os.path.join(folder_name,file)
                    read_file_ok = self.get_file(file_name)
                    if not read_file_ok:
                        break
                print '{:s}\t{:>10d}\t{:>12d}'.format(folder_name, self.total_files, self.total_lines)
                # if self.total_files >= 10:
                #     break
        return

    # Convert collections of class objects to a single dataframe for ease of use
    def write_to_pandas(self):
        if G_DEBUG: print 'In write_to_pandas'
        first_time = True
        for file in self.files:
            if first_time:
                df = file.block
                first_time = False
            else:
                df  = pd.concat([df, file.block])
        # Make 'Start Time' the dataframe's index
        df['Start Time'] = pd.to_datetime(df['Start Time'],format = '%Y/%m/%d %H:%M:%S') #Start Time,2015/12/02 12:30:00.1
        df.index = df['Start Time']
        df.drop(['Start Time'], inplace=True, axis=1)
        return df    # Return modified dataframe


if __name__ == "__main__":
    print 'ALERT! - Please note that you are running this class module directly!!!'
    print 'ALERT! -'
    print 'ALERT! - The intention is that class this module is imported into other code,'
    print 'ALERT! - and not run directly as a stand-alone piece of code.'