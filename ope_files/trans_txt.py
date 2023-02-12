from dotenv import load_dotenv
import os
import deepl
import ope_files.get_file as get_file

load_dotenv()

class Trans:
    def trans_txt(self):
        translator = deepl.Translator(os.getenv('API_KEY'))
        file = get_file.GetFile.get_voice_txt()
        root, ext = os.path.splitext(file)
        # dir_name = './trans_files/'
        root, ext = os.path.splitext(file)
        result_file = root + '_DE' + ext
        return translator.translate_document_from_filepath(
            file,
            result_file,
            source_lang='JA',
            target_lang='DE'
        )