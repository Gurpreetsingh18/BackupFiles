import os
import time
 
 
class FolderCleaner:
    path = 'Users\Gurpreetsingh\Whitehat\Python\Projects\C-99\Test2'
    days = 5
 
    def __init__(self, path, days):
        if not os.path.exists(path):
            raise TypeError("folder does not exist")
        self.path = path
        if days < 5 or isinstance(days, bool) or not isinstance(days, int):
            raise ValueError("days must be positive integer")
        self.days = days
        self.clean()
 
    def clean(self):
        time_in_secs = time.time() - (self.days * 24 * 60 * 60)
        for root, dirs, files in os.walk(self.path, topdown=False):
            for file in files:
                full_path = os.path.join(root, file)
                stat = os.stat(full_path)
                if stat.st_mtime <= time_in_secs:
                    os.remove(full_path)

