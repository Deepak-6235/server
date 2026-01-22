from google import genai
from PIL import Image
from google.genai import types
from app.core.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_product(image_path: str, product_name: str) -> str:
    image = Image.open(image_path)

    prompt = f"""
    This is a product named "{product_name}". 
    
    Step 1: Deep Analysis
    Analyze the product in the image and provide:
    - product category
    - primary and secondary materials
    - geometric shape and structural complexity
    - symmetry (Identify if it's identical from all sides or has unique features on the back)
    - suitability for 360-degree view (Score 1-10 and reasoning)

    Step 2: Generation Instructions
    Based on the analysis above, provide a "Generation Prompt" for an image creator to generate:
    1. A front-facing view (matching the original)
    2. A direct back-view (inferring details not seen)
    3. A left-profile view
    4. A right-profile view
    
    Format the response as a clear technical specification for a 360-degree rotatable asset. 
    Ensure all descriptions maintain a "flat 3D style, front-facing" aesthetic to match the project requirements.
    """

    response = client.models.generate_content(
            # model="gemini-3-pro-image-preview",
            model="gemini-2.5-flash",
        contents=[prompt, image]
    )

    return response.text
    