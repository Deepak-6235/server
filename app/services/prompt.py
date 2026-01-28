def get_image_generation_config(product_name: str):
    prompt = f"""
    OBJECT IDENTITY ANALYSIS:
    1. Examine the provided image and the name "{product_name}".
    2. Define the 'Object Language': Identify the primary materials (glass, metal, paper, plastic), the structural geometry (box, cylinder, organic), and the functional faces (which side is the front, where are the logical interactable parts).
    3. Based on this internal definition, formulate a mental model of the object's hidden sides to ensure 100% structural logic.

    GENERATION STEP (using Nano Banana):
    Using the identity established above, generate 4 new high-resolution images:
    - Image 1: FRONT: The primary face of the object, perfectly centered.
    - Image 2: BACK: The opposite face, inferring logical details (labels, spines, or ports) based on the front.
    - Image 3: LEFT PROFILE: A 90-degree side view.
    - Image 4: RIGHT PROFILE: A 90-degree side view.

    STRICT VISUAL CONSTRAINTS:
    - CAMERA: All four views must use a perfect orthographic projection with no lens distortion. The object must fill 80% of the frame.
    - LIGHTING: Use a 'Rim Light' setup—soft studio highlights that trace the outer edges to define the shape against the black background.
    - CONSISTENCY: Absolute 100% consistency in color, material texture, and scale across all four frames.
    - BACKGROUND: Solid #000000 black.
    """

    angles = ["front", "back", "left", "right"]
    return prompt, angles