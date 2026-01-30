from rembg import remove
from PIL import Image
import io

def remove_background(input_path: str, output_path: str):
    """Remove background with default settings (fastest)"""
    with open(input_path, "rb") as f:
        img_bytes = f.read()

    # Use default settings - simplest and often fastest
    # rembg will use default u2net model automatically
    output = remove(img_bytes)

    image = Image.open(io.BytesIO(output))
    image.save(output_path)
