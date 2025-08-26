from io import BytesIO
from PIL import Image
import numpy as np

async def predict_image(file):
    contents = await file.read()
    image = Image.open(BytesIO(contents)).convert("RGB")
    image = image.resize((128, 128))
    arr = np.array(image) / 255.0

    # ⚡ Aquí iría la llamada al modelo real
    return {
        "filename": file.filename,
        "label": "perro",
        "confidence": 0.87
    }
