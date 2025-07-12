import os
import json
import numpy as np


def list_all_files_in_folder_by_type(ftype, folder_path):
    """
    Returns a list of absolute paths to all MP3 files in the specified folder (non-recursive).
    """
    ftype = ftype.lower()
    foundfiles = []
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(ftype):
                full_path = os.path.join(root, filename)
                foundfiles.append(os.path.abspath(full_path))
    return foundfiles


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


def ensure_dir_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print(f"📁 Created directory: {dir_path}")
    else:
        print(f"✅ Directory already exists: {dir_path}")