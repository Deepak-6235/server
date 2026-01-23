def get_image_generation_config(product_name: str):
    """
    Get the prompt and angles for AI image generation.
    
    Args:
        product_name: Name of the product to generate views for
        
    Returns:
        tuple: (prompt, angles_list)
    """
    prompt = f"""
    Reference Product: {product_name}
    Action: Using the provided image, generate 4 new high-quality images.
    Angles: 1. Front View, 2. Back View, 3. Left Side, 4. Right Side.
    Requirements: Maintain 100% color and texture consistency. Use a flat 2D style.
    """

    
    angles = ["front", "back", "left", "right"]
    
    return prompt, angles
