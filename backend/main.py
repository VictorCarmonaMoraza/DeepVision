from fastapi import FastAPI
from api import predict

app = FastAPI(title="DeepVision API")

# Incluir rutas
app.include_router(predict.router)
