import sys
sys.path.append("..")

from src import transcribe

import glob
import tqdm
import whisper


_MODEL_NAME = "medium.pt"  # name of model saved in models folder
_AUDIO_EXT = "m4a"         # format of audio files to be gathered from data folder
_LANGUAGE = "German"       # change for intended language   

output_format = "srt"
output_dir = "../output/"

audio_files = glob.glob(f"../data/*.{_AUDIO_EXT}")

print(f"Loading model from 'models/{_MODEL_NAME}'...")
model = whisper.load_model(f"../models/{_MODEL_NAME}")
print("Model loaded")
print()

for audio_file in audio_files:
    print(f"Processing audio: {audio_file} ...")
    transcribe.exec(model, audio_file, output_format, output_dir, _LANGUAGE)
    print()