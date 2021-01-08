import os 
import glob

paths = ['5_Model_0', '6_Model_1']
for path in paths:
    wav_files = glob.glob(os.path.join(path, '*.wav'))
    for wav_file in wav_files:
        new_name = os.path.basename(wav_file).split('-')[1]
        new_file = os.path.join(path, new_name+'.wav')
        os.system('mv {} {}'.format(wav_file, new_file))

