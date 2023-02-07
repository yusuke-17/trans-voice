import glob
import os

class GetFile:
    def get_voice():
        list_files = glob.glob('voices/*m4a')
        latest_voice = max(list_files, key=os.path.getmtime)
        return latest_voice