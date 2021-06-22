#%% - Import all necessary modules
from __future__ import division
print("INFORMATION: Importing modules...           ", end="")
# Standard modules
import pandas as pd
import datetime as dt
import numpy as np
import os                          # Note: os.walk is very slow

# Non-standard modules
import Tkinter as tk               # GUI creation
import tkMessageBox                # Windows message box

# Local modules
from classes import File_Data, All_Data
from functions import *
from constants import *
print "...complete."

#%% - Read main input text files

if __name__ == "__main__":
    print "INFORMATION: Importing A-weighted data...  "                                # Let user know process is intiated...
    compilation = All_Data(input_folder = root_folder, output_folder = write_folder)   # Create object which contains all data
    compilation.populate()                                                             # Cycle through all available files and fill object with data
    data = compilation.write_to_pandas()                                               # Move data from class object to pandas dataframe
    data = filter(data)                                                                # Select what columns you want to output
    data = reorder(data)                                                               # Make sure that it is in the correct time sequence
    data = pad(data)                                                                   # Pad to provide a continuous record
    write_data(data, write_folder)                                                     # Write out daily data files
    print '\nOuput data written to folder: {:>30s}'.format(write_folder)               # Output some helpful info for the user
    messageBox("Information","Information","Rion SLM data processing complete!")       # Alert user that processing has finished