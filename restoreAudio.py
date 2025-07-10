from pydub import AudioSegment
from io import BytesIO
import sys
import numpy as np
from scipy.io import wavfile

#OUTPUTS mp3 from audio_data
def create_audio_file(audio_data, output_path):
    sample_rate = audio_data["sample_rate"]
    samples = np.array(audio_data["samples"], dtype=np.float32)
    pcm_data = (samples * 32767).astype(np.int16)
    wavfile.write(output_path, sample_rate, pcm_data)
    return output_path