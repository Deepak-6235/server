from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os, uuid, time
from PIL import Image

from app.core.config import FRONTEND_URL, BASE_URL
from app.services.ai import analyze_and_generate_views
from app.services.bg import remove_background

app = FastAPI()

# Standard Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

@app.post("/ai/image")
async def process_image(
    product_name: str = Form(...),
    image: UploadFile = File(...)
):
    start_time = time.time()
    
    try:
        # 1. Save uploaded image safely
        ext = image.filename.split(".")[-1]
        base_name = str(uuid.uuid4())
        original_filename = f"{base_name}.{ext}"
        original_path = os.path.join(UPLOAD_DIR, original_filename)

        with open(original_path, "wb") as f:
            content = await image.read()
            f.write(content)

        # 2. Remove background
        bg_filename = f"{base_name}_bg.png"
        bg_path = os.path.join(UPLOAD_DIR, bg_filename)
        remove_background(original_path, bg_path)

        # 3. AI Generation Logic
        result = analyze_and_generate_views(bg_path, product_name, UPLOAD_DIR)
        views = result["views"]
        analysis = result["analysis"]

        return {
            "status": "success",
            "product_name": product_name,
            "analysis": analysis,
            "side_views": {
                k: f"{BASE_URL}/uploads/{v}" for k, v in views.items()
            },
            "processing_time": f"{round(time.time() - start_time, 2)}s"
        }
        
    except Exception as e:
        # If the whole process (like file saving) fails, return a 500
        raise HTTPException(status_code=500, detail=str(e))