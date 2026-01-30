from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os, uuid, time
from PIL import Image

from app.core.config import FRONTEND_URL, BASE_URL
from app.services.ai import analyze_and_generate_views, analyze_and_generate_video
from app.services.bg import remove_background

app = FastAPI()

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
        ext = image.filename.split(".")[-1]
        base_name = str(uuid.uuid4())
        original_filename = f"{base_name}.{ext}"
        original_path = os.path.join(UPLOAD_DIR, original_filename)

        with open(original_path, "wb") as f:
            content = await image.read()
            f.write(content)

        bg_filename = f"{base_name}_bg.png"
        bg_path = os.path.join(UPLOAD_DIR, bg_filename)
        remove_background(original_path, bg_path)

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
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/ai/video")
async def process_video(
    product_name: str = Form(...),
    image: UploadFile = File(...),
    skip_bg_removal: bool = Form(False)  # Optional flag to skip background removal
):
    start_time = time.time()

    try:
        ext = image.filename.split(".")[-1]
        base_name = str(uuid.uuid4())
        original_filename = f"{base_name}.{ext}"
        original_path = os.path.join(UPLOAD_DIR, original_filename)

        with open(original_path, "wb") as f:
            content = await image.read()
            f.write(content)

        # Skip background removal by default for video - Veo can handle backgrounds
        # This saves 5-10 seconds of processing time
        if skip_bg_removal:
            print("⚡ Skipping background removal for faster processing")
            input_image_path = original_path
        else:
            print("⚠️  Background removal enabled (adds 5-10s)")
            bg_filename = f"{base_name}_bg.png"
            bg_path = os.path.join(UPLOAD_DIR, bg_filename)
            remove_background(original_path, bg_path)
            input_image_path = bg_path

        result = analyze_and_generate_video(input_image_path, product_name, UPLOAD_DIR)
        video_url = result["video"]  # This is now the S3 URL
        analysis = result["analysis"]

        return {
            "status": "success",
            "product_name": product_name,
            "analysis": analysis,
            "video_url": video_url,  # Return S3 URL directly
            "processing_time": f"{round(time.time() - start_time, 2)}s"
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))










