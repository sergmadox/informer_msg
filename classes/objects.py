# -*- coding:utf-8 -*-
import configparser
import os
import glob

class Folder:
    
    """Простой класс объекта-папки"""
    
    def __init__(self,dirPath):
         self.dirPath = dirPath
         os.chdir(dirPath)
    
    def search_path(self):
        files = glob.glob("*.*")
        return files
    