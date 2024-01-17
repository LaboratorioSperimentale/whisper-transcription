import whisper
from whisper.utils import get_writer


def exec(audio_file_path, output_format, output_dir):


    
    writer = get_writer(output_format, output_dir)
    language = "German"
    #     **{"language":"de"}
    result = model.transcribe(audio_file_path, 
                              fp16=False, 
                              **{"verbose": False, "language": "German"})
    writer(result, audio_file_path)


if __name__ == "__main__":

########################################
    ### ONLY CHANGE THIS SECTION ###

    _MODEL_NAME = "base.pt"  # name of model saved in models folder
    _AUDIO_EXT = "mp3"       # format of audio files to be gathered from data folder


########################################



    import glob
    import tqdm

    output_format = "srt"
    output_dir = "output/"

    audio_files = glob.glob(f"data/*.{_AUDIO_EXT}")
    
    print(f"Loading model from 'models/{_MODEL_NAME}'...")
    model = whisper.load_model(f"models/{_MODEL_NAME}")
    print("Model loaded")
    print()

    for audio_file in audio_files:
        print(f"Processing audio: {audio_file} ...")
        exec(audio_file, output_format, output_dir)
        print()