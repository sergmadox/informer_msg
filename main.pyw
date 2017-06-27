# -*- coding:utf-8 -*-
import configparser
import time
import ctypes
from classes import objects

ini = configparser.ConfigParser()
ini.read('conf.ini')

timer = ini.getint('Time', 'time')
mask = ini.get('Mask','mask')

def Mbox(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style )
    
def folderResult():
     
    try:
        for i in ini['Path']:
            dir_object = objects.Folder(ini['Path'][i])            
            result = dir_object.search_dir(mask)
            folder = ini['Path'][i]
            Message(folder, result)
    
    except:
        message = 'Ошибка конфигурации файла conf.ini'
        Mbox("Оповещение", message, 0x10 | 0x0)
        
def Message(folder,result):
    if result != []:
        message = "В папке " + str(folder).upper() + " у вас необработанный(е): \n" + str(result)
        Mbox("Оповещение", message, 0x30 | 0x0)

while True:
    time.sleep(timer)
    folderResult()