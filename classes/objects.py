# -*- coding:utf-8 -*-
import configparser
import os
import glob

class Folder:
    
    """Простой класс объекта-папки"""
    
    def __init__(self,dirPath):
         self.dirPath = dirPath
         try:
             os.chdir(dirPath)
         except FileNotFoundError:
             os.mkdir(dirPath)
        
    def search_dir(self,mask):
        result = []
        masking = mask.split(' ')
        for i in masking:
            find = glob.glob(i)
            result += find
        return result