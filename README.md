# whisper-transcription

This repository contains a simple script to run the [whisper utility](https://github.com/openai/whisper) (v20231117) on multiple audio materials.
A short sample of the audio materials and a simple output are provided in the repository.

# How to?

In order to perform transcription, it is necessary to install `whisper` as detailed on the [github repository](https://github.com/openai/whisper)

More specifically you should:

1. install `ffmpeg`

2. create a virtual environment by running

        python3.11 -m venv [name_of_venv]

3. activate your virtual environment (on Linux/macOS) by running

        source [name_of_venv]/bin/activate

4. install `whisper` within the virtual environment

        pip install openai-whisper


Once the library is correctly installed, you're good to run our transcription script.

In order to do so:
- audio data should be saved in the `data` folder
- the selected model should be placed in the `models` folder
- you should check global parameters in the specified location in the `src/transcribe.py` script


Then run:

        python src/transcribe.py


Output in `.srt` format will be produced and saved to `output` folder.


----


Shield: [![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa]

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg