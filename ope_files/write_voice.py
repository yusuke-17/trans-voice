import subprocess
import ope_files.get_file as get_file

class WriteVoice:
    def write_voice(self):
        file = get_file.GetFile.get_voice()
        subprocess.run('whisper {} --language ja -o ./output_files'.format(file), shell=True)