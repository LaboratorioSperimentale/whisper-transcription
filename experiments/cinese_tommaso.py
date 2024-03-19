import sys
import os
sys.path.append("..")

from src import transcribe

import glob
import tqdm
import whisper


output_format = "srt"
_AUDIO_EXT = "mp3"  # format of audio files to be gathered from data folder
audio_files = list(glob.glob(f"../data/*.{_AUDIO_EXT}"))


'''
# modello base
_MODEL_NAME = "base.pt"  # name of model saved in models folder
_LANGUAGE_S = "Mandarin"       # change for intended language   

output_dir = "../output_base/"
os.makedirs(output_dir, mode=0o777, exist_ok=True)

print(f"Loading model from 'models/{_MODEL_NAME}'...")
model = whisper.load_model(f"../models/{_MODEL_NAME}")
print("Model loaded")
print()

for audio_file in audio_files:
    print(f"Processing audio: {audio_file} ...")
    transcribe.exec(model, audio_file, output_format, output_dir, _LANGUAGE)
    print()
'''

# modello "medium"
_MODEL_NAME_M = "medium.pt"  # name of model saved in models folder
_LANGUAGE_M = "Mandarin"       # change for intended language   

output_dir = "../output_medium/"
os.makedirs(output_dir, mode=0o777, exist_ok=True)

print(f"Loading model from 'models/{_MODEL_NAME_M}'...")
model = whisper.load_model(f"../models/{_MODEL_NAME_M}")
print("Model loaded")
print()

for audio_file_M in audio_files:
    print(f"Processing audio: {audio_file_M} ...")
    transcribe.exec(model, audio_file_M, output_format, output_dir, _LANGUAGE_M)
    print()

'''
# modello "large"
_MODEL_NAME_L = "large-v3.pt"  # name of model saved in models folder
_LANGUAGE_L = "Mandarin"       # change for intended language   

output_dir = "../output_large/"
os.makedirs(output_dir, mode=0o777, exist_ok=True)

print(f"Loading model from 'models/{_MODEL_NAME_L}'...")
model = whisper.load_model(f"../models/{_MODEL_NAME_L}")
print("Model loaded")
print()

for audio_file_L in audio_files:
    print(f"Processing audio: {audio_file_L} ...")
    transcribe.exec(model, audio_file_L, output_format, output_dir, _LANGUAGE)
    print()
'''

