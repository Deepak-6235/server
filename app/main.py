from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os, uuid

from app.core.config import FRONTEND_URL, BASE_URL
from app.services.ai import analyze_product
from app.services.bg import remove_background
from app.services.view import generate_views

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
    ext = image.filename.split(".")[-1]
    base_name = str(uuid.uuid4())
    original_path = f"{UPLOAD_DIR}/{base_name}.{ext}"

    with open(original_path, "wb") as f:
        f.write(await image.read())

    # Background removal
    bg_path = f"{UPLOAD_DIR}/{base_name}_bg.png"
    remove_background(original_path, bg_path)

    # AI analysis
    ai_analysis = analyze_product(bg_path, product_name)

    # Generate 4 views
    views = generate_views(bg_path, UPLOAD_DIR, base_name)

    return {
        "product_name": product_name,
        "analysis": ai_analysis,
        "views": {
            k: f"{BASE_URL}/uploads/{v}" for k, v in views.items()
        }
    }
