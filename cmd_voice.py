import ope_files.write_voice as write_voice
import ope_files.trans_txt as trans_txt

def main():
    write = write_voice.WriteVoice()
    write.write_voice()
    trans = trans_txt.Trans()
    trans.trans_txt()

if __name__ == '__main__':
    main()
