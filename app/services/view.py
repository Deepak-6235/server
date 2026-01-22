from PIL import Image, ImageOps

def generate_views(input_path: str, output_dir: str, base_name: str):
    img = Image.open(input_path)

    front = img
    right = img.transform(img.size, Image.AFFINE, (1, 0.1, 0, 0, 1, 0))
    left = img.transform(img.size, Image.AFFINE, (1, -0.1, 0, 0, 1, 0))
    back = ImageOps.mirror(img)

    front.save(f"{output_dir}/{base_name}_front.png")
    right.save(f"{output_dir}/{base_name}_right.png")
    back.save(f"{output_dir}/{base_name}_back.png")
    left.save(f"{output_dir}/{base_name}_left.png")

    return {
        "front": f"{base_name}_front.png",
        "right": f"{base_name}_right.png",
        "back": f"{base_name}_back.png",
        "left": f"{base_name}_left.png",
    }
