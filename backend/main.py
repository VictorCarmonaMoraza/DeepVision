from fastapi import FastAPI
from api import predict

app = FastAPI(
    title="DeepVision API",
    description="""
    🚀 API for DeepVision Project.  
    Upload an image and get predictions with class labels and confidence levels.  

    ## Endpoints
    - `/predict`: Upload an image and get the predicted label.  
    """,
    version="1.0.0",
    contact={
        "name": "Victor M",
        "url": "https://www.linkedin.com/in/tu-perfil",
        "email": "tuemail@example.com",
    },
    license_info={
        "name": "MIT License",
    },
)

# Incluir rutas
app.include_router(predict.router)
