import processAudio as pa
import restoreAudio as ra
import fileManagement as fm
import imageConvert as ic
import os

mp3Folder = "inputmp3s/"             # .mp3s go in here
dataFolder = "data/"            # where .npz data outputs
outputFolder = 'outputmp3s/'    # where new .mp3s output
imageOutFolder = 'outputImages/'
newMp3Folder = 'newMp3s/'
samplerate = 16000

fm.ensure_dir_exists(mp3Folder)
fm.ensure_dir_exists(dataFolder)
fm.ensure_dir_exists(outputFolder)
fm.ensure_dir_exists(imageOutFolder)
fm.ensure_dir_exists(newMp3Folder)


print("\r\n\r\n")
print("==================================")
print(f"mp3 in Path: {mp3Folder}")
print(f"data out Path: {dataFolder}")
print(f"mp3 out Path: {outputFolder}")
print("==================================\r\n\r\n")
print("SET SOURCE AND DESTINATION FOLDERS IN run.py\r\n\r\n")
step = input("""input \r\n
	e : encode mp3s from folder
	d : decode npzs from folder
	g : generate images from npz data folder
	m : generate mp3s from image folder
	s : generate mp3 from image
	q : quit
	\ninput option: """)

if step.upper() == "E":
	#LOADS mp3s and saves npzs
	mp3FilePaths = fm.list_all_files_in_folder_by_type(".mp3", mp3Folder)
	pa.load_mp3_convert_and_store_as_npz(mp3FilePaths, dataFolder, samplerate)

elif  step.upper() == "D":
	#LOADS npzs and saves mp3s
	npzFilePaths = fm.list_all_files_in_folder_by_type(".npz", dataFolder)
	pa.load_npz_convert_and_store_as_mp3(npzFilePaths, outputFolder)

elif step.upper() == "G":
	#LOADS npzs and saves pngs
	npzFilePaths = fm.list_all_files_in_folder_by_type(".npz", dataFolder)
	pa.load_npz_convert_and_store_as_png(npzFilePaths, imageOutFolder)

elif step.upper() == "M":
	pngFilePaths = fm.list_all_files_in_folder_by_type(".png", imageOutFolder)
	pa.load_png_convert_and_store_as_mp3(pngFilePaths, newMp3Folder, samplerate)

elif step.upper() == "S":
	input("Provide file path to image file: ")
	print("this feature not yet implemented")
	'''

	imagePath = outpath = os.path.join(imageOutFolder, "02 - Radiohead - Bodysnatchers.png")
	data = ic.image_to_audio_data(imagePath, samplerate)
	outpath = os.path.join(newMp3Folder, "02 - Radiohead - Bodysnatchers.png.mp3")
	output = ra.create_audio_file(data,outpath)
	print(output)
	'''

