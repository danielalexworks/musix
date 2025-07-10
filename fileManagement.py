import os
import json
import numpy as np

def list_mp3_files_in_folder(folder_path):
    """
    Returns a list of absolute paths to all MP3 files in the specified folder (non-recursive).
    """
    mp3_files = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.mp3'):
            full_path = os.path.join(folder_path, filename)
            mp3_files.append(os.path.abspath(full_path))
    return mp3_files


def list_mp3_files_recursive(folder_path):
    """
    Returns a list of absolute paths to all MP3 files in the specified folder and its subfolders.
    """
    mp3_files = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith('.mp3'):
                full_path = os.path.join(root, filename)
                mp3_files.append(os.path.abspath(full_path))
    return mp3_files


def list_npz_files_recursive(folder_path):
    """
    Returns a list of absolute paths to all NPZ files in the specified folder and its subfolders.
    """
    npz_files = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith('.npz'):
                full_path = os.path.join(root, filename)
                npz_files.append(os.path.abspath(full_path))
    return npz_files



def save_audio_data_to_npz(audio_data, npz_path):
    """
    Saves the audio data dict (sample_rate and samples) to a .npz binary file.
    Much smaller and faster to load than JSON.
    """
    sample_rate = audio_data["sample_rate"]
    samples = np.array(audio_data["samples"], dtype=np.float32)
    np.savez(npz_path, sample_rate=sample_rate, samples=samples)
    print(f"✅ Saved audio data to {npz_path}")

def load_audio_data_from_npz(npz_path):
    """
    Loads the audio data dict from a .npz file and returns it
    in the same dict format as before.
    """
    data = np.load(npz_path)
    sample_rate = data["sample_rate"].item()  # .item() to get scalar from 0-d array
    samples = data["samples"]
    return {
        "sample_rate": sample_rate,
        "samples": samples
    }


def save_audio_data_to_json(audio_data, json_path):
    """
    Saves the audio data dict (sample_rate and samples) to a JSON file.
    """
    with open(json_path, "w") as f:
        json.dump(audio_data, f)
    print(f"✅ Saved audio data to {json_path}")


def load_audio_data_from_json(json_path):
    """
    Loads the audio data dict from a JSON file.
    """
    with open(json_path, "r") as f:
        audio_data = json.load(f)
    return audio_data