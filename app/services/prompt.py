def get_image_generation_config(product_name: str):
    prompt = f"""
Generate product images suitable for an e-commerce app.

Analyze the object named "{product_name}" and keep a single, consistent identity:
- Same design, color, material, finish, and proportions across all images.

Generate multiple high-quality images of the same object,
each showing a different view.
always generate 4 images. Do not generate more or less. generate seperately.

Views to include:
- Image 1 Front view (straight-on).
- Image 2 Back view (exact opposite of the front).
- Image 3 Left side view (rotate the object 90° counterclockwise from the front view; show only the left edge).
- Image 4 Right side view (rotate the object 90° clockwise from the front view; show only the right edge).


Visual requirements:
- Orthographic or near-orthographic view.
- Object clearly visible and centered.
- Soft studio lighting that makes the object fully visible.
- Very dark background (near black).
- Consistent scale, color, material, and geometry.
- Side views must show a SINGLE instance of the object (one edge only), not both edges.


Each image must clearly show the object from one view.
"""
    angles = ["front", "back", "left", "right"]
    return prompt, angles
