# -*- coding:utf-8 -*-
import configparser
import os
import glob

class Folder:
    
    """Простой класс объекта-папки"""
    
    def __init__(self,dirPath):
         self.dirPath = dirPath
         try:
             os.chdir(self.dirPath)
         except FileNotFoundError:
             os.mkdir(self.dirPath)
        
    def search_dir(self,mask):
        result = []
        masking = mask.split(' ')
        for i in masking:
            if i != []:
                result += glob.glob(i)
        return result