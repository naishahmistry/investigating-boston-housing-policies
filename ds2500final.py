"""
Naisha Mistry & Olivia Yeung
DS 2500
Spring 2024
Final Project
"""

# Import modules, libraries, and functions and save constants
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
from scipy import stats
import sys
import pandas as pd

sys.path.insert(0, "../utils")
from utils import get_filenames, read_csv, lst_to_dct, median, normalize

DIRECTORY = "housing_data"
YEARS = ["2018, 2020, 2021, 2022"]

def get_index(filenames, year):
    """ Parameters: a list of filenames (strings), a year (string)
        Does: finds filename corresponding to that year and its index
        Returns: returns index of filename (integer)
    """
    for i in range(len(filenames)):
        if year in filenames[i]:
            return i
    
def get_file(file_lst, file_ind):
    """ Parameters: a list of filenames (strings), index of desired file
        (integer)
        Does: opens the desired file and saves the data into a dictionary
        Returns: a dictionary
    """ 
    return pd.read_csv(file_lst[file_ind])

def get_years(file_lst):
    """ Parameters: a list of filenames (strings)
        Does: searches for year within the filename, saves the years in a 
        list, and converts the years from strings to integers
        Returns: a list of years (integers)
    """
    years = []
    for file in file_lst:
        if "2018" in file:
            year = file.split("-")[-5]
        else: 
            year_csv = file.split("-")[-1]
            year = year_csv.strip(".csv")
        years.append(year)
    years = [int(year) for year in years]
    return years

def main():
    filenames = get_filenames(DIRECTORY)
    print(filenames)
    
    # get 2022 housing data
    twentytwo = get_index(filenames, "2022")
    print(twentytwo)
    get_file(filenames, twentytwo)
    
    # thirteen_data = get_file(filenames, get_index(filenames, "2013"))
    years = get_years(filenames)
    print(years)
    
    
    
    

main()
