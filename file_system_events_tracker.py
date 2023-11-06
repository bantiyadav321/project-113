import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/91821/Downloads"
to_dir = "C:/Users/91821/Downloads/image_file"


# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

    #1_on_created
    def on_created(self, event):
        print(f"Hey,{event.src_path} has been craeated!")

    #2_on_deleted
    def on_deleted(self, event):
        print(f"Oops! Someone deleted{event.src_path}!")
        

    #3_on_modified
    def on_modified(self, event):
        print(f"Hey there !,{event.src_path} has been modified")
        

    #4_on_moved
    def on_modified(self, event):
        print(f"Hey there !,{event.src_path} has been modified")
        

        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:
 while True:
    time.sleep(2)
    print("running...")
except KeyboardInterrupt:
    print("stop")
    observer.stop()
