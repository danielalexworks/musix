from PIL import Image
import numpy as np
import math



def audio_data_to_image(audio_data, img_path, width=None):
    """
    Creates an image from audio data samples.
    Each sample becomes a pixel. Values are mapped to [0, 255] grayscale.
    By default, tries to create a square image.
    """
    samples = audio_data["samples"]
    
    # If samples is a nested array (stereo), flatten to mono
    if samples.ndim > 1:
        samples = np.mean(samples, axis=1)
    
    # Normalize from [-1.0, 1.0] to [0, 255]
    pixel_values = ((samples + 1) * 127.5).clip(0, 255).astype(np.uint8)
    
    total_samples = len(pixel_values)
    
    # Determine width for square by default
    if width is None:
        width = math.isqrt(total_samples)
        if width == 0:
            width = 1
    
    # Compute height and pad if needed
    height = int(math.ceil(total_samples / width))
    padded_length = height * width
    
    if padded_length > total_samples:
        pixel_values = np.pad(pixel_values, (0, padded_length - total_samples),
                              mode='constant', constant_values=127)
    
    img = Image.fromarray(pixel_values.reshape(height, width), mode='L')
    img.save(img_path)
    print(f"✅ Saved image to {img_path}")
    return img


def image_to_audio_data(image_path, sample_rate):
    """
    Loads an image and converts it back to audio data format:
    - pixel values in [0,255] mapped back to [-1.0,1.0]
    Returns: { "sample_rate": ..., "samples": np.array(...) }
    """
    img = Image.open(image_path).convert('L')  # ensure grayscale
    pixel_values = np.array(img).flatten()
    
    # Map from [0,255] to [-1.0,1.0]
    samples = (pixel_values / 127.5) - 1.0
    
    return {
        "sample_rate": sample_rate,
        "samples": samples.astype(np.float32)
    }
