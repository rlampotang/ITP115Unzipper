#################################################################################################
#                                                                                               #
#   name:  Ryan Lampotang                                                                        #
#   email:  rlampota@usc.edu                                                                     #
#                                                                                               #
#   How To: Specify whether working with a lab or assignment                                     #
#################################################################################################

import os
from os import path
import zipfile
from pathlib import Path
import shutil

# Paths for assignments and labs (you can modify these paths as needed)
ASSIGNMENT_PATH = "/Users/ryanlampotang/Downloads/Lab 1 Download Aug 28, 2024 553 PM"

def flatten_folder(directory):
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            source = path.join(root, file)
            destination = path.join(directory, file)
            if source != destination:
                os.rename(source, destination)
        for dir in dirs:
            os.rmdir(path.join(root, dir))

def unzip(directory):
    print(os.listdir(directory))
    for item in os.listdir(directory):
        if item.endswith('.zip'):
            with zipfile.ZipFile(directory + "/" + item, 'r') as zip_ref:
                zip_ref.extractall(directory)
                os.remove(directory + "/" + item)

def process_assignment():
    flatten_folder(ASSIGNMENT_PATH)
    unzip(ASSIGNMENT_PATH)

def process_lab():
    flatten_folder(ASSIGNMENT_PATH)

def main():
    choice = input("Are you working with an assignment or a lab? (Enter 'assignment' or 'lab'): ").strip().lower()
    
    if choice == 'assignment':
        process_assignment()
    elif choice == 'lab':
        process_lab()
    else:
        print("Invalid choice. Please enter 'assignment' or 'lab'.")

main()
