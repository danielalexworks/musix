import processAudio as pa
import restoreAudio as ra
import fileManagement as fm
import os

mp3Folder = "inputmp3s/"             # .mp3s go in here
dataFolder = "data/"            # where .npz data outputs
outputFolder = 'outputmp3s/'    # where new .mp3s output
samplerate = 16000
print("\r\n\r\n")
print("==================================")
print(f"mp3 in Path: {mp3Folder}")
print(f"data out Path: {dataFolder}")
print(f"mp3 out Path: {outputFolder}")
print("==================================\r\n\r\n")
print("SET SOURCE AND DESTINATION FOLDERS IN run.py\r\n\r\n")
step = input("input E to encode mp3s from folder, D to decode npzs from folder : ")

if step.upper() == "E":
	#LOADS mp3s and saves npzs
	mp3FilePaths = fm.list_mp3_files_recursive(mp3Folder)
	pa.load_mp3_convert_and_store_as_npz(mp3FilePaths, dataFolder, samplerate)

elif  step.upper() == "D":
	#LOADS npzs and saves mp3s
	npzFilePaths = fm.list_npz_files_recursive(dataFolder)
	pa.load_npz_convert_and_store_as_mp3(npzFilePaths, outputFolder)

