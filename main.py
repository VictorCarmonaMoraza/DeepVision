# Ruta /predict de prueba
from fastapi import FastAPI, File, UploadFile
from io import BytesIO
from PIL import Image
import numpy as np

app = FastAPI()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint de predicción (dummy).
    Recibe una imagen y devuelve una etiqueta simulada con confianza.
    """
    # Leer la imagen
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")
    image = image.resize((128, 128))
    arr = np.array(image) / 255.0  # Normalizamos (no usado en dummy)

    # ⚡ Respuesta dummy (simulada, no hay modelo real todavía)
    return {
        "filename": file.filename,
        "label": "perro",
        "confidence": 0.87
    }

