import subprocess
import glob
import os
import ope_files.get_file as get_file

class WriteVoice:
    
    def __init__(self, file):
        self.file = file
    
    def write_voice(self):
        file = get_file()
        subprocess.run('whisper {} --language ja'.format(self.file), shell=True)