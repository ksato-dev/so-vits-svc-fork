# -*- coding: utf-8 -*-

import glob
import subprocess
import sys
from pprint import pprint
import pathlib

if __name__ == '__main__':
    tgt_dir = sys.argv[1]
    model_path = sys.argv[2]
    cfg_path = sys.argv[3]
    wav_path_list = glob.glob(tgt_dir + '/**/*.wav', recursive=True)
    # pprint(wav_path_list)
    # venv_activate_path = pathlib.Path(venv_dir + '/Scripts/activate')
    # print(venv_activate_path)
    # process = subprocess.Popen(venv_activate_path.absolute(), stdout=subprocess.PIPE)
    # process.wait()

    # input_wav_file = sys.argv[2]
    # infer_cmd = 'svc infer ' + input_wav_file
    # print(venv_activate_path)
    for wav_path in wav_path_list:
        infer_cmd_elems = ['svc', 'infer', wav_path, '-m', model_path, '-c', cfg_path, '-o', wav_path]
        infer_cmd = ' '.join(infer_cmd_elems)
        print(infer_cmd)
        print('Process', wav_path, '.')
        # process = subprocess.Popen(infer_cmd, stdout=subprocess.PIPE)
        process = subprocess.Popen(infer_cmd)
        process.wait()
        print('Done.')
