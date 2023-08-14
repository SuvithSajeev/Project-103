import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = 'C:/Users/suvis/Downloads'

dir_tree = {
    'Image': ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    'Video': ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    'PDF': ['.pdf'],
    'PPT': ['.ppt'],
    'Docs': ['.docs','.docx'],
    'Text': ['.txt'],
    'Csv': ['.csv'],
    'Xls': ['.xls'],
    'Setup': ['.exe', '.bin', '.cmd', '.msi', '.dmg'],
    'Zip':['.zip'],
    'Audio':['.mp3','.wav','m4a'],
    'Sb3':['.sb3']
}


class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
        
    def on_deleted(self, event):
        print(f"Oops! Someone has deleted {event.src_path} !")
    
    def on_modified(self, event):
        print(f"Ohh, someone modified {event.src_path} !")
    
    def on_moved(self, event):
        print(f"Ohh, someone renamed/moved {event.src_path} !")

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir)
observer.start()


try :
    while True:
        time.sleep(2)
        print('Running...')
except KeyboardInterrupt:
    print('Stopped!')
    observer.stop()