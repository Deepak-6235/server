def get_image_generation_config(product_name: str):
    prompt = f"""
Generate a high-quality 360-degree product rotation video suitable for an e-commerce product page.

OBJECT IDENTITY LOCK:
Analyze the product named "{product_name}" and establish a single, fixed physical identity.
- The product’s geometry, proportions, materials, colors, surface details, and textures must remain identical throughout the entire video.
- Treat the object as one real, physical product placed on a studio turntable.

STATE CONSISTENCY:
- The product must remain in the SAME physical state for the entire video.
- Do not open, close, fold, unfold, extend, detach, or reconfigure any part during rotation.

ROTATION INSTRUCTIONS:
- Perform a smooth, continuous 360-degree horizontal rotation around the vertical axis.
- Rotation speed must be constant and steady (no acceleration or jitter).
- The camera must remain completely stationary.
- The product must stay centered in the frame at all times.

CAMERA & PROJECTION:
- Use strict orthographic or near-orthographic projection.
- No camera movement, zooming, tilting, or perspective shifts.
- The product should fill approximately 70–80% of the frame consistently.

LIGHTING:
- Use soft, neutral studio lighting.
- Lighting must remain constant across all frames.
- No flicker, no moving highlights, no changing reflections.

BACKGROUND:
- Background must be a single, uniform solid color (pure black or near black).
- No gradients, no borders, no light panels, no reflections, no studio cards, no side fills.

VIDEO QUALITY:
- Clean, sharp, high-resolution video.
- No motion blur.
- No text, labels, UI elements, watermarks, or overlays.
- No additional objects in the scene.

CONSISTENCY RULE (CRITICAL):
- Do NOT redesign, reinterpret, or modify any part of the product during rotation.
- Every frame must represent the same object viewed from a different angle only.

FINAL RESULT:
The output should look like a professional studio turntable product video used on Amazon or Flipkart 360° viewers.

"""
    return prompt
