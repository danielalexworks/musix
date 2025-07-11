# Audio Image Encoder

A simple Python tool to:
- Encode MP3s into `.npz` data files
- Generate grayscale images from audio data
- Reconstruct audio from images

---

## Requirements

Install libraries with:

```bash
pip install numpy scipy pydub pillow
```

---

## Usage

Run with:

```bash
python run.py
# or
python3 run.py
```

Follow the prompts:

- `e` : encode MP3s from folder
- `d` : decode NPZs from folder
- `g` : generate images from NPZ data folder
- `m` : generate MP3s from image folder
- `s` : generate MP3 from a single image
- `q` : quit

---

## Notes

- Creates directories automatically if they don't exist.
- Images store audio data pixel by pixel (0-255 mapped to -1.0 to 1.0).

---

MIT License
