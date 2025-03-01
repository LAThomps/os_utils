# -*- coding: utf-8 -*-
"""
Utilities using the python os library
"""

import os
from datetime import datetime
import yaml
import time

def log_exec_time(description: str):
    """
    Decorator function to log execution time of any function

    Use
    ---
    @loc_exec_time("here's a description")
    function(arg1, arg2)
        code ...
        return xyz
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start = time.time()

            print(f"Begin '{description}'\n")
            result = func(*args, **kwargs)
            end = time.time()

            time_elapsed = end - start
            mins_elapsed = time_elapsed / 60

            print()
            print(f"""
Completed '{description}' in {time_elapsed:.2f}s ({mins_elapsed:.2f} min)
            """.strip().replace("\n",""))
            print("-" * 90 + "\n")
            return result
        return wrapper
    return decorator

def get_file_size(
        file_path: str
    ) -> float:
    """
    Gets the size of a specified file in gigabytes
    
    Parameters
    ----------
        file_path: str
            To file in question.
            
    Returns
    -------
        gigs: float
            Size of file in GB.
    """
    return os.path.getsize(file_path) / (1e9)

def get_newest_files(path: str):
    """
    This function grabs the filepath of the most recently modified file
    in the directory specified in the path argument.
    
    Parameters
    ----------
    path: str filepath type
        filepath to directory user wishes to search for files
    
    Returns
    -------
    res: str
        file chosen to use from this function
    """
    sort = {}
    for file in os.listdir(path):
        sort[file] = os.path.getmtime(f'{path}/{file}')
    sort = sorted(sort, key=sort.get, reverse=True)
    res = os.path.join(path, sort[0])

    print(f"Using this file: {res}")
    
    return res

def get_file_mdate(path: str):
    """
    Gets the file modified date at a specified file path
    
    Parameters
    ----------
    path: str
        filepath for desired time
        
    Returns
    -------
    date: datetime obj
        datetime of the modified date
    """
    mtime = os.path.getmtime(path)
    mdate = datetime.fromtimestamp(mtime)
    return mdate

def read_yaml(
        file_path: str
    ):
    """
    Reads in data from global_params.yaml file

    Paramters
    ---------
    file_pathe: str
        Path to yaml file you want to read in.

    Returns
    -------
    stuff : dict
        yaml data as python dictionary
    """
    yaml_path = file_path
    with open(yaml_path, "r") as file:
        stuff = yaml.safe_load(file)
    return stuff


