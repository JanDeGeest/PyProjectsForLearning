#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 10:47:07 2022

@author: jhdegeest
"""
# Import packages
import shutil
import os

class FileMigration:
    
    def __init__(self, source_dir, target_dir, file_type):
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.file_type = file_type
        
        # Functions for file mutations
    def copy(self): #Copy all files with certain extention.
        file_names = os.listdir(self.source_dir)
        
        for file_name in file_names:
            if file_name.endswith(self.file_type):
                shutil.copy(os.path.join(self.source_dir, file_name), self.target_dir)

                print("\n Files successfully copied")

    def move(self): #Move all files with certain extention.
        file_names = os.listdir(self.source_dir)
        
        for file_name in file_names:
            if file_name.endswith(self.file_type):
                shutil.move(os.path.join(self.source_dir, file_name), self.target_dir)

                print("\n Files successfully moved.")

    def purge(self): #Delete all files with certain extention within target dir.
        file_names = os.listdir(self.target_dir)
                    
        for file_name in file_names:
            if file_name.endswith(self.file_type):
                os.remove(os.path.join(self.target_dir, file_name))

                print("\n Scripts successfully deleted")

if __name__ == "__main__": #Check if script runs as main.
    print("Don't execute this .py file, just import the class.")