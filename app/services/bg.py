from rembg import remove
from PIL import Image
import io

def remove_background(input_path: str, output_path: str):
    with open(input_path, "rb") as f:
        img_bytes = f.read()

    output = remove(img_bytes)
    image = Image.open(io.BytesIO(output))
    image.save(output_path)
