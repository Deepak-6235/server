def get_image_generation_config(product_name: str):
    prompt = f"""
Generate product images suitable for an e-commerce app.

Analyze the object named "{product_name}" and keep a single, consistent identity:
- Same design, color, material, finish, and proportions across all images.

Generate multiple high-quality images of the same object,
each showing a different view.
always generate 6 images. Do not generate more or less. generate seperately.

Views to include:
- Image 1 Front view (straight-on).
- Image 2 Back view (exact opposite of the front).
- Image 3 Left side view (rotate the object 90° counterclockwise from the front view; show only the left edge).
- Image 4 Right side view (rotate the object 90° clockwise from the front view; show only the right edge).
- Image 5 Top view (camera positioned directly above the object, looking straight down; show only the top face).
- Image 6 Bottom view (camera positioned directly below the object, looking straight up; show only the bottom face).


Visual requirements:
- Orthographic or near-orthographic view.
- Object clearly visible and centered.
- Soft studio lighting that makes the object fully visible.
- Background must be a single, uniform solid color with no gradients, light panels, reflections, borders, or side fills.
- Consistent scale, color, material, and geometry.
- Each image must contain only ONE physical instance of the product. Never show multiple objects in the same image.
- The product must remain in the SAME physical state in all images (do not open, close, unfold, or change configuration between views).
- The object’s geometry must be treated as fixed and identical across all images; do not alter, reinterpret, or redesign any part of the object between views.
- Side views must show a SINGLE instance of the object (one edge only), not both edges.
- Left and right side views must use strict orthographic projection with zero perspective or tilt.
- Top and bottom views must not show any side faces; only the flat top or bottom surface.
- Front view must be perfectly flat and face-on, with the camera perpendicular to the front surface (no tilt).


Each image must clearly show the object from one view.
"""
    angles = ["front", "back", "left", "right" ,"top", "bottom"]
    return prompt, angles
