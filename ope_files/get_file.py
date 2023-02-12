import glob
import os

class GetFile:
    def get_voice():
        list_files = glob.glob('voices/*m4a')
        latest_voice = max(list_files, key=os.path.getmtime)
        return latest_voice

    def get_voice_txt():
        list_files = glob.glob('output_files/*txt')
        latest_txt = max(list_files, key=os.path.getmtime)
        return latest_txt