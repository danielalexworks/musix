from pydub import AudioSegment
from io import BytesIO
import sys
import numpy as np
from scipy.io import wavfile
from scipy.signal import resample
import fileManagement as fm
import restoreAudio as ra
import imageConvert as ic
import os

# LOADS PNG Files
# CONVERT to mp3
def load_png_convert_and_store_as_mp3(pngFilePaths, outputFolder, sample_rate):
    for p in pngFilePaths:
        outfile = os.path.splitext(os.path.basename(p))[0] + "_png.mp3"
        outpath = os.path.join(outputFolder, outfile)
        print(outpath)
        audio_data = ic.image_to_audio_data(p, sample_rate)
        output = ra.create_audio_file(audio_data,outpath)
        

# LOADS NPZ Files
# CONVERT to png
def load_npz_convert_and_store_as_png(npzFilePaths, outputFolder):
    for n in npzFilePaths:
        outfile = os.path.splitext(os.path.basename(n))[0] + ".png"
        outpath = os.path.join(outputFolder, outfile)
        print(outpath)
        data = fm.load_audio_data_from_npz(n)
        outtput = ic.audio_data_to_image(data, outpath)


# LOADS NPZ Files
# CONVERT to mp3
def load_npz_convert_and_store_as_mp3(npzFilePaths, outputFolder):
    for n in npzFilePaths:
        outfile = os.path.splitext(os.path.basename(n))[0] + ".mp3"
        outpath = os.path.join(outputFolder, outfile)
        print(outpath)
        data = fm.load_audio_data_from_npz(n)
        output = ra.create_audio_file(data,outpath)


#LOOP THROUGH FILE PATHS
#CONVERT TO WAV DATA
#ENCODE TO BUFFER
#SAVE TO FILE [originalfilename.json]
def load_mp3_convert_and_store_as_npz(mp3FilePaths, dataFolder, samplerate):
    for m in mp3FilePaths:
        outfile = os.path.splitext(os.path.basename(m))[0] + ".npz"
        outpath = os.path.join(dataFolder, outfile)
        wav = convert_mp3_to_wav_in_memory(m, samplerate)
        data = encode_audio_from_buffer(wav)
        fm.save_audio_data_to_npz(data, outpath)



def encode_audio_from_buffer(wav_buffer):
    """
    Reads a WAV file from an in-memory buffer (BytesIO) and returns
    a dict with the sample_rate and normalized samples.
    """
    sample_rate, data = wavfile.read(wav_buffer)

    if data.dtype == np.int16:
        samples = data.astype(np.float32) / 32768
    elif data.dtype == np.int32:
        samples = data.astype(np.float32) / 2147483648
    elif data.dtype == np.float32:
        samples = data
    else:
        raise ValueError(f"Unsupported audio format: {data.dtype}")

    samples = samples.tolist()

    return {
        "sample_rate": sample_rate,
        "samples": samples
    }



def convert_mp3_to_wav_in_memory(mp3_file_path, target_sample_rate=None):
    """
    Converts an MP3 file to WAV format and returns a BytesIO object
    containing the WAV data (in-memory file).
    Optionally resamples to target_sample_rate.
    """
    audio = AudioSegment.from_mp3(mp3_file_path)

    if target_sample_rate:
        audio = audio.set_frame_rate(target_sample_rate)

    wav_buffer = BytesIO()
    audio.export(wav_buffer, format="wav")
    wav_buffer.seek(0)
    return wav_buffer
